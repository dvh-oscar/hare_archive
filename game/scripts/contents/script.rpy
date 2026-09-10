# 여기에서부터 게임이 시작합니다.
label start:

    ## miyo 캐릭터 스프라이트와 circle 기능 테스트
    show miyo at sprite_center

    miyo "안녕하세요, 선생님."


    miyo laugh "이 프로젝트는 hare_archive입니다."

    show miyo at sprite_pickup
    pause 0.60
    # show miyo happy at sprite_center
    miyo "circle 기능이 제대로 표시되나요?"
    show miyo at sprite_jump
    pause 0.60

    show miyo:
        xpos 0.5
        easein 0.3 xpos POS_LEFT
    show mari at sprite_right, inactive_say

    # show miyo smile at sprite_center
    miyo "감정 표현 테스트도 해볼까요?"
    "모브양" "귀여움" "냥냥냥냥야"

    return
