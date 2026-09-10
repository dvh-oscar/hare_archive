init offset = -1

################################################################################
## 통신 화면 (화상 통화 / 홀로그램 / 모니터 스캔라인 & 플리커) 시스템
################################################################################

init python:
    # 1. 커스텀 GLSL 셰이더 등록: serika.transmission
    renpy.register_shader("serika.transmission",
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;
            uniform float u_scanline_count;
            uniform float u_scanline_speed;
            uniform float u_scanline_intensity;
            uniform float u_bar_count;
            uniform float u_bar_speed;
            uniform float u_bar_intensity;
            uniform float u_flicker_speed;
            uniform float u_flicker_intensity;
            uniform float u_noise_intensity;
            uniform vec4 u_holo_tint;
            uniform float u_holo_amount;
            varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            float serika_trans_hash(vec2 p) {
                p = fract(p * vec2(123.34, 456.21));
                p += dot(p, p + 45.32);
                return fract(p.x * p.y);
            }
        """,
        fragment_300="""
            // 1. 이동하는 가로 스캔라인 (Horizontal Scanlines)
            float scan_wave = sin((v_tex_coord.y * u_scanline_count) - (u_time * u_scanline_speed));
            float scan_norm = (scan_wave + 1.0) * 0.5; // 0.0 ~ 1.0
            float scan_factor = 1.0 - (scan_norm * u_scanline_intensity);

            // 2. 굵은 이동 주사 빔 (Rolling Bar)
            float bar_wave = sin((v_tex_coord.y * u_bar_count) - (u_time * u_bar_speed));
            float bar_factor = smoothstep(0.4, 1.0, (bar_wave + 1.0) * 0.5) * u_bar_intensity;

            // 3. 플리커 현상 (Flicker - 다중 사인파 합성)
            float flicker_raw = (
                sin(u_time * u_flicker_speed * 13.7) * 0.45 +
                sin(u_time * u_flicker_speed * 31.3) * 0.35 +
                sin(u_time * u_flicker_speed * 67.9) * 0.20
            );
            float flicker_factor = 1.0 + (flicker_raw * u_flicker_intensity);

            // 4. 노이즈 스펙클 (Signal Noise)
            float noise_val = (serika_trans_hash(vec2(v_tex_coord.y * 50.0, floor(u_time * 24.0))) - 0.5) * 2.0;
            float noise_factor = noise_val * u_noise_intensity;

            // 총 밝기 계수 계산
            float total_brightness = max(0.0, (scan_factor + bar_factor) * flicker_factor + noise_factor);

            // 5. 색상 틴트 (Hologram / Green Screen / Tactical Monitor Tint)
            if (u_holo_amount > 0.001) {
                float lum = dot(gl_FragColor.rgb, vec3(0.299, 0.587, 0.114));
                vec3 tinted_mul = gl_FragColor.rgb * u_holo_tint.rgb;
                vec3 tinted_lum = vec3(lum) * u_holo_tint.rgb;
                vec3 tinted_color = mix(tinted_mul, tinted_lum, 0.35);
                gl_FragColor.rgb = mix(gl_FragColor.rgb, tinted_color, u_holo_amount);
            }

            // RGB 색상에 밝기 적용
            gl_FragColor.rgb *= total_brightness;

            // 6. 알파 플리커 (미세한 투명도 깜빡임)
            if (u_flicker_intensity > 0.001) {
                gl_FragColor.a *= clamp(1.0 + (flicker_raw * u_flicker_intensity * 0.5), 0.5, 1.2);
            }
        """
    )


################################################################################
## 통신 Transform 정의 및 프리셋
################################################################################

## 1. 범용 파라미터형 Transform (세부 수치 직접 조절 가능)
## 사용 예시:
##   show kei at sprite_center, comm_screen
##   show kei at sprite_right, comm_screen(scanline_speed=10.0, flicker_intensity=0.15)
transform comm_screen(
    scanline_count=160.0,
    scanline_speed=8.0,
    scanline_intensity=0.22,
    bar_count=1.5,
    bar_speed=2.5,
    bar_intensity=0.15,
    flicker_speed=6.0,
    flicker_intensity=0.07,
    noise_intensity=0.04,
    holo_tint=(0.75, 0.92, 1.0, 1.0),
    holo_amount=0.0,
    alpha=1.0
):
    shader "serika.transmission"
    u_scanline_count scanline_count
    u_scanline_speed scanline_speed
    u_scanline_intensity scanline_intensity
    u_bar_count bar_count
    u_bar_speed bar_speed
    u_bar_intensity bar_intensity
    u_flicker_speed flicker_speed
    u_flicker_intensity flicker_intensity
    u_noise_intensity noise_intensity
    u_holo_tint holo_tint
    u_holo_amount holo_amount
    alpha alpha


## 2. 기본 통신 플리커 (가로 줄무늬 이동 + 자연스러운 플리커, 원본 색감 100% 유지)
## 사용 예시:
##   show kei at sprite_center, comm_flicker
##   show kei at sprite_left, comm_flicker
transform comm_flicker:
    comm_screen(
        scanline_count=160.0,
        scanline_speed=8.0,
        scanline_intensity=0.22,
        bar_count=1.5,
        bar_speed=2.5,
        bar_intensity=0.15,
        flicker_speed=6.0,
        flicker_intensity=0.07,
        noise_intensity=0.03,
        holo_amount=0.0,
        alpha=1.0
    )


## 3. 녹색 통신 화면 (그린 모니터 / 전술 단말기 / CRT 그린 틴트)
## 전체적으로 약간 녹색 빛을 띄며 가로 줄무늬와 플리커가 적용됩니다.
## 사용 예시:
##   show kei at sprite_center, comm_green
##   show kei at sprite_left, comm_green
transform comm_green:
    comm_screen(
        scanline_count=170.0,
        scanline_speed=8.5,
        scanline_intensity=0.28,
        bar_count=1.5,
        bar_speed=2.5,
        bar_intensity=0.18,
        flicker_speed=6.5,
        flicker_intensity=0.08,
        noise_intensity=0.04,
        holo_tint=(0.50, 1.25, 0.65, 1.0),
        holo_amount=0.55,
        alpha=0.96
    )


## 4. 파란색 통신 화면 (블루 모니터 / 사이버네틱 디스플레이)
## 전체적으로 선명한 푸른빛(Blue Tint)을 띄며 가로 줄무늬와 플리커가 적용됩니다.
## 사용 예시:
##   show kei at sprite_center, comm_blue
transform comm_blue:
    comm_screen(
        scanline_count=170.0,
        scanline_speed=8.5,
        scanline_intensity=0.28,
        bar_count=1.5,
        bar_speed=2.5,
        bar_intensity=0.18,
        flicker_speed=6.5,
        flicker_intensity=0.08,
        noise_intensity=0.04,
        holo_tint=(0.50, 0.85, 1.30, 1.0),
        holo_amount=0.55,
        alpha=0.96
    )

transform comm_blue_inactive:
    comm_screen(
        scanline_count=170.0,
        scanline_speed=8.5,
        scanline_intensity=0.28,
        bar_count=1.5,
        bar_speed=2.5,
        bar_intensity=0.18,
        flicker_speed=6.5,
        flicker_intensity=0.08,
        noise_intensity=0.04,
        holo_tint=(0.00, 0.00, 0.25, 1.0),
        holo_amount=0.55,
        alpha=0.96
    )


## 4. SF 홀로그램 스타일 (사이버 블루 틴트 + 반투명 + 가로 줄무늬 + 플리커)
## 사용 예시:
##   show kei at sprite_center, comm_hologram
##   show kei at sprite_right, comm_hologram
transform comm_hologram:
    comm_screen(
        scanline_count=180.0,
        scanline_speed=10.0,
        scanline_intensity=0.30,
        bar_count=2.0,
        bar_speed=3.0,
        bar_intensity=0.22,
        flicker_speed=8.0,
        flicker_intensity=0.10,
        noise_intensity=0.05,
        holo_tint=(0.65, 0.90, 1.15, 1.0),
        holo_amount=0.35,
        alpha=0.88
    )


## 5. 수신 불량 노이즈 통신 (강한 플리커 + 빠른 줄무늬 + 신호 잡음)
## 사용 예시:
##   show kei at sprite_center, comm_bad_signal
transform comm_bad_signal:
    comm_screen(
        scanline_count=130.0,
        scanline_speed=16.0,
        scanline_intensity=0.40,
        bar_count=3.0,
        bar_speed=5.0,
        bar_intensity=0.35,
        flicker_speed=14.0,
        flicker_intensity=0.18,
        noise_intensity=0.12,
        holo_tint=(0.80, 0.95, 1.10, 1.0),
        holo_amount=0.15,
        alpha=0.90
    )


## 6. 은은하고 차분한 모니터 화면 (부드러운 줄무늬 + 최소화된 플리커)
## 사용 예시:
##   show kei at sprite_center, comm_subtle
transform comm_subtle:
    comm_screen(
        scanline_count=200.0,
        scanline_speed=5.0,
        scanline_intensity=0.15,
        bar_count=1.0,
        bar_speed=1.5,
        bar_intensity=0.08,
        flicker_speed=4.0,
        flicker_intensity=0.03,
        noise_intensity=0.01,
        holo_amount=0.0,
        alpha=1.0
    )


## 7. 통신 접속 / 종료 전환 연출
## 통신 시작할 때 번쩍이며 나타나는 연출
transform comm_in:
    alpha 0.0 yzoom 0.05 xzoom 1.2
    parallel:
        easein 0.15 alpha 1.0
    parallel:
        easein 0.20 yzoom 1.0 xzoom 1.0

## 통신 종료될 때 가로선으로 꺼지는 연출
transform comm_out:
    easein 0.15 yzoom 0.05 xzoom 1.2 alpha 0.8
    easeout 0.10 yzoom 0.0 xzoom 0.0 alpha 0.0
