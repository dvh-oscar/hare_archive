init offset = -1

## About 스크린 ###################################################################
##
## 이 스크린은 게임과 렌파이 엔진 크레딧과 저작권 정보를 표시합니다.
##
## 특별할 것이 없으므로 스크린을 새로 커스터마이징하여 만드는 예제이기도 합니다.

screen about():

    tag menu

    ## 이 use 명령어로 game_menu 스크린을 이 스크린 내에 불러옵니다. use 명령어
    ## 하위블럭(vbox 내용)은 game_menu 스크린 내 transclude 명령어가 있는 곳에
    ## 다시 불려집니다.
    use game_menu(_("버전정보"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("버전 [config.version!t]\n")

            ## gui.about 의 내용은 보통 options.rpy에 있습니다.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
