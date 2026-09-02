# FASHION FINDER v1 — Update 04

이번 버전은 **사용자 제공 기준 디자인 `FASHION-FINDER-MAIN-2.jpg`를 다시 해석하지 않고 직접 기준으로 삼아** 상단을 재구현했습니다.

## 핵심 수정

- 상단 GNB를 Streamlit `st.columns`가 아니라 **고정 CSS Grid/HTML**로 구현
- 좌측 Discovery와 우측 Finder+Quick 영역을 **동일한 590px 높이**로 맞춤
- Discovery 이미지: 기준 디자인과 같은 `476×364` 비율
- Finder 카드: 기준 디자인과 같은 약 `362px` 높이
- 자연어 예시: 반드시 **2열 × 2행**으로 고정
- `지금 많이 찾고 있어요`: Finder 아래 5개 원형 이미지 한 줄 고정
- BI 이미지, 착장 이미지, 원형 이미지, 우측 플로팅 메뉴를 실제 Asset으로 포함
- 상단은 HTML GET 링크/폼을 사용해 디자인 정렬을 Streamlit 위젯 레이아웃에 의존하지 않음

## 기준 이미지

`assets/reference/TARGET_MAIN_2.jpg`

이 이미지가 상단 UI의 기준입니다.

## 덮어쓰기

기존 GitHub 레포에 이 ZIP의 내용을 전체 덮어쓰기하고 push 하세요.
