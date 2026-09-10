init offset = -1

################################################################################
## 게임내 스크린
################################################################################


## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what, circle=None):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"

                hbox:
                    style "say_namebox_hbox"
                    text who id "who"
                    if circle is not None:
                        text circle id "circle" style "say_circle"

        text what id "what"


    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Character 객체를 통해 스타일을 지정할 수 있도록 namebox와 circle을 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('circle')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style say_namebox_hbox is default:
    spacing 12
    yalign 0.5

style say_circle is default:
    properties gui.text_properties("name", accent=False)
    size 30
    color "#84D4F9"
    outlines [ (1, "#29415A", 0, 0) ]
    yalign 0.6


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox_BA.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=False)
    xalign gui.name_xalign
    yalign 0.5

style ruby_text:
    size gui.text_size * 0.65
    yoffset - gui.text_size

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    ruby_style style.ruby_text
    ruby_line_leading gui.text_size // 2

    adjust_spacing False

style centered_text:
    outlines [ (5, "#000000", 0, 0) ]
    size 50
    line_spacing 30
    line_overlap_split -15
