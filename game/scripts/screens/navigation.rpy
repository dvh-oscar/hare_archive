init offset = -1

################################################################################
## Main과 Game Menu 스크린
################################################################################

## Navigation 스크린 ##############################################################
##
## 이 스크린은 메인메뉴와 게임외 메뉴에 포함되어 다른 메뉴로 이동하거나 게임을
## 시작/종료할 수 있게 합니다.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("시작하기") action Start()
            

        else:

            textbutton _("대사록") action ShowMenu("history")

            textbutton _("저장하기") action ShowMenu("save")

        textbutton _("불러오기") action ShowMenu("load")

        textbutton _("환경설정") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("메인 메뉴") action MainMenu()

        textbutton _("버전정보") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## 도움말 메뉴는 모바일 디바이스와 맞지 않아 불필요합니다.
            textbutton _("조작방법") action ShowMenu("help")

        if renpy.variant("pc"):

            ## iOS에서는 종료 버튼이 금지되어 있으며 Android 및 웹에서는 불필요
            ## 합니다.
            textbutton _("종료하기") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
