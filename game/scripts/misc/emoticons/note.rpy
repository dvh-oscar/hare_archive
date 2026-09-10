init offset = -1

################################################################################
## (12) NOTE (음표 / 콧노래)
################################################################################

transform _fx_note_motion(duration=1.5, sfx="sfx_emoticon_twinkle"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 xoffset 0 rotate 0
    function _fx_play_sfx(sfx)
    parallel:
        easein 0.20 zoom 0.75 alpha 1.0
        easeout 0.15 zoom 0.70
    parallel:
        linear 2.5 xoffset -120
    parallel:
        block:
            ease 0.35 rotate 6 yoffset -6
            ease 0.35 rotate -6 yoffset 0
            repeat
    parallel:
        pause duration
        linear 0.6 alpha 0.0

image fx note = At("images/emoticons/Emoticon_Note.png", _fx_note_motion(duration=1.5, sfx="sfx_emoticon_twinkle"))
image fx music = "fx note"
