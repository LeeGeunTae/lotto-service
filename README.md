# 로또 서비스 (Lotto Service)

Django와 Docker를 사용하여 구축된 로또 서비스 프로젝트입니다.

## 주요 기능
1. **로또 구매**
   - 자동 번호 생성 또는 직접 번호 입력을 통해 로또 구매 가능.
   - 비밀번호(4자리)를 사용하여 구매 번호 확인 가능.

2. **로또 번호 확인**
   - 구매한 로또 번호와 당첨 번호를 비교하여 당첨 여부를 확인.

3. **관리자 기능**
   - 당첨 번호 추첨.
   - 구매된 로또 번호 통계 및 당첨자 수 확인.

4. **화면 구성**
   - 메인 화면: 최근 회차 당첨 번호 및 당첨자 수 표시.
   - 구매 화면: 로또 번호를 입력하거나 자동 생성으로 구매.
   - 확인 화면: 비밀번호로 구매한 로또 번호와 당첨 여부 확인.
   - 관리자 화면: 당첨 번호 생성 및 통계 확인.

## 실행 방법
1. **Docker로 실행**
   ```bash
   docker-compose up --build
2. **접속 주소**
   - 메인 화면 : http://127.0.0.1:8000
   - 로또 번호 확인 : http://127.0.0.1:8000/check
   - 관리자 페이지 : http://127.0.0.1:8000/admin

## 프로젝트 구조도
lotto_service/
├── manage.py                     # Django 관리 명령어
├── lotto_project/                # Django 프로젝트 디렉토리
│   ├── settings.py               # Django 설정 파일
│   ├── urls.py                   # 프로젝트 URL 설정
├── lotto/                        # 로또 앱 디렉토리
│   ├── models.py                 # 데이터베이스 모델
│   ├── views.py                  # 뷰 로직
│   ├── templates/lotto/          # 템플릿 디렉토리
│   │   ├── home.html             # 메인 화면 템플릿
│   │   ├── buy.html              # 구매 화면 템플릿
│   │   ├── check.html            # 확인 화면 템플릿
│   │   └── admin_panel.html      # 관리자 화면 템플릿
│   ├── static/css/               # 정적 파일 디렉토리
│   │   └── style.css             # CSS 스타일
├── Dockerfile                    # Docker 설정 파일
├── docker-compose.yml            # Docker Compose 설정 파일
└── requirements.txt              # Python 패키지 의존성
