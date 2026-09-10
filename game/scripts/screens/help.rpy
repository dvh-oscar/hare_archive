init offset = -1

## Help 스크린 ####################################################################
##
## 입력장치의 기능을 설명합니다. 각 입력장치별 설정은 keyboard_help, mouse_help,
## gamepad_help 스크린을 각각 불러와서 출력합니다.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")

    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("스크린샷 저장.")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}대사 읽어주기 기능{/a} 토글.")

    hbox:
        label "Shift+A"
        text _("접근성 메뉴를 엽니다.")


screen mouse_help():

    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("휠 위로")
        text _("이전 대사로 롤백.")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("왼쪽 트리거\n왼쪽 어깨")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0
