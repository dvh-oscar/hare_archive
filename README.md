# 프로젝트 개요
> `하레` 는 블루아카이브의 등장인물인물입니다. 제가 하레를 정말 좋아하기 때문에 이 프로젝트의 이름으로 정했습니다.
## 목표
[Base](https://github.com/oryxel1/Base) 와 같이 블루아카이브의 스토리를 흉내내는 것을 목표로 합니다.
> 이 프로젝트의 일부 리소스는 Base로부터 가져왔습니다.
## 기술 스택
RenPy를 사용합니다.


## 유지보수
이 프로젝트는 개발자의 흥미에 의해 유지보수합니다.
개발자가 원하는 바에 따라 기능을 추가합니다.

## 기타 리소스
gitignore 처리한 사항은 사용자가 직접 리소스를 확보해야 합니다.
### 이미지
- `game/images/backgrounds` : 배경 일러스트
- `game/images/cg` : CG 일러스트
- `game/images/characters` : 스탠딩 일러스트
### 음향
- `game/audio/bgm` : 배경음악. `game/scripts/misc/bgm.rpy`에 배경음악의 목록이 정의되어 있습니다.

# 기능
## 스탠딩 일러스트 전처리
> 이 기능을 사용하려면 Python이 설치되어 있어야 합니다.
1. 전처리가 필요한 스탠딩 일러스트를 `BaSpines/{id}/{id}_default_{number}.png` 에 준비하십시오
2. `tools/workdir/config.json` 속성을 추가하십시오.
    ```json
    {
        // 속성명은 {id} 롸 동일해야 함
        "NP0036": {
            "id": "millemob", // 이 명칭은 캐릭터 일러스트 접두사로 사용됨
            "dx": 50,
            "dy": 800
        }
    }
    ```
3. `run_tool.bat` 혹은 `run_tool.sh` 를 실행하십시오.
4. `tools/grid/{id}`에 생성된 일러스트를 확인하십시오. 적색 가로선과 세로선의 교점이 의도한 위치에 있는지 확인하십시오. 이 프로젝트에 정의한 각종 Transform 이 해당 위치를 중심으로 확대 혹은 축소를 수행합니다. 필요에 따라 `dx` 혹은 `dy` 의 값을 조정하십시오.
5. `game/images/characters/{id}`에 생성된 파일을 확인하십시오.

# 스크립트
> 사용자는 `game/` 내의 적당히 rpy 파일을 작성하 `start` 라벨을 작성하여야 합니다.
## 예제
`sprite_left`, `sprite_center`, `sprite_right`과 `DEFAULT_ZOOM` 을 이용하면 화면에 최대 3인의 캐릭터를 자연스럽게 배치할 수 있습니다.
해당 Transform은 스탠딩 일러스트의 가로축상 중앙, 세로축상 위와 아래를 1:3 으로 내분하는 지점을 anchor로 하고 있습니다. (위에 서술한 스탠딩 일러스트 전처리 내용을 확인하십시오)

```renpy
define millemob = Character("밀레니엄 모브 쨩", image = "millemob", circle = "귀여움")
define highlander = Character("하이랜더 모브 쨩", image = "landermob", circle = 
"커여움")
define trimob = Character("티파티 모브 양", image = "teaparty", circle = "아름다움")

label example:
    show millemob at sprite_center:
        zoom DEFAULT_ZOOM #DEFAULT_ZOOM 을 명시해야 크기가 알맞게 표시됩니다.
    show highlander at sprite_right:
        matrixcolor TintMatrix("#888888") # inactive_say 의 TintMatrix 값
        zoom DEFAULT_ZOOM
    with dissolve

    pause 1.0
    millemob "나는 밀레니엄 공순이!"

    show millemob at inactive_say
    show highlander at active_say
    highlander "나는 하이랜더의 승무원!"

    show highlander at inactive_say
    show trimob at sprite_left, comm_blue: # 통신 플리커링 등 묘사
        zoom DEFAULT_ZOOM
    
    pause 0.2
    trimob "저는 티파티의 임원입니다."

    show trimob at comm_blue_inactive
    play sound sfx_steam
    show highlander at sprite_jump, active_say # active_say, inactive_say, comm_blue, comm_blue_inactive 는 마지막에 사용해야 잘 작동하는 경향이 있음
    pause 1.0
    show highlander at inactive_say
    show millemob at sprite_pickup, active_say
    millemob "뭘 그리 방방 뛰고 그럽니까?"
    

    
    


```
