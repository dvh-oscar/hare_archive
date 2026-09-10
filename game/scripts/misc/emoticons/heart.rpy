init offset = -1

################################################################################
## (10) HEART / LOVE (하트)
################################################################################

transform _fx_heart_icon_motion:
    anchor (0.5, 0.5)
    zoom 0.7
    pos (89, 64)
    block:
        easein 0.18 zoom 0.80 rotate 6
        easeout 0.18 zoom 0.68 rotate -6
        easein 0.18 zoom 0.76 rotate 4
        easeout 0.18 zoom 0.70 rotate 0
        pause 0.3
        # repeat

image _fx_heart_base = Fixed(
    Transform("images/emoticons/Emoticon_Balloon_N.png", zoom=0.7, pos=(0, 0)),
    At("images/emoticons/Emoticon_Heart.png", _fx_heart_icon_motion),
    xsize=179,
    ysize=139,
    fit_first=False
)

image fx heart = At("_fx_heart_base", _fx_pop_root(duration=0.5, sfx="sfx_emoticon_heart"))
image fx love = "fx heart"
