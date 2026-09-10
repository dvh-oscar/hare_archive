init offset = -1

## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

## 선택지 버튼 호버 및 클릭(소멸) 애니메이션 Transform
transform choice_button_tf:
    transform_anchor True
    on hover:
        easein 0.15 zoom 1.03
    on idle:
        easeout 0.15 zoom 1.00
    on selected_hover:
        easein 0.15 zoom 1.03
    on selected_idle:
        easeout 0.15 zoom 1.00
    on hide:
        ## 클릭 직후: 효과음 재생 중 버튼이 탄력 있게 확대 피드백 (불투명 상태 유지)
        easein 0.12 zoom 1.06
        ## 이후 부드럽게 추가 확대되며 자연스럽게 페이드아웃 소멸
        parallel:
            easeout 0.78 zoom 1.10
        parallel:
            easeout 0.78 alpha 0.0


screen choice(items):
    style_prefix "choice"
    zorder 100

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
                at choice_button_tf


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Frame("gui/button/dialogue_button.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    hover_background Frame("gui/button/dialogue_button.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    activate_sound audio.click_sound
    xalign 0.5
    xsize gui.choice_button_width
    ysize gui.choice_button_height

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    xalign 0.5
    yalign 0.5
