from datetime import datetime
from urllib.parse import quote_plus
import html
import streamlit as st

from components.data import load_products, load_brands, LIVE_PRODUCT_COUNT, LIVE_BRAND_COUNT
from components.search import parse_query, filter_products, humanize_filters
from components.ui import inject_css, product_card_html, brand_card_html, section_title, asset_image_html, asset_uri, qurl, nav_url

st.set_page_config(page_title="FASHION FINDER | 내옷 찾는 가장 쉬운 방법", page_icon="🛍️", layout="wide", initial_sidebar_state="collapsed")
inject_css()
products = load_products(); brands = load_brands()

DEFAULTS = {"page":"home","query":"","selected_product_id":None,"selected_category":"상의","selected_middle":"전체","selected_brand":None}
for k,v in DEFAULTS.items(): st.session_state.setdefault(k,v)

# HTML links/forms use query params so the top design can be pixel-controlled.
params = st.query_params
if params.get("page"):
    st.session_state.page = params.get("page")
if params.get("q"):
    st.session_state.query = params.get("q")
    st.session_state.page = "search"
if params.get("category"):
    st.session_state.selected_category = params.get("category")
    st.session_state.selected_middle = "전체"
if params.get("brand"):
    st.session_state.selected_brand = params.get("brand")
    st.session_state.page = "brand_detail"

BANNER = {
    "eyebrow":"TODAY'S FIND",
    "title":"지금부터 가장 많이 입을<br>간절기 출근룩",
    "sub":"77까지 · 체형커버 · 오늘출발",
    "count":"10,276개",
    "query":"77까지 체형커버 출근룩 오늘출발",
    "image":"assets/hero/main_01.jpg",
}
QUICK = [
    ("출근룩 최근 80%","출근룩","assets/quick/q01.jpg"),
    ("연휴 여행룩","여행룩","assets/quick/q02.jpg"),
    ("간절기 가디건","가디건","assets/quick/q03.jpg"),
    ("체형커버 슬랙스","체형커버 슬랙스","assets/quick/q04.jpg"),
    ("신경쓰이는 모임룩","모임룩","assets/quick/q05.jpg"),
]
EXAMPLES = [
    ("“배 좀 가려지고 77도 입는 출근용 니트 찾아줘”","77까지 뱃살커버 출근 니트"),
    ("“내가 힙이 좀 있는 편인데 편한 청바지 추천해줘”","힙커버 편한 데님"),
    ("“내일 시댁가는데 얌전하면서 편한 원피스 필요해”","단정한 편한 원피스"),
    ("“어려보이면서도 너무 튀지 않는 셔츠 있어?”","부드러운 인상 셔츠"),
]


def go(page, **kwargs):
    st.session_state.page = page
    for k,v in kwargs.items(): st.session_state[k] = v
    st.rerun()


def run_search(q):
    q = (q or "").strip()
    if not q: return
    st.session_state.query = q; st.session_state.page = "search"; st.rerun()


def header_html():
    bi = asset_uri("assets/brand/bi.png")
    navs = [
        ("NEW",nav_url("search","신상품")),("BEST",nav_url("search","BEST")),("브랜드",nav_url("brands")),
        ("상의",nav_url("category","상의")),("하의",nav_url("category","하의")),("원피스",nav_url("category","원피스")),
        ("아우터",nav_url("category","아우터")),("세트",nav_url("category","세트")),("체형커버",nav_url("search","체형커버")),
    ]
    nav_html = "".join([f"<a href='{u}'>{html.escape(t)}</a>" for t,u in navs])
    return f"""
    <div class='ff-header'>
      <div class='ff-head-row'>
        <a href='?page=home'><img class='ff-bi' src='{bi}' alt='FASHION FINDER'></a>
        <nav class='ff-nav'>{nav_html}</nav>
        <div class='ff-utils'><a class='heart' href='#'>♡</a><a class='bag' href='#'>BAG</a></div>
      </div>
    </div>
    """


def home_hero_html():
    hero = asset_uri(BANNER["image"])
    floating = asset_uri("assets/floating/tools.png")
    examples = "".join([f"<span class='ff-example'>{html.escape(label)}</span>" for label,_q in EXAMPLES])
    quicks = []
    for label,q,img_path in QUICK:
        img = asset_uri(img_path)
        style = f"background-image:url('{img}')" if img else ""
        quicks.append(f"<a class='ff-quick-item' href='{qurl(q)}'><span class='ff-quick-img' style=\"{style}\"></span><span class='ff-quick-label'>{html.escape(label)}</span></a>")
    now = datetime.now().strftime("%H:%M:%S")
    return f"""
    <div class='ff-hero'>
      <section class='ff-discovery'>
        <div class='ff-hero-image' style="background-image:url('{hero}')"></div>
        <div class='ff-discovery-copy'>
          <div class='ff-eyebrow'>{BANNER['eyebrow']}</div>
          <h2 class='ff-discovery-title'>{BANNER['title']}</h2>
          <div class='ff-discovery-sub'>{BANNER['sub']}</div>
        </div>
        <a class='ff-discovery-cta' href='{qurl(BANNER['query'])}'>출근룩 <strong>{BANNER['count']}</strong> 보러가기</a>
      </section>

      <section class='ff-finder-side'>
        <div class='ff-finder-card'>
          <div class='ff-finder-top'>
            <h1 class='ff-finder-title'>오늘은 어떤 옷 찾으세요?</h1>
            <form class='ff-search-form' method='get'>
              <input type='hidden' name='page' value='search'>
              <input class='ff-search-input' name='q' placeholder='원하는 옷을 편하게 말씀해주세요' autocomplete='off'>
              <button class='ff-search-submit' type='submit'>찾기 →</button>
            </form>
            <div class='ff-helper'>이렇게 찾아보세요</div>
            <div class='ff-examples'>{examples}</div>
          </div>
          <div class='ff-live'>
            <div class='ff-live-top'><span><span class='ff-live-dot'></span>FINDER LIVE</span><span class='ff-live-time'>{now}</span></div>
            <div class='ff-live-row'>
              <div class='ff-live-copy'>당일발송 가능한 상품 대기중</div>
              <div class='ff-live-number'><span class='prefix'>현재</span><b>{LIVE_PRODUCT_COUNT:,}</b><span class='unit'>개</span></div>
              <div class='ff-live-brand'>{LIVE_BRAND_COUNT}개 브랜드</div>
            </div>
          </div>
        </div>
        <div class='ff-quick'>
          <h2 class='ff-quick-title'>지금 많이 찾고 있어요</h2>
          <div class='ff-quick-grid'>{''.join(quicks)}</div>
        </div>
      </section>
    </div>
    <img class='ff-floating' src='{floating}' alt='빠른 메뉴'>
    """


def finder_input(prefix, default=""):
    qcol,bcol = st.columns([8.6,1.4],gap="small")
    with qcol:
        q = st.text_input("원하는 옷", value=default, key=f"{prefix}_query", placeholder="원하는 옷을 편하게 말씀해주세요", label_visibility="collapsed")
    with bcol:
        if st.button("찾기 →", key=f"{prefix}_submit", use_container_width=True, type="primary"): run_search(q)
    return q


def render_grid(df,prefix="grid",cols_count=4,limit=8):
    if df.empty:
        st.markdown("<div class='empty-box'><div class='empty-title'>조건에 딱 맞는 상품이 아직 없어요.</div><div class='muted'>조건을 하나 줄이거나 더 편한 표현으로 다시 물어보세요.</div></div>",unsafe_allow_html=True); return
    cols=st.columns(cols_count,gap="medium")
    for idx,(_,row) in enumerate(df.head(limit).iterrows()):
        with cols[idx%cols_count]:
            with st.container(key=f"product_{prefix}_{row.product_id}"):
                st.markdown(product_card_html(row),unsafe_allow_html=True)
                if st.button("상세보기 →",key=f"open_{prefix}_{row.product_id}"): go("product",selected_product_id=row.product_id)


def home_page():
    st.markdown(home_hero_html(), unsafe_allow_html=True)
    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
    section_title("지금 4050이 많이 보는 옷","실시간 FASHION RANK")
    render_grid(products.sort_values(["rank_score","same_day"],ascending=[False,False]),"rank",4,8)


def search_page():
    st.markdown("<div class='eyebrow red'>TALK FINDER</div><h2 class='page-title'>찾고 싶은 옷을 말해주세요.</h2>",unsafe_allow_html=True)
    finder_input("search",st.session_state.query)
    parsed=parse_query(st.session_state.query,brands.brand.tolist()); base=filter_products(products,parsed); labels=humanize_filters(parsed)
    chips="".join([f"<span class='filter-chip'>{html.escape(x)}</span>" for x in labels])
    st.markdown(f"<div class='search-summary'><div class='result-title'>찾았어요! <b>{len(base)}개</b> 상품이 있습니다.</div><div class='chip-row'>{chips}</div></div>",unsafe_allow_html=True)
    fcol,pcol=st.columns([1,3.5],gap="large")
    with fcol:
        st.markdown("<div class='filter-title'>더 골라보기</div>",unsafe_allow_html=True)
        brand=st.selectbox("브랜드",["전체"]+brands.brand.tolist()); size=st.selectbox("사이즈",["전체","55","66","77까지","88까지"]); concern=st.selectbox("체형 고민",["전체","팔뚝커버","뱃살커버","하체커버","힙커버"]); tpo=st.selectbox("입는 상황",["전체","출근","데일리","모임","여행"]); same=st.checkbox("당일발송만"); maxp=st.slider("최대 가격",30000,120000,80000,5000)
        refined=dict(parsed)
        if brand!="전체": refined["brand"]=brand
        if size=="77까지": refined["min_max_size"]=77
        elif size=="88까지": refined["min_max_size"]=88
        elif size in ("55","66"): refined["size_contains"]=size
        if concern!="전체": refined["concern"]=concern
        if tpo!="전체": refined["tpo"]=tpo
        if same: refined["same_day"]=True
        refined["max_price"]=maxp
        rdf=filter_products(products,refined); st.markdown(f"<div class='filter-count'>현재 <b>{len(rdf)}개</b></div>",unsafe_allow_html=True)
    with pcol:
        sort=st.selectbox("정렬",["추천순","낮은가격순","높은가격순"],label_visibility="collapsed")
        if sort=="낮은가격순": rdf=rdf.sort_values("price")
        elif sort=="높은가격순": rdf=rdf.sort_values("price",ascending=False)
        else: rdf=rdf.sort_values("rank_score",ascending=False)
        render_grid(rdf,"search",3,12)


def category_page():
    cat=st.session_state.selected_category
    st.markdown(f"<div class='eyebrow'>CATEGORY</div><h2 class='page-title'>{html.escape(cat)}</h2>",unsafe_allow_html=True)
    mids=["전체"]+sorted(products.loc[products.major_category==cat,"middle_category"].dropna().unique().tolist())
    cols=st.columns(min(len(mids),7),gap="small")
    for col,mid in zip(cols,mids):
        with col:
            if st.button(mid,key=f"mid_{cat}_{mid}",use_container_width=True,type="primary" if st.session_state.selected_middle==mid else "secondary"): st.session_state.selected_middle=mid; st.rerun()
    df=products[products.major_category==cat]
    if st.session_state.selected_middle!="전체": df=df[df.middle_category==st.session_state.selected_middle]
    section_title(st.session_state.selected_middle if st.session_state.selected_middle!="전체" else cat,f"총 {len(df)}개")
    render_grid(df.sort_values("rank_score",ascending=False),"cat",4,16)


def brands_page():
    st.markdown("<div class='eyebrow'>BRANDS</div><h2 class='page-title'>브랜드</h2>",unsafe_allow_html=True)
    q=st.text_input("브랜드명 검색",placeholder="브랜드명을 검색하세요")
    view=brands if not q else brands[brands.brand.str.contains(q,case=False,na=False)|brands.brand_ko.str.contains(q,case=False,na=False)]
    st.markdown("<div class='brand-index'>ㄱ　ㄴ　ㄷ　ㄹ　ㅁ　ㅂ　ㅅ　ㅇ　ㅈ　ㅊ　ㅋ　ㅌ　ㅍ　ㅎ<br>A　B　C　D　E　F　G　H　I　J　K　L　M　N　O　P　Q　R　S　T　U　V　W　X　Y　Z　#</div>",unsafe_allow_html=True)
    cols=st.columns(4,gap="medium")
    for i,(_,row) in enumerate(view.iterrows()):
        with cols[i%4]:
            st.markdown(brand_card_html(row),unsafe_allow_html=True)
            if st.button("브랜드 보기 →",key=f"brand_{row.brand}"): go("brand_detail",selected_brand=row.brand)


def brand_detail_page():
    brand=st.session_state.selected_brand
    if not brand: return go("brands")
    info=brands[brands.brand==brand].iloc[0]; df=products[products.brand==brand]
    st.markdown(f"<div class='eyebrow'>BRAND</div><h2 class='page-title'>{html.escape(brand)}</h2><div class='brand-desc'>{html.escape(info.description)}</div>",unsafe_allow_html=True)
    section_title("전체상품",f"{len(df)}개"); render_grid(df.sort_values("rank_score",ascending=False),"brand",4,16)


def product_page():
    pid=st.session_state.selected_product_id
    if pid not in products.product_id.values: return go("home")
    row=products[products.product_id==pid].iloc[0]
    a,b=st.columns([1.05,1],gap="large")
    with a: st.markdown(asset_image_html(f"assets/products/{row.product_id}.jpg","PRODUCT IMAGE","product-image-tall"),unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='product-brand'>{html.escape(row.brand)}</div><h2 class='detail-title'>{html.escape(row['name'])}</h2><div class='detail-price'>{int(row.price):,}원</div>",unsafe_allow_html=True)
        chips=[f"{int(row.max_size)}까지" if row.max_size>0 else "FREE", row.body_concerns.split("|")[0] if row.body_concerns else "편안한 핏", row.tpo.split("|")[0], row.middle_category]
        st.markdown("<div class='match-label'>FINDER MATCH</div><div class='chip-row'>"+"".join([f"<span class='filter-chip'>{html.escape(x)}</span>" for x in chips])+"</div>",unsafe_allow_html=True)
        st.markdown(f"<div class='why-box'><div class='why-title'>왜 잘 맞나요?</div><div class='why-copy'>{html.escape(row.description)}</div></div>",unsafe_allow_html=True)
        st.selectbox("색상",row.color.split("|")); st.selectbox("사이즈",row.sizes.split("|")); st.button("구매하기 (시안)",use_container_width=True,type="primary")

st.markdown(header_html(), unsafe_allow_html=True)
page=st.session_state.page
{"home":home_page,"search":search_page,"category":category_page,"brands":brands_page,"brand_detail":brand_detail_page,"product":product_page}.get(page,home_page)()
