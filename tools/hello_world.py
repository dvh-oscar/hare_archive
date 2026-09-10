#!/usr/bin/env python3
"""
tools/hello_world.py

UHD(3840x2160) 규격 투명 이미지 캔버스에 입력 이미지를 중앙 배치하고
상하(높이)를 규격에 맞게 리사이즈하여 저장하는 이미지 처리 유틸리티입니다.

추가로 짙은 회색 배경에 투명도 75%의 이미지와 중앙 십자선 좌표평면을 오버레이한
가이드 이미지(tools/grid)도 함께 생성합니다.
"""

import argparse
import sys
import time
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("❌ Pillow 라이브러리가 설치되어 있지 않습니다.")
    print("   'pip install -r requirements.txt' 또는 run_tool 스크립트를 실행하여 설치하세요.")
    sys.exit(1)


# 지원하는 이미지 확장자 목록
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def create_grid_image(
    resized_img: Image.Image,
    output_path: Path,
    paste_x: int,
    paste_y: int,
    target_width: int = 3840,
    target_height: int = 2160,
    opacity: float = 0.75,
    bg_color: tuple = (36, 36, 36),
    axis_color: tuple = (255, 10, 150),  # 밝은 시안(고대비)
    subgrid_color: tuple = (50, 50, 50),  # 보조 그리드 선
) -> Path:
    """짙은 회색 배경에 투명도(opacity)가 적용된 이미지를 배치하고,

    정중앙(좌표평면 축)에 십자선을 그려 가이드 이미지를 생성합니다.
    """
    # 1. 짙은 회색 RGB 배경 생성
    grid_canvas = Image.new("RGB", (target_width, target_height), bg_color)

    # 2. 보조 눈금선(그리드) 그리기 (200px 간격, 은은한 선)
    draw = ImageDraw.Draw(grid_canvas)
    center_x = target_width // 2
    center_y = target_height // 2

    # 세로 보조선
    for x in range(center_x % 200, target_width, 200):
        if x != center_x:
            draw.line([(x, 0), (x, target_height)], fill=subgrid_color, width=1)

    # 가로 보조선
    for y in range(center_y % 200, target_height, 200):
        if y != center_y:
            draw.line([(0, y), (target_width, y)], fill=subgrid_color, width=1)

    # 3. 투명도(불투명도 75%) 적용된 이미지 합성
    img_with_alpha = resized_img.convert("RGBA")
    alpha = img_with_alpha.getchannel("A")
    # 원본 알파 채널에 지정된 불투명도(예: 0.75) 곱 적용
    adjusted_alpha = alpha.point(lambda p: int(p * opacity))
    img_with_alpha.putalpha(adjusted_alpha)

    # 배경에 이미지 합성 (알파 마스크 이용)
    grid_canvas.paste(img_with_alpha, (paste_x, paste_y), mask=img_with_alpha)

    # 4. 이미지 상단에 중앙 십자선(X축, Y축 좌표평면) 오버레이
    # 가로축 (X축: y = center_y)
    draw.line(
        [(0, center_y), (target_width, center_y)], fill=axis_color, width=10
    )
    # 세로축 (Y축: x = center_x)
    draw.line(
        [(center_x, 0), (center_x, target_height)], fill=axis_color, width=10
    )

    # 원점(중심점) 타겟 마크 (중앙 식별용 링 & 점)
    ring_radius = 12
    draw.ellipse(
        [
            (center_x - ring_radius, center_y - ring_radius),
            (center_x + ring_radius, center_y + ring_radius),
        ],
        outline=axis_color,
        width=2,
    )
    draw.ellipse(
        [(center_x - 3, center_y - 3), (center_x + 3, center_y + 3)],
        fill=axis_color,
    )

    # 5. 저장
    output_path.parent.mkdir(parents=True, exist_ok=True)
    grid_canvas.save(output_path, "PNG")
    return output_path


def process_image(
    image_path: Path,
    output_dir: Path,
    grid_dir: Path = None,
    target_width: int = 3840,
    target_height: int = 2160,
    opacity: float = 0.75,
) -> tuple[Path, Path | None]:
    """단일 이미지를 target_height에 맞게 비율을 유지하여 리사이즈한 뒤,

    1) (target_width, target_height) 크기의 투명 캔버스 정중앙에 배치하여 저장하고
    2) 필요 시 tools/grid 가이드 이미지도 함께 생성하여 저장합니다.
    """
    with Image.open(image_path) as img:
        # 투명도를 지원하기 위해 RGBA로 변환
        img_rgba = img.convert("RGBA")
        orig_w, orig_h = img_rgba.size

        # 상하(높이)를 target_height에 맞추어 비율 유지 리사이즈
        scale = target_height / orig_h
        new_w = round(orig_w * scale)
        new_h = target_height

        # 고품질 Lanczos 필터로 리사이즈
        resample_filter = getattr(Image.Resampling, "LANCZOS", Image.LANCZOS)
        resized_img = img_rgba.resize((new_w, new_h), resample=resample_filter)

        # 정중앙 배치 좌표 계산
        paste_x = (target_width - new_w) // 2
        paste_y = (target_height - new_h) // 2

        # 1. 투명 캔버스 생성 및 저장 (tools/outputs)
        canvas = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
        canvas.paste(resized_img, (paste_x, paste_y), mask=resized_img)

        output_filename = f"{image_path.stem}.png"
        output_path = output_dir / output_filename
        output_dir.mkdir(parents=True, exist_ok=True)
        canvas.save(output_path, "PNG")

        # 2. 그리드 가이드 이미지 생성 및 저장 (tools/grid)
        grid_path = None
        if grid_dir is not None:
            grid_path = grid_dir / output_filename
            create_grid_image(
                resized_img=resized_img,
                output_path=grid_path,
                paste_x=paste_x,
                paste_y=paste_y,
                target_width=target_width,
                target_height=target_height,
                opacity=opacity,
            )

        print(
            f"  ✔ [{image_path.name}] {orig_w}x{orig_h} "
            f"-> 리사이즈: {new_w}x{new_h} "
            f"-> 캔버스: {target_width}x{target_height} (좌표: x={paste_x}, y={paste_y})"
        )
        print(f"     └─ 캔버스 출력 : {output_path}")
        if grid_path:
            print(f"     └─ 그리드 가이드: {grid_path}")

        return output_path, grid_path


def get_image_files(input_path: Path):
    """입력 경로(파일 또는 디렉토리)에서 지원하는 이미지 파일 목록을 반환합니다."""
    if input_path.is_file():
        if input_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            return [input_path]
        return []
    elif input_path.is_dir():
        files = [
            p
            for p in input_path.iterdir()
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
        ]
        files.sort(key=lambda p: p.name.lower())
        return files
    return []


def parse_args():
    parser = argparse.ArgumentParser(
        description="UHD(3840x2160) 투명 이미지 캔버스 중앙 배치 및 좌표평면 그리드 가이드 생성 유틸리티"
    )
    script_dir = Path(__file__).resolve().parent
    default_input = script_dir / "inputs"
    default_output = script_dir / "outputs"
    default_grid = script_dir / "grid"

    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=default_input,
        help=f"입력 이미지 파일 또는 폴더 경로 (기본값: {default_input})",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=default_output,
        help=f"투명 캔버스 출력 폴더 경로 (기본값: {default_output})",
    )
    parser.add_argument(
        "-g",
        "--grid-dir",
        type=Path,
        default=default_grid,
        help=f"좌표평면 그리드 가이드 출력 폴더 경로 (기본값: {default_grid})",
    )
    parser.add_argument(
        "--no-grid",
        action="store_true",
        help="그리드 가이드 이미지 생성을 비활성화합니다.",
    )
    parser.add_argument(
        "--opacity",
        type=float,
        default=0.75,
        help="그리드 가이드 이미지의 캐릭터 투명도/불투명도 비율 (기본값: 0.75)",
    )
    parser.add_argument(
        "-W",
        "--width",
        type=int,
        default=4096,
        help="목표 캔버스 너비 (기본값: 3840, UHD 규격)",
    )
    parser.add_argument(
        "-H",
        "--height",
        type=int,
        default=4096,
        help="목표 캔버스 높이 (기본값: 2160, UHD 규격)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("=" * 70)
    print("🎨 UHD 투명 캔버스 & 좌표평면 그리드 생성 유틸리티")
    print("=" * 70)
    print(f"📌 목표 규격    : {args.width} × {args.height} (UHD/4K)")
    print(f"📌 입력 경로    : {args.input}")
    print(f"📌 투명 출력    : {args.output}")
    if not args.no_grid:
        print(f"📌 그리드 출력  : {args.grid_dir} (투명도 {int(args.opacity * 100)}%)")
    print("-" * 70)

    if not args.input.exists():
        print(f"⚠️  입력 경로가 존재하지 않습니다: {args.input}")
        print("   'tools/inputs' 디렉토리에 이미지를 추가하거나 --input 옵션으로 경로를 지정하세요.")
        sys.exit(1)

    image_files = get_image_files(args.input)
    if not image_files:
        print(f"⚠️  처리할 이미지 파일을 찾을 수 없습니다: {args.input}")
        print(f"   지원 포맷: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        sys.exit(0)

    print(f"🔍 총 {len(image_files)}개의 이미지 파일을 발견했습니다. 처리를 시작합니다...\n")

    start_time = time.time()
    success_count = 0
    target_grid_dir = None if args.no_grid else args.grid_dir

    for idx, img_path in enumerate(image_files, start=1):
        try:
            process_image(
                image_path=img_path,
                output_dir=args.output,
                grid_dir=target_grid_dir,
                target_width=args.width,
                target_height=args.height,
                opacity=args.opacity,
            )
            success_count += 1
        except Exception as e:
            print(f"  ❌ [{img_path.name}] 처리 중 오류 발생: {e}")

    elapsed = time.time() - start_time
    print("-" * 70)
    print(f"✨ 작업 완료! 총 {success_count}/{len(image_files)}개 파일 변환 성공 (소요 시간: {elapsed:.2f}초)")
    print(f"📂 투명 이미지 결과 : {args.output.resolve()}")
    if not args.no_grid:
        print(f"📂 그리드 가이드 결과: {args.grid_dir.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
