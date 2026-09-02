# FASHION FINDER Prototype

**슬로건: 내옷 찾는 가장 쉬운 방법**

4050 여성 패션 버티컬 플랫폼 **Fashion Finder**의 Streamlit UI/UX 프로토타입입니다.

이 레포는 완성 쇼핑몰 프론트엔드가 아니라, 개발사·UI 디자이너와 실제 클릭 흐름을 검증하기 위한 **기능형 시안**입니다.

## 핵심 컨셉

PC 첫 화면:
- **왼쪽 약 55~60%**: TALK FINDER + FINDER LIVE
- **오른쪽 약 40~45%**: 상품/착장 Discovery Banner
- 아래: 빠른 탐색 → 실시간 FASHION RANK

모바일:
1. TALK FINDER
2. FINDER LIVE
3. 상품 Discovery
4. 빠른 탐색
5. 상품 랭킹

## 포함 화면
- HOME
- TALK FINDER 자연어 검색
- 검색 결과 + 재필터링
- 상의/하의/원피스/아우터/세트 카테고리
- 브랜드 카테고리
- 브랜드 상세
- 상품 상세 + FINDER MATCH

## 자연어 검색 예시
- `77까지 편한 출근팬츠`
- `배 가려지는 77 출근 니트`
- `팔뚝커버 블라우스`
- `미샵 원피스`
- `5만원 이하 니트`
- `오늘출발`

현재는 프로토타입용 **규칙 기반 파서**입니다. 나중에 LLM 기반 파서로 교체할 수 있도록 `components/search.py`에 분리했습니다.

## 로컬 실행

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

macOS/Linux:
```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud 배포
1. GitHub에 이 폴더 전체를 새 Repository로 업로드합니다.
2. Streamlit Community Cloud에서 **New app**을 선택합니다.
3. Repository와 branch를 선택합니다.
4. Main file path를 `app.py`로 지정합니다.
5. Deploy 합니다.

## 이미지
현재 이미지 영역은 의도적으로 **placeholder**입니다.
- 메인 Discovery 이미지: `assets/hero/`
- 상품 이미지: `assets/products/`

실제 이미지를 넣는 단계에서는 이미지 규격·파일명·경로 연결을 같이 확정하면 됩니다.

## 데이터
- `data/products.csv`
- `data/brands.csv`
- `data/hero_banners.csv`

## FINDER LIVE
현재 `28,765`는 프로토타입 상수입니다. `components/data.py`의 `LIVE_PRODUCT_COUNT`를 추후 실제 API 집계로 교체합니다.

## 브랜드 위계
브랜드는 Fashion Finder의 **여러 탐색 방법 중 하나**입니다.
- 브랜드가 없어도 검색 정상 작동
- `미샵 원피스`처럼 브랜드가 포함된 경우에만 조건 추가
- 브랜드 카테고리에서는 ㄱ~ㅎ / A~Z 구조 사용
