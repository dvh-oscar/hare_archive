init offset = -1

################################################################################
## (8) ANXIETY / ANXIOUS (초조 / 불안 파동)
################################################################################

transform _fx_anxiety_pulse:
    anchor (0.5, 0.5)
    zoom 0.7
    pos (89, 69)
    block:
        ease 0.18 xzoom 0.95 yzoom 0.62
        ease 0.18 xzoom 0.62 yzoom 0.95
        repeat

transform _fx_anxiety_shake:
    block:
        linear 0.06 xoffset 2
        linear 0.06 xoffset -2
        # repeat

image _fx_anxiety_base = Fixed(
    Transform("images/emoticons/Emoticon_Balloon_N.png", zoom=0.7, pos=(0, 0)),
    At("images/emoticons/Emoticon_Anxiety.png", _fx_anxiety_pulse),
    xsize=179,
    ysize=139,
    fit_first=False
)

transform _fx_anxiety_root(duration=1.5, sfx="sfx_emoticon_sad"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0 yoffset 15
    function _fx_play_sfx(sfx)
    easein 0.15 zoom 1.15 yoffset -6 alpha 1.0
    easeout 0.10 zoom 0.95 yoffset 2
    easein 0.08 zoom 1.0 yoffset 0
    parallel:
        _fx_anxiety_shake
    parallel:
        pause duration
        linear 0.6 alpha 0.0

image fx anxiety = At("_fx_anxiety_base", _fx_anxiety_root(duration=0.5, sfx="sfx_emoticon_sad"))
image fx anxious = "fx anxiety"
