init offset = -1

################################################################################
## (5) EXCLAIM (느낌표)
################################################################################

transform _fx_exclaim_motion(duration=1.5, sfx="sfx_emoticon_exclaim"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 yoffset 20
    function _fx_play_sfx(sfx)
    easein 0.12 zoom 0.80 yoffset -8 alpha 1.0
    easeout 0.08 zoom 0.67 yoffset 2
    easein 0.06 zoom 0.70 yoffset 0
    pause duration
    linear 0.6 alpha 0.0

image fx exclaim = At("images/emoticons/Emoticon_ExclamationMark.png", _fx_exclaim_motion(duration=1.5, sfx="sfx_emoticon_exclaim"))
image fx exclamation = "fx exclaim"
image fx exclamation_mark = "fx exclaim"
