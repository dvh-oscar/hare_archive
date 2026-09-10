init offset = -1

################################################################################
## (2) QUESTION / DOUBT (물음표 / 의문)
################################################################################

transform _fx_question_motion(duration=1.5, sfx="sfx_emoticon_question"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 yoffset 20 rotate -15
    function _fx_play_sfx(sfx)
    easein 0.14 zoom 0.80 yoffset -8 rotate 8 alpha 1.0
    easeout 0.10 zoom 0.67 yoffset 2 rotate -4
    easein 0.08 zoom 0.70 yoffset 0 rotate 0
    pause duration
    linear 0.6 alpha 0.0

image fx question = At("images/emoticons/Emoticon_QuestionMark.png", _fx_question_motion(duration=1.5, sfx="sfx_emoticon_question"))
image fx question_mark = "fx question"
image fx doubt = "fx question"
