# Booka

임시 설명 md입니다.

## 개발환경 세팅 방법

필요: `npm`와 `nodejs`, `pipenv`와 `python`

```sh
git clone https://github.com/kookmin-sw/capstone-2022-27
cd capstone-2022-27
cp .env.example .env // .env 파일 설정 (실제 서비스를 사용하기 위해서는 책 정보 등이 담긴 DB를 연결해 줄 필요가 있음)
pipenv shell // pipenv 가상환경 진입
pipenv install // pip 패키지 설치
npm i // npm 패키지 설치
python3 manage.py migrate // 초기 DB 설정
```

## 개발서버 실행 방법

```sh
// 터미널 1: 서버
pipenv shell
npm run server
// 터미널 2: 클라이언트
npm run dev
// 터미널 3: 코어
pipenv shell
npm run core
```
