init offset = -1

################################################################################
## (16) SIGH (한숨)
################################################################################

transform _fx_sigh_motion(duration=1.5, sfx="sfx_emoticon_sigh"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 xoffset 0 yoffset 0
    function _fx_play_sfx(sfx)
    alpha 1.0
    easein 0.40 zoom 0.67
    parallel:
        pause 0.20
        ease 0.35 xoffset -30 yoffset 30
    pause duration
    linear 0.5 alpha 0.0

image fx sigh = At("images/emoticons/Emoji_Sigh.png", _fx_sigh_motion(duration=1.5, sfx="sfx_emoticon_sigh"))
