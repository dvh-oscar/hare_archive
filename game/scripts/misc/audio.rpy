init offset = -1

################################################################################
## 오디오 채널 등록 (Audio Channel Registration)
################################################################################

## 환경음 (Ambient) 채널 등록
## music 채널과 동일하게 기본적으로 loop 합니다.
## 사용 예시:
##   play ambient amb_rain fadein 1.0
##   stop ambient fadeout 1.0
init python:
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)

################################################################################
## 오디오 (Audio / BGM / SFX) 정의
################################################################################

## 1. 배경음악 (Music / BGM)
## `define audio.<변수명> = "<경로>"` 형태로 정의하면 스크립트에서
## `play music <변수명>` 또는 `play music audio.<변수명>` 형태로 바로 재생할 수 있습니다.
##
## 배경음악은 추후 프로젝트에 맞는 곡을 추가하세요.
## 예시:
##   define audio.bgm_main = "audio/music/main_theme.mp3"


## 2. 환경음 (Ambient Sounds)
## ambient 채널은 기본적으로 loop 됩니다.
## 사용 예시:
##   play ambient amb_train fadein 1.0
##   stop ambient fadeout 1.0

define audio.ambient_train = "audio/ambient/ambient_train.mp3"


## 3. 일반 효과음 (Sound Effects)
define audio.sound_door_open = "audio/sound/sound_door_open.mp3"
define audio.sound_call_beep = "audio/sound/call_beep.mp3"
define audio.sound_call_beep_connected = "audio/sound/call_beep_connected.mp3"

## 4. UI 효과음
define audio.click_sound = "audio/sfx/click_sound.mp3"


## 5. 이모티콘 모션 효과음 (Emoticon Motion SFX)
## 사용 예시:
##   play sound sfx_emoticon_angry
##   play sound sfx_surprise
##   play sound sfx_emoticon_heart

define audio.sfx_emoticon_angry = "audio/sfx/emoticon/sfx_emoticon_angry.wav"
define audio.sfx_emoticon_bulb = "audio/sfx/emoticon/sfx_emoticon_bulb.wav"
define audio.sfx_emoticon_chat = "audio/sfx/emoticon/sfx_emoticon_chat.wav"
define audio.sfx_emoticon_dot = "audio/sfx/emoticon/sfx_emoticon_dot.wav"
define audio.sfx_emoticon_exclaim = "audio/sfx/emoticon/sfx_emoticon_exclaim.wav"
define audio.sfx_emoticon_heart = "audio/sfx/emoticon/sfx_emoticon_heart.wav"
define audio.sfx_emoticon_question = "audio/sfx/emoticon/sfx_emoticon_question.wav"
define audio.sfx_emoticon_respond = "audio/sfx/emoticon/sfx_emoticon_respond.wav"
define audio.sfx_emoticon_sad = "audio/sfx/emoticon/sfx_emoticon_sad.wav"
define audio.sfx_emoticon_shy = "audio/sfx/emoticon/sfx_emoticon_shy.wav"
define audio.sfx_emoticon_sigh = "audio/sfx/emoticon/sfx_emoticon_sigh.wav"
define audio.sfx_emoticon_steam = "audio/sfx/emoticon/sfx_emoticon_steam.wav"
define audio.sfx_emoticon_surprise = "audio/sfx/emoticon/sfx_emoticon_surprise.wav"
define audio.sfx_emoticon_sweat = "audio/sfx/emoticon/sfx_emoticon_sweat.wav"
define audio.sfx_emoticon_tear = "audio/sfx/emoticon/sfx_emoticon_tear.wav"
define audio.sfx_emoticon_think = "audio/sfx/emoticon/sfx_emoticon_think.wav"
define audio.sfx_emoticon_twinkle = "audio/sfx/emoticon/sfx_emoticon_twinkle.wav"
define audio.sfx_emoticon_upset = "audio/sfx/emoticon/sfx_emoticon_upset.wav"
define audio.sfx_emoticon_zzz = "audio/sfx/emoticon/sfx_emoticon_zzz.wav"

## 간편 별칭 (Aliases)
define audio.sfx_angry = "audio/sfx/emoticon/sfx_emoticon_angry.wav"
define audio.sfx_bulb = "audio/sfx/emoticon/sfx_emoticon_bulb.wav"
define audio.sfx_chat = "audio/sfx/emoticon/sfx_emoticon_chat.wav"
define audio.sfx_dot = "audio/sfx/emoticon/sfx_emoticon_dot.wav"
define audio.sfx_exclaim = "audio/sfx/emoticon/sfx_emoticon_exclaim.wav"
define audio.sfx_heart = "audio/sfx/emoticon/sfx_emoticon_heart.wav"
define audio.sfx_question = "audio/sfx/emoticon/sfx_emoticon_question.wav"
define audio.sfx_respond = "audio/sfx/emoticon/sfx_emoticon_respond.wav"
define audio.sfx_sad = "audio/sfx/emoticon/sfx_emoticon_sad.wav"
define audio.sfx_shy = "audio/sfx/emoticon/sfx_emoticon_shy.wav"
define audio.sfx_sigh = "audio/sfx/emoticon/sfx_emoticon_sigh.wav"
define audio.sfx_steam = "audio/sfx/emoticon/sfx_emoticon_steam.wav"
define audio.sfx_surprise = "audio/sfx/emoticon/sfx_emoticon_surprise.wav"
define audio.sfx_sweat = "audio/sfx/emoticon/sfx_emoticon_sweat.wav"
define audio.sfx_tear = "audio/sfx/emoticon/sfx_emoticon_tear.wav"
define audio.sfx_think = "audio/sfx/emoticon/sfx_emoticon_think.wav"
define audio.sfx_twinkle = "audio/sfx/emoticon/sfx_emoticon_twinkle.wav"
define audio.sfx_upset = "audio/sfx/emoticon/sfx_emoticon_upset.wav"
define audio.sfx_zzz = "audio/sfx/emoticon/sfx_emoticon_zzz.wav"
