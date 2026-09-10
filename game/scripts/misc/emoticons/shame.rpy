init offset = -1

################################################################################
## (1) SHY / SHAME (홍조 / 부끄러움)
################################################################################

transform _fx_shy_icon_motion:
    anchor (0.5, 0.5)
    zoom 0.7
    pos (89, 64)
    block:
        easein 0.22 rotate 7 zoom 0.73
        easeout 0.22 rotate -7 zoom 0.68
        repeat

image _fx_shy_base = Fixed(
    Transform("images/emoticons/Emoticon_Balloon_N.png", zoom=0.7, pos=(0, 0)),
    At("images/emoticons/Emoticon_Shy.png", _fx_shy_icon_motion),
    xsize=179,
    ysize=139,
    fit_first=False
)

image fx shy = At("_fx_shy_base", _fx_pop_root(duration=1.5, sfx="sfx_emoticon_shy"))
image fx shame = "fx shy"
