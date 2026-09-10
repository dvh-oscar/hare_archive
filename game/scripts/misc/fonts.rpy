init offset = -2

################################################################################
## 경기천년체 (Gyeonggi Font Family) 설정
################################################################################

## 폰트 파일 경로 상수 정의
define font_gyeonggi_batang = "fonts/gyeonggi_batang_regular.ttf"
define font_gyeonggi_batang_bold = "fonts/gyeonggi_batang_bold.ttf"
define font_gyeonggi_title = "fonts/gyeonggi_title_medium.ttf"
define font_gyeonggi_title_light = "fonts/gyeonggi_title_light.ttf"
define font_gyeonggi_title_bold = "fonts/gyeonggi_title_bold.ttf"
define font_gyeonggi_title_v = "fonts/gyeonggi_title_v_bold.ttf"

init python:
    ## 1. 텍스트 태그용 폰트 별칭 (config.font_name_map)
    ## 사용 예시:
    ##   "{font=gyeonggi}기본 경기천년바탕 본문{/font}"
    ##   "{font=gyeonggi_title}경기천년제목 타이틀{/font}"
    ##   "{font=gyeonggi_title_bold}경기천년제목 볼드{/font}"
    ##   "{font=gyeonggi_title_v}경기천년제목 V볼드{/font}"
    config.font_name_map["gyeonggi"] = "fonts/gyeonggi_batang_regular.ttf"
    config.font_name_map["gyeonggi_batang"] = "fonts/gyeonggi_batang_regular.ttf"
    config.font_name_map["gyeonggi_batang_bold"] = "fonts/gyeonggi_batang_bold.ttf"
    config.font_name_map["gyeonggi_title"] = "fonts/gyeonggi_title_medium.ttf"
    config.font_name_map["gyeonggi_title_light"] = "fonts/gyeonggi_title_light.ttf"
    config.font_name_map["gyeonggi_title_bold"] = "fonts/gyeonggi_title_bold.ttf"
    config.font_name_map["gyeonggi_title_v"] = "fonts/gyeonggi_title_v_bold.ttf"

    ## 2. 굵은 글씨 / 스타일 대체 맵 (config.font_replacement_map)
    ## {b} 태그 사용 시 렌파이의 인조 볼드 대신 최적화된 실제 볼드 폰트 파일을 렌더링합니다.
    config.font_replacement_map["fonts/gyeonggi_batang_regular.ttf", True, False] = ("fonts/gyeonggi_batang_bold.ttf", False, False)
    config.font_replacement_map["fonts/gyeonggi_title_medium.ttf", True, False] = ("fonts/gyeonggi_title_bold.ttf", False, False)
    config.font_replacement_map["fonts/gyeonggi_title_light.ttf", True, False] = ("fonts/gyeonggi_title_bold.ttf", False, False)

    ## 별칭 태그에 대한 볼드 맵핑
    config.font_replacement_map["gyeonggi", True, False] = ("fonts/gyeonggi_batang_bold.ttf", False, False)
    config.font_replacement_map["gyeonggi_batang", True, False] = ("fonts/gyeonggi_batang_bold.ttf", False, False)
    config.font_replacement_map["gyeonggi_title", True, False] = ("fonts/gyeonggi_title_bold.ttf", False, False)
    config.font_replacement_map["gyeonggi_title_light", True, False] = ("fonts/gyeonggi_title_bold.ttf", False, False)
