init offset = -1

################################################################################
## (7) ANGRY / AGGRO (분노 / 어그로 마크)
################################################################################

transform _fx_angry_twitch:
    block:
        easein 0.12 zoom 1.15
        easeout 0.10 zoom 0.95
        easein 0.10 zoom 1.10
        easeout 0.10 zoom 1.00
        pause 0.35
        repeat

transform _fx_angry_root(duration=1.5, sfx="sfx_emoticon_angry"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0
    function _fx_play_sfx(sfx)
    easein 0.12 zoom 1.20 alpha 1.0
    easeout 0.08 zoom 0.95
    easein 0.06 zoom 1.00
    parallel:
        _fx_angry_twitch
    parallel:
        pause duration
        linear 0.6 alpha 0.0

image _fx_angry_base = Fixed(
    Transform("images/emoticons/Emoticon_Aggro.png", zoom=0.7, pos=(15, -10), rotate=-120),
    Transform("images/emoticons/Emoticon_Aggro.png", zoom=0.7, pos=(20, 50), rotate=0),
    Transform("images/emoticons/Emoticon_Aggro.png", zoom=0.7, pos=(-30, 30), rotate=90),
    xsize=105,
    ysize=85,
    fit_first=False
)

image fx angry = At("_fx_angry_base", _fx_angry_root(duration=1.5, sfx="sfx_emoticon_angry"))
image fx aggro = "fx angry"
