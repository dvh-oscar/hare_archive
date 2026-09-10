init offset = -1

################################################################################
## (3) THINKING (생각 중 - 구름 말풍선 + 도트 3개 1회 순차 등장 후 유지)
################################################################################

transform _fx_thinking_dot1:
    zoom 0.7
    pos (37, 68)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

transform _fx_thinking_dot2:
    zoom 0.7
    pos (75, 68)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    pause 0.4
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

transform _fx_thinking_dot3:
    zoom 0.7
    pos (113, 68)
    anchor (0.5, 0.5)
    alpha 0.0 zoom 0.0
    pause 0.8
    easein 0.15 zoom 0.75 alpha 1.0
    easeout 0.08 zoom 0.70

image _fx_thinking_base = Fixed(
    Transform("images/emoticons/Emoticon_Balloon_T.png", zoom=0.7, pos=(0, 0)),
    At("images/emoticons/Emoticon_Idea.png", _fx_thinking_dot1),
    At("images/emoticons/Emoticon_Idea.png", _fx_thinking_dot2),
    At("images/emoticons/Emoticon_Idea.png", _fx_thinking_dot3),
    xsize=179,
    ysize=155,
    fit_first=False
)

transform _fx_think_root(duration=1.5, sfx="sfx_emoticon_think"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 yoffset 15
    function _fx_play_sfx(sfx)
    easein 0.15 zoom 1.12 yoffset -6 alpha 1.0
    easeout 0.10 zoom 0.96 yoffset 2
    easein 0.08 zoom 1.0 yoffset 0
    pause duration
    linear 0.6 alpha 0.0

image fx thinking = At("_fx_thinking_base", _fx_think_root(duration=1.5, sfx="sfx_emoticon_think"))
image fx think = "fx thinking"
