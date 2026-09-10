#!/usr/bin/env python3
"""
tools/convert_wav.py

Blue Archive Collections/Blue Archive BGMs 디렉토리 내의
'Theme'로 시작하는 WAV 파일들을 MP3(320kbps)로 일괄 변환하여
Blue Archive Collections/Blue Archive BGMs/mp3 디렉토리에 저장합니다.
원본 WAV 파일은 유지됩니다.
"""

import argparse
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def find_ffmpeg() -> str:
    """ffmpeg 실행 파일 경로를 탐색합니다."""
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        return ffmpeg_path

    # mac/linux 일반 설치 경로 확인
    candidates = [
        "/opt/homebrew/bin/ffmpeg",
        "/usr/local/bin/ffmpeg",
        "/usr/bin/ffmpeg",
    ]
    for candidate in candidates:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    raise FileNotFoundError(
        "ffmpeg 실행 파일을 찾을 수 없습니다. ffmpeg가 시스템에 설치되어 있는지 확인해주세요."
    )


def convert_file(ffmpeg_path: str, src_path: Path, dst_path: Path, bitrate: str) -> tuple[Path, bool, str]:
    """단일 WAV 파일을 MP3로 변환합니다."""
    cmd = [
        ffmpeg_path,
        "-y",               # 기존 출력 파일 덮어쓰기 허용
        "-i", str(src_path),
        "-codec:a", "libmp3lame",
        "-b:a", bitrate,
        str(dst_path),
    ]

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return src_path, True, ""
        else:
            return src_path, False, result.stderr.strip()
    except Exception as e:
        return src_path, False, str(e)


def main():
    parser = argparse.ArgumentParser(description="Convert Theme WAV files to MP3 format.")
    default_base = Path(__file__).resolve().parent.parent / "Blue Archive Collections" / "Blue Archive BGMs"
    default_output = default_base / "mp3"

    parser.add_argument(
        "--input-dir",
        type=Path,
        default=default_base,
        help=f"입력 WAV 파일 디렉토리 (기본값: {default_base})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_output,
        help=f"출력 MP3 파일 디렉토리 (기본값: {default_output})",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        default="Theme",
        help="변환 대상 파일 접두어 (기본값: 'Theme')",
    )
    parser.add_argument(
        "--bitrate",
        type=str,
        default="320k",
        help="MP3 오디오 비트레이트 (기본값: '320k')",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="동시 변환 스레드 수 (기본값: CPU 코어 수 기준)",
    )

    args = parser.parse_args()

    input_dir: Path = args.input_dir.resolve()
    output_dir: Path = args.output_dir.resolve()

    if not input_dir.is_dir():
        print(f"❌ 입력 디렉토리가 존재하지 않습니다: {input_dir}", file=sys.stderr)
        sys.exit(1)

    try:
        ffmpeg_path = find_ffmpeg()
        print(f"🔧 ffmpeg 감지됨: {ffmpeg_path}")
    except FileNotFoundError as err:
        print(f"❌ {err}", file=sys.stderr)
        sys.exit(1)

    # 출력 디렉토리 생성
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 출력 디렉토리: {output_dir}")

    # 변환 대상 파일 검색 (대소문자 무관 prefix 매칭 및 .wav 확장자)
    prefix_lower = args.prefix.lower()
    wav_files = sorted([
        f for f in input_dir.iterdir()
        if f.is_file() and f.suffix.lower() == ".wav" and f.name.lower().startswith(prefix_lower)
    ])

    total_files = len(wav_files)
    if total_files == 0:
        print(f"ℹ️ '{args.prefix}'로 시작하는 WAV 파일을 찾지 못했습니다.")
        return

    print(f"🎵 변환 대상 WAV 파일: {total_files}개 발견 (비트레이트: {args.bitrate})")

    workers = args.workers or min(32, (os.cpu_count() or 4) + 4)
    print(f"⚡ 병렬 작업 스레드 수: {workers}")

    success_count = 0
    fail_count = 0
    failures = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_file = {}
        for wav_path in wav_files:
            mp3_path = output_dir / f"{wav_path.stem}.mp3"
            future = executor.submit(convert_file, ffmpeg_path, wav_path, mp3_path, args.bitrate)
            future_to_file[future] = (wav_path, mp3_path)

        completed_count = 0
        for future in as_completed(future_to_file):
            wav_path, mp3_path = future_to_file[future]
            completed_count += 1
            src_file, success, error_msg = future.result()
            if success:
                success_count += 1
                print(f"[{completed_count}/{total_files}] ✅ 변환 완료: {wav_path.name} -> {mp3_path.name}")
            else:
                fail_count += 1
                failures.append((wav_path.name, error_msg))
                print(f"[{completed_count}/{total_files}] ❌ 변환 실패: {wav_path.name}\n    오류: {error_msg}")

    print("\n" + "=" * 50)
    print(f"📊 변환 결과 요약")
    print(f"  - 총 대상: {total_files}개")
    print(f"  - 성공: {success_count}개")
    print(f"  - 실패: {fail_count}개")
    print(f"  - 저장 위치: {output_dir}")
    print("=" * 50)

    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
