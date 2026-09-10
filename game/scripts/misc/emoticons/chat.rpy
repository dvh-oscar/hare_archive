init offset = -1

################################################################################
## (9) CHAT (대화 / 수다)
################################################################################

transform _fx_chat_motion(duration=1.5, sfx="sfx_emoticon_chat"):
    anchor (0.5, 0.5)
    zoom 0.0 alpha 0.0
    function _fx_play_sfx(sfx)
    easein 0.15 zoom 0.80 alpha 1.0
    easeout 0.10 zoom 0.68
    easein 0.08 zoom 0.70
    parallel:
        block:
            ease 0.25 rotate 12
            ease 0.25 rotate -12
            # repeat
    parallel:
        pause duration
        linear 0.3 alpha 0.0

image fx chat = At("images/emoticons/Emoticon_Chat.png", _fx_chat_motion(duration=0.5, sfx="sfx_emoticon_chat"))
image fx talk = "fx chat"
