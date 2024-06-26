# 콩닥콩닥

## 대학생활을 기억하는 방식을 바꾸다.

![readme_mockup2](./images/intro3.png)

<br>

## 프로젝트 소개

- 콩닥콩닥은 시간이 흐르면 그리워질 우리의 학창시절,입학부터 졸업까지 당신의 설렘을 간직해드립니다.
- 콩닥콩닥은 캠퍼스 건물 별로 나만의 일기를 기록할 수 있는 서비스입니다.
- 일기를 기록하고, 해시태그 기능과 랭킹 시스템을 통해 다른 사람들과 교류할 수 있습니다.
- 날씨 기능, 디데이, 업로드 수에 따라 달라지는 코끼리 이미지 등 소소한 디테일을 살려 서비스 이용에 재미를 더했습니다.

<br>

## 팀원 구성

<div align="center">

| ![zoey003](https://github.com/zoey003.png) | ![sayyyho](https://github.com/sayyyho.png) | ![chaem03](https://github.com/chaem03.png) | ![pyeree](https://github.com/pyeree.png) | ![onlynyang](https://github.com/onlynyang.png) |
| :----------------------------------------: | :----------------------------------------: | :----------------------------------------: | :--------------------------------------: | :--------------------------------------------: |
|    [김지현](https://github.com/zoey003)    |    [박세호](https://github.com/sayyyho)    |    [하채민](https://github.com/chaem03)    |   [임현우](https://github.com/pyeree)    |     [한지은](https://github.com/onlynyang)     |
|                기획/디자인                 |                 프론트엔드                 |                 프론트엔드                 |                  백엔드                  |                     백엔드                     |

</div>

<br>

## ✏️ 사용방법

## 🍎 Mac

### python 3.11 버전 설치

```SSH
https://www.python.org/ 에서 3.11 버전을 설치해주세요.
```

### python virtualenv를 이용한 가상환경 정의

```SSH
# 프로젝트를 생성하려는 폴더경로에서 git bash를 열고..
python3.11 -m venv venv
```

---

### 가상환경 실행 및 장고 설치

```SSH
source venv/bin/activate

# 최초 1회만
pip install django
```

---

### 프로젝트 실행

```SSH
# manage.py 포함된 경로에서
# Model을 건들이지 않았다면, 최초 1회만 실행
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

---

## 💻 Windows

### python virtualenv를 이용한 가상환경 정의

```SSH
# 프로젝트를 생성하려는 폴더경로에서 git bash를 열고..
pip install virtualenv
virtualenv venv --python=3.11
```

---

### 가상환경 실행 및 장고설치

```SSH
source venv/Scripts/activate

# 최초 1회만
pip install django
```

---

### 프로젝트 실행

```SSH
# manage.py 포함된 경로에서
# Model을 건들이지 않았다면, 최초 1회만 실행
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

## 1. 개발 환경

- PD : Figma ( [디자인 보러가기 ](https://www.figma.com/design/QoYerRSNVn6RwYx7aWuvUT/%EC%BD%A9%EB%8B%A5%EC%BD%A9%EB%8B%A5?node-id=2594-2732&t=dzkaXg1aOwc6rUh5-1))
- Frontend : HTML, CSS, JavaScript
- Backend : Python, Django
- 버전 및 이슈관리 : Github, Github Issues
- 협업 툴 : Discord, Notion

<br>

## 2. 협업 전략

### Git-flow 전략

- Git-flow 전략을 기반으로 main, develop 브랜치와 feature 보조 브랜치를 운용했습니다.
- main, develop, Feat 브랜치로 나누어 개발을 하였습니다. - **main** 브랜치는 무결성 검증 이후 단계에서만 사용하는 브랜치입니다. - **develop** 브랜치는 개발 단계에서 git-flow의 master 역할을 하는 브랜치입니다. - **Feat** 브랜치는 기능 단위로 독립적인 개발 환경을 위하여 사용하고 merge 후 각 브랜치를 삭제해주었습니다.

## GitHub Role

- 사용자는 먼저 Upstream Repository를 자신의 GitHub 계정으로 포크(fork)하고, 이 포크(fork)된 Origin Repository를 로컬 컴퓨터로 **Clone**하여 작업합니다.

- 그 후 개발한 변경 사항을 Origin Repository로 **Push**합니다. 이후 Upstream Repository로 풀 **PR**를 보내 변경 사항을 제안합니다.

- PR이 완료 된 후 Upstream Repository의 최신 변경 사항을 가져오기 위해 Local에서 풀(pull)을 사용합니다.

### 개발을 시작할 때

1. 개발을 시작할 때는 Upstream Repository에서 Issue를 생성합니다.
2. 이후 Issue에서 Origin Repository의 Dev Branch에서 새로운 Branch를 생성합니다
   - 이때 브랜치 이름은 다음을 따릅니다.
   - **새로운 기능 개발 : feature/#[Issue의 번호]**
   - **버그 픽스 : fix/#[Issue의 번호]**
   - **기능 리팩토링 : refactor/#[Issue의 번호]**
3. Loacl에서 Fetch를 통해 만든 New Branch(feature or fix or refactor)을 들고옵니다.
4. 해당 Branch로 checkout 이후 기능 개발을 진행합니다.

### 개발을 종료할 때

1. 기능 개발이 종료되면 Origin Repository의 Branch(feature or fix or refactor)로 변경 사항을 Push 합니다.
2. Origin Repository에서 Upstream Repository로 PR을 보냅니다.
3. Code Review 이후 마지막으로 Approve한 사람은 **Squash And Merge**를 합니다.
4. PR이 **Squash And Merge**되면 Local에서는 dev Branch로 checkout합니다.
5. Local에서 Upstream Repository의 dev Branch를 pull 받습니다.
6. 마지막으로 Origin Repository의 dev Branch를 Update하기 위해 Push를 해줍니다.

### Main Branch가 갱신될 때

1. 만약 Release Version을 낼 때는 Upstream의 dev Branch에서 main Branch로 PR을 날립니다.
2. 해당 Repository의 모든 사용자가 Code를 재확인한 후 Merge를 합니다.

## Commit & PR Convention

| Commit Type | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| Feat        | 기능 개발                                                      |
| Fix         | 버그 수정                                                      |
| Docs        | 문서 수정                                                      |
| Style       | 코드 formatting, 세미콜론 누락 등 코드 자체의 변경이 없는 경우 |
| Refactor    | 코드 리팩토링                                                  |
| Chore       | package manager 수정 등                                        |
| Design      | CSS 등 사용자 UI 변경                                          |

  <br>

## 3. 프로젝트 구조

```
├── README.md
├── LICENSE
├── .gitignore
├── project
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── manage.py
│   ├── Pipfile
│   ├── project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── static
│   │   │   ├── assets
│   │   │   │   ├── font
│   │   │   │   │   ├── Sagak-sagak.ttf
│   │   │   │   │   ├── Human-beomseok.ttf
│   │   │   │   ├── images
│   │   │   │   │   ├── a_screen.svg
│   │   │   │   │   ├── arrow.svg
│   │   │   │   │   ├── b_screen.svg
│   │   │   │   │   ├── ...
│   │   │   ├── css
│   │   │   │   ├── base
│   │   │   │   │   ├── index.css
│   │   │   │   │   ├── reset.css
│   │   │   │   ├── shared
│   │   │   │   │   ├── topnav.css
│   │   │   │   ├── all_posts.css
│   │   │   │   ├── category_a.css
│   │   │   │   ├── category_b.css
│   │   │   │   ├── category_c.css
│   │   │   │   ├── categorypage.css
│   │   │   │   ├── create_post.css
│   │   │   │   ├── edit.css
│   │   │   │   ├── login.css
│   │   │   │   ├── main.css
│   │   │   │   ├── post_detail.css
│   │   │   │   ├── search.css
│   │   │   │   ├── signup_done.css
│   │   │   │   ├── signup.css
│   │   │   ├── js
│   │   │   │   ├── allPost.js
│   │   │   │   ├── backControl.js
│   │   │   │   ├── category.js
│   │   │   │   ├── createPost.js
│   │   │   │   ├── editPost.js
│   │   │   │   ├── login.js
│   │   │   │   ├── main.js
│   │   │   │   ├── placeFrame.js
│   │   │   │   ├── postDetail.js
│   │   │   │   ├── search.js
│   │   │   │   ├── signup.js
│   │   │   │   ├── topnav.js
│   │   │   │   ├── weather.js
│   │   ├── templates
│   │   │   ├── shared
│   │   │   │   ├── _topnav.html
│   │   │   ├── base.html
│   └── main
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── utils.py
│       ├── views.py
│       ├── templates
│       │   ├── all_posts.html
│       │   ├── cateogrypage.html
│       │   ├── create_post.html
│       │   ├── edit_post.html
│       │   ├── firstpage.html
│       │   ├── mainpage.html
│       │   ├── post_detail.html
│       │   ├── search.html
│       │   ├── secondpage_a.html
│       │   ├── secondpage_b.html
│       │   ├── secondpage_c.html
│       │   ├── signup_done.html
│       │   ├── signup.html

```

<br>

## 4. 신경 쓴 부분
-  협업 방식 
-  최고의 순간 하트 구현
-  페이지 간 경로 


## 5. 페이지별 기능

### [초기화면]
   - 회원가입과 로그인을 할 수 있는 초기 화면 입니다.
   - 디자인
      - 로고 :심작 박동 수와 동국대학교의 명진관&남산타워를 조합해 콩닥콩닥만의 로고를 표현하였습니다.
      - 스타일 : 일기 작성을 컨셉으로 스케치북의 로그인 화면을 표현하였습니다.

<br>

### [회원가입]
   - 아이디를 입력한 후 중복확인 버튼을 누르면 유효성 검사가 진행되고 통과하지 못한 경우 경고 문구가 입력창 하단에 표시됩니다. 
   - 비밀번호는 영문 / 숫자 포함 8글자 이상 입력해야하며, 비밀번호 확인란으로 유효성 검사를 합니다. 비밀번호가 일치하지 않거나, 영문 / 숫자 포함 8글자 이상이 아닐 시 각 입력창이 빨간색으로 표현되고 하단에 경고 문구가 표현됩니다.
   - 이름을 입력 받습니다.
   - 학번은 10자리로 입력해야하며 조건을 충족하지 않을 시 입력창 하단에 경고 문구가 표현됩니다.


### [로그인]
   -  아이디와 비밀번호를 입력 받습니다. 로그인 버튼을 통해 유효성 검사를 실시하며, 유효하지 않은 아이디/비밀번호일 경우 입력창이 빨간색으로 표현되고 하단에 경고 문구가 표현됩니다.

### [로그아웃]
   - 메인페이지 최 하단에 로그아웃 버튼을 통해 로그아웃 할 수 있습니다.
   - 로그아웃 버튼을 누르면 확인 메세지를 통해 사용자의 로그아웃 의사를 재 확인합니다.

### [메인페이지]
0. 상단 nav-bar
   - "00일째 콩닥콩닥 "가입한 날짜로부터 경과한 날이 표현됩니다.
   -  현재 날짜와 오늘의 날씨가 실시간으로 연동됩니다.
     
1. 학교 맵
   - 실제 학교를 구조를 표현했으며 ,a, b, c 구역으로 나눠져  있으며 맵 하단에 건물들이 분류 되어 있습니다.
   - a, b, c 버튼을 통해 해당 구역 맵으로 이동할 수 있습니다. 사용자는 해당 구역의 건물을 선택해 건물별로 글을 남길 수 있습니다.
     
2. 해시태그 검색
   - 해시태그 검색 페이지로 이동할 수 있습니다.
     
3. 주간랭킹
   - 월요일 부터 일요일까지 1주일을 기준으로 주간 랭킹이 표현됩니다. 랭킹을 통해 사용자의 참여를 유도할 수 있습니다.
     
4. 내 정보
   - 회원가입 시 입력 했던 정보를 바탕으로 학번, 이름이 표현되고, 회원 가입일을 입학 날로 표현 됩니다. 추가로 사용자가 작성한 글의 개수를 표현합니다.
   - 사용자가 작성한 글 개수를 기준으로 개수별 코끼리 이미지가 변합니다.

5. 최고의 순간들
   - 모아보기 페이지에서 하트 버튼을 통해 사용자가 최고의 순간으로 지정한 글들을 개수 제한 없이 표현해줍니다
   - 글을 작성한 날짜와 제목, 건물이 표현 되며, 건물별 프레임은 a,b,c 구간 별로 다른 색으로 표현됩니다.
     
6. 모아보기
   - 사용자가 작성한 모든글을 한눈에 볼 수 있는 모아보기 페이지로 이동합니다.

### [Top-nav]
   - 뒤로가기 버튼을 통해 이전 페이지로 이동합니다.
   - 홈 버튼을 통해 메인페이지로 이동합니다.

### [구역 a,b,c  맵]
   - 메인페이지의 a,b,c 버튼을 통해 해당 구역 맵으로 이동합니다.
   - 사용자는 글을 남기고 싶은 건물을 선택해 해당 건물 페이지로 이동할 수 있습니다.

### [건물별 일기장]
1. 누적글 코끼리 순위
   - 해당 건물에서 글을 많이 작성한 사용자 순으로 1위~3위까지 사용자 아이디와 게이징 바,작성한 글 개수로 표현됩니다.
     
2. 나의 글 목록
   - 실선 기준 상단에 사용자가 작성한 글 개수가 표현됩니다
   - 실선 기준 하단에 사용자가 작성한 글의 목록이 표현됩니다. 글은 작성한 날짜와 글의 제목 그날의 날씨가 표현됩니다.
   - 글을 선택하면 글을 수정 삭제할 수 있는 상세 페이지로 이동합니다.
   - 페이지 하단의 새로운 '추억 남기기' 버튼을 통해 건물에서 새 글을 작성할 수 있습니다.

### [글 작성]
   - 현재 날짜와 현재의 날씨가 반영되며 사용자는 제목과 내용 해시태그를 입력할 수 있습니다.
   - 제목과 내용은 필수 입력이며 태그는 필수 입력이 아닙니다.
   - 제목은 8글자로 제한되며, 내용은 제한이 없습니다. 태그는 #을 붙이지 않고 작성후 엔터를 누르면 자동으로 # 붙습니다.
   - 유효성 검사 후 글 작성이 유효할 시 저장 버튼이 회색에서 주황색으로 활성화 됩니다.
   - 해시태그를 통해 사용자간의 상호작용을 유도하였습니다.

### [해시태그 검색]
   - 상단의 검색란에 글작성 페이지와 마찬가지로 원하는 해시태그 검색어를 입력후 엔터를 누르면 #이 붙습니다.
   - 입력 후 돋보기 버튼을 통해 검색을 할 수 있습니다
   - 검색 결과로는 해당 해시태그가 포함된 전체 사용자의 글이 최신순으로 업로드 됩니다.
   - 해당 해시태그가 포함된 전체 사용자의 글 내용을 볼 수 있습니다.
   - 해시태그 검색 결과가 없을 경우 '검색결과가 없습니다'로 표현됩니다.


### [글 상세 페이지]
1. 수정
   - 연필 버튼을 통해 글을 수정할 수 있습니다. 
2. 삭제
   - 휴지통 버튼을 통해 글을 삭제할 수 있습니다.
   - 로그아웃 버튼과 마찬가지로 사용자의 삭제 의사를 메시지를 통해 재 확인합니다.
  
### [모아보기]
- 사용자가 작성한 모든 글을 한눈에 볼 수 있으며, 날짜별 필터링 그리고 최고의 순간을 지정할 수 있습니다.
1. 기간 별 필터링 기능
   - 0000년, 00월 , 00일 ~ 0000년, 00월 , 00일 로 글을 필터링 합니다.
   - 기간을 지정 후 돋보기 버튼을 통해 필터링을 할 수 있습니다.
   - Reset 버튼을 통해 필터링을 초기화 할 수 있습니다.
2. 최고의 순간들 지정
   - 하트 버튼을 통해 최고의 순간들을 지정합니다.
   - 최고의 순간의 글은 메인페이지 '최고의 순간들' 확인 할 수 있습니다.

## 4. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2024-06-16 ~ 2024-06-26

<br>

### 작업 관리

- GitHub Issues를 사용하여 진행 상황을 공유했습니다.
- 매일 스크럼 회의를 진행하며 작업 순서와 방향성에 대한 고민을 나누고 노션에 회의 내용을 기록했습니다.

<br>

<!-- ## 7. 페이지별 기능

### [초기화면]

- 서비스 접속 초기화면으로 splash 화면이 잠시 나온 뒤 다음 페이지가 나타납니다.
  - 로그인이 되어 있지 않은 경우 : SNS 로그인 페이지
  - 로그인이 되어 있는 경우 : README 홈 화면
- SNS(카카오톡, 구글, 페이스북) 로그인 기능은 구현되어 있지 않습니다.

| 초기화면                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------- |
| ![splash](https://user-images.githubusercontent.com/112460466/210172920-aef402ed-5aef-4d4a-94b9-2b7147fd8389.gif) |

<br>

### [회원가입]

- 이메일 주소와 비밀번호를 입력하면 입력창에서 바로 유효성 검사가 진행되고 통과하지 못한 경우 각 경고 문구가 입력창 하단에 표시됩니다.
- 이메일 주소의 형식이 유효하지 않거나 이미 가입된 이메일일 경우 또는 비밀번호가 6자 미만일 경우에는 각 입력창 하단에 경구 문구가 나타납니다.
- 작성이 완료된 후, 유효성 검사가 통과된 경우 다음 버튼이 활성화되며, 버튼을 클릭하면 프로필 설정 화면이 나타납니다.

| 회원가입                                                                                                        |
| --------------------------------------------------------------------------------------------------------------- |
| ![join](https://user-images.githubusercontent.com/112460466/210173571-490f5beb-5791-4a4a-8c5e-510cdcb5f1fe.gif) |

<br>

### [프로필 설정]

- 회원가입 페이지의 유효성 검사를 통과해야 진입할 수 있습니다.
- 프로필 설정에 필요한 프로필 사진, 사용자 이름, 계정 ID, 소개를 입력받습니다.
- 사용자 이름과 계정 ID는 필수 입력사항입니다.
- 계정 ID에는 형식 및 중복 검사가 진행됩니다.
- 프로필 사진은 등록하지 않을 경우 기본 이미지가 등록됩니다.

| 프로필 설정                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- |
| ![setProfile](https://user-images.githubusercontent.com/112460466/210173749-2da6c9af-eb93-4eea-9663-1a03e19299ec.gif) |

<br>

### [로그인]

- 이메일 주소와 비밀번호를 입력하면 입력창에서 바로 유효성 검사가 진행되고 통과하지 못한 경우 각 경고 문구가 입력창 하단에 표시됩니다.
- 이메일 주소의 형식이 유효하지 않거나 비밀번호가 6자 미만일 경우에는 각 입력창 하단에 경구 문구가 나타납니다.
- 작성이 완료된 후, 유효성 검사가 통과된 경우 로그인 버튼이 활성화됩니다.
- 로그인 버튼 클릭 시 이메일 주소 또는 비밀번호가 일치하지 않을 경우에는 경고 문구가 나타나며, 로그인에 성공하면 홈 피드 화면으로 이동합니다.

| 로그인                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------- |
| ![login](https://user-images.githubusercontent.com/112460466/210177956-c716414e-01c2-4c1e-b1f7-6562b9b7a857.gif) |

<br>

### [로그아웃]

- 상단 의 kebab menu를 클릭 후 나타나는 모달창의 로그아웃 버튼을 클릭하면 확인창이 뜹니다.
- 로그아웃시 로컬 저장소의 토큰 값과 사용자 정보를 삭제하고 초기화면으로 이동합니다.

| 로그아웃                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------- |
| ![logout](https://user-images.githubusercontent.com/112460466/210178009-11225733-7af5-4b8b-aa1c-fe264af01797.gif) |

<br>

### [상하단 배너]

- 상단 배너 : 각 페이지별로 다른 종류의 버튼을 가지고 있습니다.
  - 뒤로가기 : 브라우저 상에 기록된 이전 페이지로 돌아갑니다.
  - 검색 : 사용자 검색 페이지로 이동합니다.
  - 사용자 이름 : 채팅룸 페이지의 경우 상대방의 사용자 이름을 보여줍니다.
  - kebab menu : 각 페이지 또는 컴포넌트에 따른 하단 모달창을 생성합니다.
    - 상품, 댓글, 게시글 컴포넌트 - 삭제, 수정, 신고하기
    - 사용자 프로필 페이지 - 설정 및 사용자 정보, 로그아웃
- 하단 탭 메뉴 : 홈, 채팅, 게시물 작성, 프로필 아이콘을 클릭하면 각각 홈 피드, 채팅 목록, 게시글 작성 페이지, 내 프로필 페이지로 이동합니다.

| 상하단 배너                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- |
| ![tab](https://user-images.githubusercontent.com/112460466/210178028-3185f944-6ac1-468a-94ba-b32cdc5e380e.gif) |

<br>

### [홈 피드]

- 자신이 팔로우 한 유저의 게시글이 최신순으로 보여집니다.
- 팔로우 한 유저가 없거나, 팔로워의 게시글이 없을 경우 검색 버튼이 표시됩니다.
- 게시글의 상단 유저 배너 클릭 시 게시글을 작성한 유저의 프로필 페이지로, 본문 클릭 시 게시글 상세 페이지로 이동합니다.

| 팔로우하는 유저가 없을 때                                                                                        | 팔로우하는 유저가 있을 때                                                                                        |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| ![home0](https://user-images.githubusercontent.com/112460466/210379059-48900aac-3735-45c6-a249-bc9c41b49414.gif) | ![home1](https://user-images.githubusercontent.com/112460466/210379110-49153d27-0405-48e6-adfb-62c7818d2f43.gif) |

<br>

### [검색]

- 사용자 이름 혹은 계정 ID로 유저를 검색할 수 있습니다.
- 검색어와 일치하는 단어는 파란색 글씨로 표시됩니다.
- 클릭 시 해당 유저의 프로필 페이지로 진입합니다.

| 검색                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------- |
| ![search](https://user-images.githubusercontent.com/112460466/210379805-6c8a42c0-0de8-48d3-8f75-cdf0ae5f4fb6.gif) |

<br>

### [프로필]

#### 1. 내 프로필

- 상단 프로필란에 프로필 수정과 상품 등록 버튼이 나타납니다.
- 판매중인 상품란에는 사용자가 판매하는 상품이 등록되며, 판매중인 상품이 없을 경우에는 영역 자체가 나타나지 않습니다.
- 게시글란은 상단의 리스트형과 앨범형 두 개의 버튼을 통해서 나누어 볼 수 있습니다.
  - 리스트형의 경우, 사용자가 작성한 글 내용과 이미지, 좋아요와 댓글의 수를 보여줍니다.
  - 앨범형의 경우, 사용자 게시글 중 이미지가 있는 글만 필터링해 바둑판 배열로 보여줍니다.
- 게시글을 클릭하면 각 게시글의 상세페이지로 이동합니다.

| 리스트형 & 앨범형 게시글                                                                                             | 팔로잉 & 팔로워 리스트                                                                                                |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| ![myProfile](https://user-images.githubusercontent.com/112460466/210380492-40560e0b-c306-4e69-8939-cc3e7dc3d8fe.gif) | ![followList](https://user-images.githubusercontent.com/112460466/210380539-d09b0bd7-0b61-4b22-85fa-f75e6bcecb68.gif) |

<br>

#### 2. 타 유저의 프로필

- 버튼을 클릭해 해당 사용자를 팔로우 또는 언팔로우할지 결정할 수 있으며 팔로워 수의 변화가 페이지에 즉시 반영됩니다.

| 팔로우 & 언팔로우                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------- |
| ![yourProfile](https://user-images.githubusercontent.com/112460466/210380853-04f2d2bd-adab-4786-a8e8-c275ce765071.gif) |

<br>

#### 3. 프로필 수정

- 사용자 프로필 이미지, 이름, 아이디, 소개 중 한 가지를 수정하면 저장 버튼이 활성화됩니다.
- 계정 ID의 유효한 형식 및 중복 검사를 통과하지 못하면 하단에 경고 문구가 나타나며 저장 버튼이 비활성화됩니다.
- 사용자 이름과 소개는 공백으로 시작할 수 없습니다.
- 프로필 수정이 완료되면 내 프로필 페이지로 이동합니다.

| 초기화면                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------- |
| ![editProfile](https://user-images.githubusercontent.com/112460466/210381212-d67fdf87-b90c-4501-a331-f2a384534941.gif) |

<br>

### [게시글]

#### 1. 게시글 작성

- 글이 입력되거나 사진이 첨부되면 업로드 버튼이 활성화됩니다.
- 최대 세 장까지 이미지 첨부가 가능하며 첨부한 파일을 취소할 수 있습니다.
- 게시글 하단에 업로드 날짜가 표시됩니다.

| 게시글 작성                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- |
| ![uploadPost](https://user-images.githubusercontent.com/112460466/210381758-1de5a889-f587-41d2-b200-22c20a970519.gif) |

<br>

#### 2. 게시글 수정 및 삭제

- 자신의 게시글일 경우 모달 버튼을 통해 수정, 삭제가 가능합니다.
- 게시글 삭제 버튼 클릭 시, 게시글을 삭제하고 페이지를 리렌더링하여 삭제된 내용을 페이지에 반영합니다.
- 타 유저의 게시글일 경우 모달 버튼을 통해 신고할 수 있습니다.

| 게시글 수정 & 삭제                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------- |
| ![editDeletePost](https://user-images.githubusercontent.com/112460466/210382021-da057943-dc21-411e-a1f8-552be0e973bf.gif) |

<br>

#### 3. 좋아요와 댓글

- 좋아요와 댓글 수는 실시간으로 상세 페이지에 반영됩니다.
- 댓글이 몇 분 전에 작성되었는지 표시됩니다.
- 자신의 댓글일 경우 모달 버튼을 통해 삭제가 가능합니다.
- 타 유저의 댓글일 경우 모달 버튼을 통해 신고할 수 있습니다.

| 좋아요 & 댓글                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------- |
| ![likeComment](https://user-images.githubusercontent.com/112460466/210382217-01d70181-91c3-43db-a1b8-409a612afb1c.gif) |

<br>

### [상품]

#### 1. 상품 등록

- 상품 이미지, 상품명, 가격, 판매 링크를 필수로 입력해야 저장 버튼이 활성화됩니다.
- 상품 가격은 숫자만 입력할 수 있으며, 숫자를 입력하면 자동으로 원 단위로 변환됩니다.
- 상품 가격이 0원일 경우 버튼이 비활성화되며 하단에 경고 문구가 나타납니다.
- 상품명과 판매 링크는 공백으로 시작할 수 없습니다.
- 상품 등록이 완료되면 내 프로필 페이지로 이동합니다.

| 상품 등록                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------- |
| ![addProduct](https://user-images.githubusercontent.com/112460466/210386068-c6ff2e05-eb64-4abc-b6dc-93bf52b88d3f.gif) |

<br>

#### 2. 상품 수정 및 삭제

- 상품 이미지, 상품명, 가격, 판매 링크 중 한 가지를 수정하면 저장 버튼이 활성화됩니다.
- 상품 수정이 완료되면 내 프로필 페이지로 이동합니다.
- 상품 삭제 버튼 클릭 시, 상품을 삭제하고 페이지를 리렌더링하여 삭제된 내용을 페이지에 반영합니다.

| 상품 수정 & 삭제                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- |
| ![editDeleteProduct](https://user-images.githubusercontent.com/112460466/210386311-5fae87a7-745f-47c0-b8e3-fc41c65cb3cb.gif) |

<br>

### [채팅]

- 채팅 목록에서 아직 읽지 않은 채팅에는 좌측 상단의 파란색 알림을 띄워줍니다.
- 채팅방에서 메시지를 입력하거나 파일을 업로드하면 전송 버튼이 활성화됩니다.
- 채팅방에서 우측 상단의 채팅방 나가기 모달 버튼을 통해 채팅 목록 페이지로 이동할 수 있습니다.
- 채팅 메시지 전송 및 수신 기능은 개발 예정입니다.

| 채팅                                                                                                            |
| --------------------------------------------------------------------------------------------------------------- |
| ![chat](https://user-images.githubusercontent.com/112460466/210386478-ea4877c5-1728-4872-ab50-a8408ddf6dcd.gif) |

<br>

## 8. 트러블 슈팅

- [탭메뉴 프로필 버튼 이슈](https://github.com/likelion-project-README/README/wiki/README-8.%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85_%ED%83%AD%EB%A9%94%EB%89%B4-%ED%94%84%EB%A1%9C%ED%95%84-%EB%B2%84%ED%8A%BC-%EC%9D%B4%EC%8A%88)

- [프로필 수정 이슈](https://github.com/likelion-project-README/README/wiki/README-8.%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85_%ED%94%84%EB%A1%9C%ED%95%84-%EC%88%98%EC%A0%95-%EC%9D%B4%EC%8A%88)

<br>

## 9. 개선 목표

- API 모듈화 : API를 불러오는 코드의 반복이 많아 모듈화할 예정
- lighthouse Performance 증진
  - 모든 페이지에서 특히 Best Practices & SEO 점수는 90~100으로 우수
  - Performance 점수가 대체적으로 미흡한 문제
    ![KakaoTalk_Photo_2023-01-04-16-55-30](https://user-images.githubusercontent.com/112460466/210591134-09bf8efd-3c34-4b99-a3d7-895ca99e1457.png)
- **23-01-17 성능 개선 내용**
  ![성능개선 후](https://user-images.githubusercontent.com/106502312/212872369-7ceeb2cf-d551-41d2-bfb0-01e35e9903fe.png)
  - 이미지 최적화
    - `<img>` 요소에 `width` , `height` 속성값을 명시해 불필요한 Reflow를 방지했습니다.
    - browser-image-compression 라이브러리를 사용해 유저가 업로드하는 이미지를 압축했습니다.
    - Intersection Observer API를 사용해 Lazy Loading 기법을 적용하여 홈 피드의 게시글 이미지가 viewport 내에 들어오는 순간 로딩되도록 변경했습니다.
  - 웹폰트 최적화
    - WOFF2 포맷을 추가하고 가장 우선적으로 적용되도록 선언했습니다.
    - 서브셋 폰트로 교체해 용량을 줄였습니다.

<br> -->
