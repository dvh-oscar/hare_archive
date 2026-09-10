init offset = -1

################################################################################
## 캐릭터 스탠딩/스프라이트 Transform 정의
################################################################################

define POS_LEFT = 0.25
define POS_CENTER = 0.50
define POS_RIGHT = 0.75
define DEFAULT_ZOOM = 0.675


transform active_say:
    # xoffset 0
    matrixcolor TintMatrix("#888888")
    linear 0.2 matrixcolor TintMatrix("#FFFFFF")

transform inactive_say:
    # xoffset 0
    matrixcolor TintMatrix("#FFFFFF")
    linear 0.2 matrixcolor TintMatrix("#888888")

transform sprite_center:
    # zoom DEFAULT_ZOOM
    anchor (0.5, 0.5)
    pos (POS_CENTER, 0.425)

transform sprite_right:
    # zoom DEFAULT_ZOOM
    anchor (0.5, 0.5)
    pos (POS_RIGHT, 0.425)

transform sprite_left:
    # zoom DEFAULT_ZOOM
    anchor (0.5, 0.5)
    pos (POS_LEFT, 0.425)

transform sprite_jump:
    yoffset 0
    easein 0.12 yoffset -50
    easeout 0.15 yoffset 0
    easein 0.12 yoffset -50
    easeout 0.15 yoffset 0
    # easein 0.10 yoffset -50
    # easeout 0.10 yoffset 0


transform sprite_pickup:
    yoffset 0
    easein 0.18 yoffset 60
    pause 0.20
    easein 0.18 yoffset 0

define inactive_color_matrix = ContrastMatrix(0.75) * BrightnessMatrix(-0.4)

## 1. 기본 크기 조절 Transform
## Ren'Py의 기본 위치(center, left, right, truecenter 등)와 함께 조합하여 사용할 수 있습니다.
## 사용 예시:
##   show kei at sprite_zoom(0.48), center
##   show kei at sprite_zoom(0.5), left
# transform sprite_zoom(z=0.5):
#     zoom z

# ## 2. 위치 및 크기 통합 Transform (파라미터 직접 지정)
# ## x: 가로 위치 (0.0: 왼쪽, 0.5: 중앙, 1.0: 오른쪽)
# ## y: 세로 정렬 (1.0: 하단 기준, 0.0: 상단 기준)
# ## z: 확대/축소 배율 (기본값: 0.5)
# ## 사용 예시:
# ##   show kei at sprite_pos(0.45, 0.5, 1.0)
# ##   show kei at sprite_pos(z=0.45, x=0.3, y=1.0, yoffset=20)
# transform sprite_pos(z=0.5, x=0.5, y=1.0, xoffset=0, yoffset=0):
#     zoom z
#     xalign x
#     yalign y
#     xoffset xoffset
#     yoffset yoffset

# ## 3. 대표 위치 프리셋 Transform (크기 조정 가능)
# ## 기본 크기는 0.5이며, 괄호 안에 원하는 배율(예: 0.45)을 전달하여 크기를 바꿀 수 있습니다.
# ## 사용 예시:
# ##   show kei at sprite_center
# ##   show kei at sprite_center(0.45)
# ##   show kei at sprite_left
# ##   show kei at sprite_right(0.5)
# transform sprite_center(z=0.5, y=1.0):
#     zoom z
#     xalign 0.5
#     yalign y

# transform sprite_left(z=0.5, y=1.0):
#     zoom z
#     xalign 0.2
#     yalign y

# transform sprite_right(z=0.5, y=1.0):
#     zoom z
#     xalign 0.8
#     yalign y

# transform sprite_far_left(z=0.5, y=1.0):
#     zoom z
#     xalign 0.05
#     yalign y

# transform sprite_far_right(z=0.5, y=1.0):
#     zoom z
#     xalign 0.95
#     yalign y

# ## 4. 연출용 샷 거리 프리셋 (전신, 미디엄, 바스트, 클로즈업)
# ## 고해상도(2170px 높이 등) 일러스트에 맞춘 거리별 샷 프리셋입니다.
# ## 사용 예시:
# ##   show kei at sprite_full
# ##   show kei at sprite_mid
# ##   show kei at sprite_close
# transform sprite_full(x=0.5):
#     zoom 0.45
#     xalign x
#     yalign 1.0

# transform sprite_mid(x=0.5):
#     zoom 0.65
#     xalign x
#     yalign 0.95

# transform sprite_bust(x=0.5):
#     zoom 0.85
#     xalign x
#     yalign 0.85

# transform sprite_close(x=0.5):
#     zoom 1.1
#     xalign x
#     yalign 0.6

# ## 5. 부드러운 위치 이동 Transform
# ## 사용 예시:
# ##   show kei at sprite_move(x_from=0.2, x_to=0.5, z=0.5, duration=0.4)
# transform sprite_move(x_from=0.2, x_to=0.5, z=0.5, y=1.0, duration=0.4):
#     zoom z
#     yalign y
#     xalign x_from
#     easein duration xalign x_to

################################################################################
## 화면 통신 / 홀로그램 / 스캔라인 플리커 Transform (transmission_shader.rpy 연동)
################################################################################
## 셰이더 기반으로 실시간 가로 줄무늬 이동, 롤링 빔, 플리커 깜빡임 효과를 제공합니다.
##
## [사용 가능한 프리셋]
##   - comm_flicker     : 기본 통신 화면 (가로 줄무늬 + 자연스러운 플리커, 원본 색상)
##   - comm_green       : 녹색 통신 화면 (그린 모니터 / CRT 녹색 틴트 + 줄무늬 + 플리커)
##   - comm_blue        : 파란색 통신 화면 (블루 모니터 / 사이버네틱 디스플레이 + 줄무늬 + 플리커)
##   - comm_hologram    : SF 홀로그램 (사이버 블루 틴트 + 반투명 + 줄무늬 + 플리커)
##   - comm_bad_signal  : 수신 불량 (강한 플리커 + 빠른 줄무늬 + 신호 노이즈)
##   - comm_subtle      : 은은하고 차분한 모니터 화면
##   - comm_screen(...) : 세부 수치(scanline_speed, flicker_intensity 등) 직접 커스텀
##   - comm_in / comm_out : 통신 시작(켜짐) / 통신 종료(꺼짐) 트랜스폼
##
## [사용 예시]
##   show kei at sprite_center, comm_flicker
##   show kei at sprite_center, comm_green
##   show kei at sprite_center, comm_blue
##   show kei at sprite_right, comm_hologram
##   show kei at sprite_left, comm_bad_signal
##   show kei at sprite_center, comm_screen(scanline_speed=8.0, flicker_intensity=0.15)

