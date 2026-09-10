init offset = -1

################################################################################
## (13) RESPOND (주목 / 반응 강조선 3개)
################################################################################

transform _fx_respond_root(duration=1.5, sfx="sfx_emoticon_respond"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0
    function _fx_play_sfx(sfx)
    easein 0.12 zoom 1.20 alpha 1.0
    easeout 0.08 zoom 0.95
    easein 0.06 zoom 1.00
    pause duration
    linear 0.5 alpha 0.0

image _fx_respond_base = Fixed(
    Transform("images/emoticons/Emoticon_Action.png", zoom=0.7, pos=(0, -50), rotate=-20),
    Transform("images/emoticons/Emoticon_Action.png", zoom=0.7, pos=(20, 36)),
    Transform("images/emoticons/Emoticon_Action.png", zoom=0.7, pos=(0, 72), rotate=20),
    xsize=95,
    ysize=115,
    fit_first=False
)

image fx respond = At("_fx_respond_base", _fx_respond_root(duration=1.5, sfx="sfx_emoticon_respond"))
image fx action = "fx respond"
image fx sparkle = "fx respond"
