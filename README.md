# Booka

임시 설명 md입니다.

## 개발환경 세팅 방법

필요: `npm`와 `nodejs`, `pipenv`와 `python`

```sh
git clone https://github.com/kookmin-sw/capstone-2022-27
cd capstone-2022-27
git checkout <branch> // 원하는 브랜치
pipenv shell // pipenv 가상환경 진입
pipenv install // pip 패키지 설치
npm i // npm 패키지 설치
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
cd core
python3 server.py
```

## 개발문서 확인 방법

swagger를 이용함
서버가 실행된 상태에서 [브라우저로 접속](http://127.0.0.1:3001/swagger/)

## 컨벤션

### 프론트

```svelte
<ul>
    <li>indent: 4 space</li>
    <li>html, script, style 순서로 배치하기</li>
    <li>각 부분 사이에 한 줄 공백 넣기, script와 style은 1 indent</li>
</ul>

<script>
    let var1 = "let, const 등 ecmascript 사용"
    const var2 = "세미콜론 사용하지 않기"
</script>

<style>
    div {
        color: red;
    }
</style>
```
