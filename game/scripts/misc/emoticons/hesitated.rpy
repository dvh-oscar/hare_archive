init offset = -1

################################################################################
## (4) HESITATED / DOT (망설임 - 일반 말풍선 + 도트 점 3개 1회 순차 등장 후 유지)
################################################################################

transform _fx_hesitated_dot1:
    zoom 0.7
    pos (37, 66)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

transform _fx_hesitated_dot2:
    zoom 0.7
    pos (75, 66)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    pause 0.4
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

transform _fx_hesitated_dot3:
    zoom 0.7
    pos (113, 66)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    pause 0.8
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

image _fx_hesitated_base = Fixed(
    Transform("images/emoticons/Emoticon_Balloon_N.png", zoom=0.7, pos=(0, 0)),
    At("images/emoticons/Emoticon_Idea.png", _fx_hesitated_dot1),
    At("images/emoticons/Emoticon_Idea.png", _fx_hesitated_dot2),
    At("images/emoticons/Emoticon_Idea.png", _fx_hesitated_dot3),
    xsize=179,
    ysize=139,
    fit_first=False
)

image fx hesitated = At("_fx_hesitated_base", _fx_think_root(duration=1.5, sfx="sfx_emoticon_dot"))
image fx dot = "fx hesitated"
image fx speech = "fx hesitated"
