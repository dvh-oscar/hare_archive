init offset = -1

################################################################################
## 블루아카이브 감정표현 (이모티콘 FX) - 공통 설정 및 기본 트랜스폼
################################################################################

## 1. 전용 FX 레이어 설정
## 'fx' 레이어를 'master' 바로 위에 배치하여 캐릭터 스프라이트에 가려지지 않고 항상 앞에 출력되도록 합니다.
init -2 python:
    if "fx" not in config.layers:
        master_idx = config.layers.index("master")
        config.layers.insert(master_idx + 1, "fx")
    config.tag_layer["fx"] = "fx"


## 2. 전역 설정 (사운드 활성화 및 볼륨 조절)
## 스크립트 도중 `$ fx_enable_sfx = False` 또는 `$ fx_sfx_volume = 0.5` 등으로 조절 가능합니다.
default fx_enable_sfx = True
default fx_sfx_volume = 1.0

init -1 python:
    # 렌파이 세이브/로드(Pickle) 완벽 호환을 위한 최상위 모듈 함수 기반 효과음 재생 핸들러
    def _fx_play_sfx_direct(sfx_name, st):
        if st == 0 and getattr(renpy.store, "fx_enable_sfx", True) and sfx_name:
            sfx_file = getattr(audio, sfx_name, None)
            if sfx_file:
                vol = getattr(renpy.store, "fx_sfx_volume", 1.0)
                try:
                    renpy.sound.play(sfx_file, relative_volume=vol)
                except TypeError:
                    renpy.sound.play(sfx_file)
        return None

    def _fx_sfx_shy(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_shy", st)
    def _fx_sfx_question(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_question", st)
    def _fx_sfx_think(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_think", st)
    def _fx_sfx_dot(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_dot", st)
    def _fx_sfx_exclaim(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_exclaim", st)
    def _fx_sfx_surprise(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_surprise", st)
    def _fx_sfx_angry(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_angry", st)
    def _fx_sfx_sad(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_sad", st)
    def _fx_sfx_chat(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_chat", st)
    def _fx_sfx_heart(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_heart", st)
    def _fx_sfx_sweat(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_sweat", st)
    def _fx_sfx_twinkle(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_twinkle", st)
    def _fx_sfx_respond(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_respond", st)
    def _fx_sfx_sigh(trans, st, at): return _fx_play_sfx_direct("sfx_emoticon_sigh", st)
    def _fx_sfx_none(trans, st, at): return None

    _FX_SFX_MAP = {
        "sfx_emoticon_shy": _fx_sfx_shy,
        "sfx_emoticon_question": _fx_sfx_question,
        "sfx_emoticon_think": _fx_sfx_think,
        "sfx_emoticon_dot": _fx_sfx_dot,
        "sfx_emoticon_exclaim": _fx_sfx_exclaim,
        "sfx_emoticon_surprise": _fx_sfx_surprise,
        "sfx_emoticon_angry": _fx_sfx_angry,
        "sfx_emoticon_sad": _fx_sfx_sad,
        "sfx_emoticon_chat": _fx_sfx_chat,
        "sfx_emoticon_heart": _fx_sfx_heart,
        "sfx_emoticon_sweat": _fx_sfx_sweat,
        "sfx_emoticon_twinkle": _fx_sfx_twinkle,
        "sfx_emoticon_respond": _fx_sfx_respond,
        "sfx_emoticon_sigh": _fx_sfx_sigh,
    }

    def _fx_play_sfx(sfx_name):
        return _FX_SFX_MAP.get(sfx_name, _fx_sfx_none)

    # 기본 이모티콘 헬퍼 함수
    def fx_show(name, at_pos=None, xoffset=0, yoffset=0, duration=1.5):
        tag_name = f"fx {name}"
        renpy.show(tag_name)


## 3. 위치 트랜스폼 프리셋 (Position Transforms)
transform fx_center:
    xpos 0.50
    ypos 0.18
    anchor (0.5, 0.5)

transform fx_left:
    xpos 0.32
    ypos 0.18
    anchor (0.5, 0.5)

transform fx_right:
    xpos 0.85
    ypos 0.18
    anchor (0.5, 0.5)

transform fx_pos(x=0.5, y=0.18):
    xpos x
    ypos y
    anchor (0.5, 0.5)


## 4. 공통 팝업 루트 모션 트랜스폼 (지속 시간: 1.5초)
transform _fx_pop_root(duration=1.5, sfx=None):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 yoffset 15
    function _fx_play_sfx(sfx)
    easein 0.15 zoom 1.15 yoffset -8 alpha 1.0
    easeout 0.10 zoom 0.95 yoffset 2
    easein 0.08 zoom 1.0 yoffset 0
    pause duration
    linear 0.6 alpha 0.0
