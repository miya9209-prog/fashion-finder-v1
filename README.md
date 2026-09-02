# FASHION FINDER v1 — Update 02

사용자가 디자인한 **2안(왼쪽 Discovery / 오른쪽 Finder)**을 기준으로 정리한 전체 Streamlit 레포입니다.

## 이번 버전 방향

### 그대로 살린 부분
- 왼쪽 대형 착장/상품 Discovery
- 오른쪽 `오늘은 어떤 옷 찾으세요?`
- 자연어 질문 예시 2×2
- FINDER LIVE 보드
- 오른쪽 아래 `지금 많이 찾고 있어요` 원형 5개
- 얇은 텍스트형 GNB
- 우측 플로팅 메뉴

### 보완한 부분
- 브랜드는 서비스 중심이 아니라 GNB의 한 카테고리로 유지
- LIVE 문구를 `현재 28,796개 / 당일발송 가능한 상품 대기중 / 271개 브랜드`로 정리
- Streamlit Cloud 상단 기본 UI를 숨겨 실제 쇼핑몰 느낌 강화
- 모바일에서는 Finder가 먼저 나오도록 순서 자동 변경
- 이미지 파일만 넣으면 코드 변경 없이 바로 표시되도록 Asset 구조화
- 상품 카드의 큰 `상품 보기` 버튼을 축소형 상세 링크로 유지

## 배포

현재 GitHub 레포에 이 ZIP 내용을 **전체 덮어쓰기** 후 push 하세요.
Streamlit Community Cloud가 자동으로 재배포합니다.

## 이미지

자세한 파일명과 교체 방식은 `assets/README_IMAGES.md` 참고.

## 디자인 레퍼런스

사용자가 제공한 2안 이미지가 있다면 `assets/reference/FASHION-FINDER-MAIN-2.jpg`에 포함되어 있습니다.
