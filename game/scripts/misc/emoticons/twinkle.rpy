init offset = -1

################################################################################
## (14) TWINKLE (반짝임 / 별)
################################################################################

transform _fx_twinkle1_atl:
    pos (-79, 0)
    anchor (0.5, 0.5)
    block:
        ease 0.32 zoom 0.52 rotate 15
        ease 0.32 zoom 0.68 rotate -15
        repeat

transform _fx_twinkle2_atl:
    pos (0, 40)
    anchor (0.5, 0.5)
    block:
        ease 0.45 zoom 0.22 rotate -20
        ease 0.45 zoom 0.32 rotate 20
        repeat

transform _fx_twinkle3_atl:
    pos (0, -60)
    anchor (0.5, 0.5)
    block:
        ease 0.38 zoom 0.40 rotate 18
        ease 0.38 zoom 0.54 rotate -18
        repeat

transform _fx_twinkle_root(duration=1.5, sfx="sfx_emoticon_twinkle"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0
    function _fx_play_sfx(sfx)
    easein 0.15 zoom 1.1 alpha 1.0
    easeout 0.10 zoom 1.0
    pause duration
    linear 0.6 alpha 0.0

image _fx_twinkle_base = Fixed(
    At("images/emoticons/Emoticon_Twinkle.png", _fx_twinkle1_atl),
    At("images/emoticons/Emoticon_Twinkle.png", _fx_twinkle2_atl),
    At("images/emoticons/Emoticon_Twinkle.png", _fx_twinkle3_atl),
    xsize=160,
    ysize=180,
    fit_first=False
)

image fx twinkle = At("_fx_twinkle_base", _fx_twinkle_root(duration=1.5, sfx="sfx_emoticon_twinkle"))
image fx star = "fx twinkle"
