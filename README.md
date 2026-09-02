# FASHION FINDER v1 — UI Update 01

**내옷 찾는 가장 쉬운 방법**

현재 배포된 Streamlit 시안 화면을 기준으로 첫 화면을 실제 쇼핑몰에 더 가깝게 다듬은 전체 교체용 레포입니다.

## 이번 수정 내용

1. **상단 GNB**
   - 알약형 버튼 스타일 제거
   - 일반 패션몰형 텍스트 메뉴로 변경
   - `FASHION FINDER`는 워드마크처럼 강조

2. **TALK FINDER**
   - 슬로건 + 질문 + 검색창 + 예시 질문 + FINDER LIVE를 하나의 `Finder Console`로 묶음
   - 기능들이 따로 떠 보이던 느낌을 줄임

3. **FINDER LIVE**
   - `현재 28,765개`를 더 크게 표시
   - LIVE 상태 + 현재시간을 좌우로 정리
   - 시그니처 보드로 존재감 강화

4. **오른쪽 Discovery Banner**
   - 이미지 / 카피 / CTA / 좌우 이동을 한 카드 안에 통합
   - 실제 상품·착장 이미지는 다음 단계에서 적용

5. **상품 랭킹**
   - `실시간 FASHION RANK` 설명을 `지금 4050이 많이 보는 옷` 중심으로 변경
   - 모든 카드 아래의 큰 `상품 보기` 버튼 제거
   - 작은 `상세보기 →` 링크형 인터랙션으로 변경

6. **브랜드**
   - 브랜드는 여전히 하나의 카테고리/필터
   - 자연어에 브랜드명이 있을 때만 검색 조건으로 작동

## 배포 방법

현재 GitHub 레포의 파일을 이 ZIP 내용으로 **전체 덮어쓰기**하면 됩니다.

중요 파일:

```text
app.py
components/data.py
components/search.py
components/ui.py
data/products.csv
data/brands.csv
.streamlit/config.toml
requirements.txt
```

GitHub에 push하면 Streamlit Community Cloud가 자동으로 재배포합니다.

## 이미지

아직 Placeholder입니다.

- Hero/Discovery: `assets/hero/`
- 상품: `assets/products/`

다음 단계에서 실제 화면을 다시 확인한 뒤 이미지 비율, 파일명 규칙, CSV 연결 방법을 정합니다.
