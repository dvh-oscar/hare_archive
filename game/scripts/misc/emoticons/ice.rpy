init offset = -1

################################################################################
## (15) ICE (얼어붙음 / 굳음 / 경직)
################################################################################

transform _fx_ice1_atl:
    pos (-30, 0)
    anchor (0.5, 0.5)
    zoom 0.7
    block:
        linear 0.08 xoffset 3 yoffset -2
        linear 0.08 xoffset -3 yoffset 2
        repeat

transform _fx_ice2_atl:
    pos (30, 20)
    anchor (0.5, 0.5)
    zoom 0.7
    block:
        linear 0.09 xoffset -2 yoffset 3
        linear 0.09 xoffset 2 yoffset -3
        repeat

transform _fx_ice3_atl:
    pos (10, -20)
    anchor (0.5, 0.5)
    zoom 0.7
    block:
        linear 0.07 xoffset 2 yoffset 2
        linear 0.07 xoffset -2 yoffset -2
        repeat

image _fx_ice_base = Fixed(
    At("images/emoticons/Emoticon_Ice_V.png", _fx_ice1_atl),
    At("images/emoticons/Emoticon_Ice_M.png", _fx_ice2_atl),
    At("images/emoticons/Emoticon_Ice_S.png", _fx_ice3_atl),
    xsize=180,
    ysize=160,
    fit_first=False
)

transform _fx_ice_root(duration=1.5, sfx="sfx_emoticon_sad"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0
    function _fx_play_sfx(sfx)
    easein 0.12 zoom 1.15 alpha 1.0
    easeout 0.08 zoom 1.00
    pause duration
    linear 0.6 alpha 0.0

image fx ice = At("_fx_ice_base", _fx_ice_root(duration=1.5, sfx="sfx_emoticon_sad"))
image fx freeze = "fx ice"
