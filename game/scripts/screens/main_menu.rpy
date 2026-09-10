init offset = -1

## Main Menu 스크린 ###############################################################
##
## 렌파이가 시작할 때 메인메뉴를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 이렇게 하면 다른 메뉴 화면이 모두 교체됩니다.
    tag menu

    add gui.main_menu_background

    ## 이 빈 프레임은 기본 메뉴를 어둡게 만듭니다.
    frame:
        style "main_menu_frame"

    ## use 명령어로 스크린 내에 다른 스크린을 불러옵니다. 메인 메뉴 스크린의 내
    ## 용물은 navigation 스크린에 있습니다.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
