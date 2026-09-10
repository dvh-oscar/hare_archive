init offset = -1

################################################################################
## (11) SWEAT (식은땀 - 1회 흘러내림)
################################################################################

transform _fx_sweat1_motion:
    zoom 0.7
    pos (0, 0)
    yoffset 0
    linear 0.46 yoffset 49

transform _fx_sweat2_motion:
    zoom 0.7
    pos (49, 0)
    yoffset 0
    linear 0.46 yoffset 84

image _fx_sweat_base = Fixed(
    At("images/emoticons/Emoticon_Sweat_1.png", _fx_sweat1_motion),
    At("images/emoticons/Emoticon_Sweat_2.png", _fx_sweat2_motion),
    xsize=82,
    ysize=130,
    fit_first=False
)

transform _fx_sweat_root(duration=1.5, sfx="sfx_emoticon_sweat"):
    anchor (0.5, 0.5)
    alpha 0.0
    function _fx_play_sfx(sfx)
    linear 0.2 alpha 1.0
    pause duration
    linear 0.6 alpha 0.0

image fx sweat = At("_fx_sweat_base", _fx_sweat_root(duration=1.5, sfx="sfx_emoticon_sweat"))
