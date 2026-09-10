init offset = -1

################################################################################
## (6) SURPRISED (놀람 !?)
################################################################################

transform _fx_surprised_root(duration=1.5, sfx="sfx_emoticon_surprise"):
    anchor (0.5, 1.0)
    zoom 0.0 alpha 0.0 yoffset 30
    function _fx_play_sfx(sfx)
    easein 0.14 zoom 1.15 yoffset -18 alpha 1.0
    easeout 0.10 zoom 0.95 yoffset 4
    easein 0.08 zoom 1.0 yoffset 0
    parallel:
        block:
            linear 0.05 xoffset 4
            linear 0.05 xoffset -4
            linear 0.05 xoffset 0
    parallel:
        pause duration
        linear 0.6 alpha 0.0

image _fx_surprised_base = Fixed(
    Transform("images/emoticons/Emoticon_Exclamation.png", zoom=0.7, pos=(0, 0)),
    Transform("images/emoticons/Emoticon_Question.png", zoom=0.7, pos=(45, 0)),
    xsize=117,
    ysize=104,
    fit_first=False
)

image fx surprised = At("_fx_surprised_base", _fx_surprised_root(duration=1.5, sfx="sfx_emoticon_surprise"))
image fx surprise = "fx surprised"
