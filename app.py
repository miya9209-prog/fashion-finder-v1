from datetime import datetime
import streamlit as st

from components.data import load_products, load_brands, LIVE_PRODUCT_COUNT
from components.search import parse_query, filter_products, humanize_filters
from components.ui import inject_css, placeholder_image, product_card_html, brand_card_html, section_title

st.set_page_config(page_title="FASHION FINDER | 내옷 찾는 가장 쉬운 방법", page_icon="FF", layout="wide", initial_sidebar_state="collapsed")
inject_css()
products = load_products(); brands = load_brands()

for k, v in {
    'page':'home','query':'','selected_product_id':None,'selected_category':'상의',
    'selected_middle':'전체','selected_brand':None,'banner_index':0
}.items():
    st.session_state.setdefault(k, v)

BANNERS = [
    {'eyebrow':"TODAY'S FIND",'title':'지금부터 가장 많이 입을\n간절기 출근룩','sub':'77까지 · 체형커버 · 오늘출발','cta':'출근룩 찾아보기','query':'77까지 체형커버 출근룩 오늘출발'},
    {'eyebrow':'4050 BEST','title':'편한데 단정한\n팬츠를 찾고 있다면','sub':'허리밴딩 · 하체커버 · 77까지','cta':'팬츠 BEST 보기','query':'77까지 하체커버 팬츠'},
    {'eyebrow':'SAME DAY','title':'오늘 주문하면\n바로 출발하는 옷','sub':'당일발송 가능 상품만 모아보기','cta':'오늘출발 보기','query':'오늘출발'},
]

def go(page, **kwargs):
    st.session_state.page = page
    for k,v in kwargs.items(): st.session_state[k] = v
    st.rerun()

def run_search(query):
    query = (query or '').strip()
    if not query: return
    st.session_state.query = query; st.session_state.page = 'search'; st.rerun()

def nav_header():
    cols = st.columns([2.3,.72,.72,.86,.72,.72,.9,.9,.72,1.04,.6,.6])
    with cols[0]:
        if st.button('FASHION FINDER', key='logo_btn', use_container_width=True): go('home')
    navs=[('NEW','search','신상품'),('BEST','search','BEST'),('브랜드','brands',None),('상의','category','상의'),('하의','category','하의'),('원피스','category','원피스'),('아우터','category','아우터'),('세트','category','세트'),('체형커버','search','체형커버')]
    for col,(label,page,val) in zip(cols[1:10],navs):
        with col:
            if st.button(label,key=f'nav_{label}',use_container_width=True):
                if page=='category': go('category',selected_category=val,selected_middle='전체')
                elif page=='search': run_search(val)
                else: go(page)
    with cols[10]: st.markdown("<div class='nav-icon'>♡</div>",unsafe_allow_html=True)
    with cols[11]: st.markdown("<div class='nav-icon'>BAG</div>",unsafe_allow_html=True)
    st.markdown("<div class='nav-rule'></div>",unsafe_allow_html=True)

def finder_input(prefix, default_query=''):
    qcol,bcol=st.columns([8.8,1.2])
    with qcol:
        q=st.text_input('원하는 옷',value=default_query,key=f'{prefix}_query',placeholder='원하는 옷을 편하게 말씀해주세요',label_visibility='collapsed')
    with bcol:
        if st.button('찾기 →',key=f'{prefix}_submit',use_container_width=True,type='primary'): run_search(q)
    return q

def render_live_card():
    now=datetime.now().strftime('%H:%M:%S')
    st.markdown(f"""<div class='live-card'><div class='live-top'><span class='live-dot'></span> FINDER LIVE <span class='live-time'>{now}</span></div><div class='live-number'>{LIVE_PRODUCT_COUNT:,}</div><div class='live-label'>당일발송 상품 대기중</div></div>""",unsafe_allow_html=True)

def render_product_grid(df,prefix='grid',cols_count=4,limit=8):
    if df.empty:
        st.markdown("<div class='empty-box'><div class='empty-title'>조건에 딱 맞는 상품을 찾는 중이에요.</div><div class='muted'>조건을 하나 줄이거나, 더 편한 표현으로 다시 물어보세요.</div></div>",unsafe_allow_html=True); return
    view=df.head(limit); cols=st.columns(cols_count)
    for idx,(_,row) in enumerate(view.iterrows()):
        with cols[idx%cols_count]:
            st.markdown(product_card_html(row),unsafe_allow_html=True)
            if st.button('상품 보기',key=f'{prefix}_{row["product_id"]}',use_container_width=True): go('product',selected_product_id=row['product_id'])

def home_page():
    left,right=st.columns([1.32,1.0],gap='large')
    with left:
        st.markdown("<div class='eyebrow red'>내옷 찾는 가장 쉬운 방법</div>",unsafe_allow_html=True)
        st.markdown("<h1 class='hero-title'>오늘은 어떤 옷을<br>찾으세요?</h1>",unsafe_allow_html=True)
        finder_input('home')
        st.markdown("<div class='helper-label'>이렇게 찾아보세요</div>",unsafe_allow_html=True)
        excols=st.columns(4); examples=[('77까지 편한 출근팬츠','77까지 편한 출근팬츠'),('팔뚝 가려주는 블라우스','팔뚝커버 블라우스'),('뱃살 티 안 나는 니트','뱃살커버 니트'),('9월 여행 원피스','여행 원피스')]
        for col,(label,q) in zip(excols,examples):
            with col:
                if st.button(label,key=f'ex_{label}',use_container_width=True): run_search(q)
        render_live_card()
    with right:
        b=BANNERS[st.session_state.banner_index]
        st.markdown(f"""<div class='discovery-banner'><div class='banner-image-placeholder'><div class='image-note'>DISCOVERY IMAGE</div></div><div class='banner-copy'><div class='eyebrow'>{b['eyebrow']}</div><div class='banner-title'>{b['title'].replace(chr(10),'<br>')}</div><div class='banner-sub'>{b['sub']}</div></div></div>""",unsafe_allow_html=True)
        c1,c2,c3=st.columns([5,1,1])
        with c1:
            if st.button(b['cta'],key='banner_cta',use_container_width=True,type='primary'): run_search(b['query'])
        with c2:
            if st.button('‹',key='banner_prev',use_container_width=True): st.session_state.banner_index=(st.session_state.banner_index-1)%len(BANNERS); st.rerun()
        with c3:
            if st.button('›',key='banner_next',use_container_width=True): st.session_state.banner_index=(st.session_state.banner_index+1)%len(BANNERS); st.rerun()
    st.markdown("<div class='section-gap'></div>",unsafe_allow_html=True)
    section_title('지금 많이 찾고 있어요','말하지 않아도 바로 고를 수 있는 빠른 탐색')
    qcols=st.columns(6); quicks=[('출근룩','출근룩'),('체형커버','체형커버'),('77+','77까지'),('간절기','간절기'),('오늘출발','오늘출발'),('브랜드','__brands__')]
    for col,(label,q) in zip(qcols,quicks):
        with col:
            if st.button(label,key=f'quick_{label}',use_container_width=True): go('brands') if q=='__brands__' else run_search(q)
    st.markdown("<div class='section-gap-sm'></div>",unsafe_allow_html=True)
    section_title('실시간 FASHION RANK','4050 고객에게 반응이 좋은 상품을 먼저 보여줍니다')
    render_product_grid(products.sort_values(['rank_score','same_day'],ascending=[False,False]),prefix='rank',cols_count=4,limit=8)

def search_page():
    st.markdown("<div class='eyebrow red'>TALK FINDER</div>",unsafe_allow_html=True)
    st.markdown("<h2 class='page-title'>찾고 싶은 옷을 말해주세요.</h2>",unsafe_allow_html=True)
    finder_input('search',st.session_state.query)
    parsed=parse_query(st.session_state.query,brands['brand'].tolist()); base=filter_products(products,parsed); labels=humanize_filters(parsed)
    st.markdown(f"<div class='search-summary'><div class='result-title'>찾았어요! <b>{len(base)}개</b> 상품이 있습니다.</div><div class='chip-row'>{''.join([f'<span class=\"filter-chip\">{x}</span>' for x in labels])}</div></div>",unsafe_allow_html=True)
    fcol,pcol=st.columns([1.0,3.4],gap='large')
    with fcol:
        st.markdown("<div class='filter-title'>더 골라보기</div>",unsafe_allow_html=True)
        opts=['전체']+brands['brand'].tolist(); default_brand=parsed.get('brand') if parsed.get('brand') in opts else '전체'
        brand=st.selectbox('브랜드',opts,index=opts.index(default_brand)); size=st.selectbox('사이즈',['전체','55','66','77까지','88까지']); concern=st.selectbox('체형 고민',['전체','팔뚝커버','뱃살커버','하체커버','힙커버']); tpo=st.selectbox('입는 상황',['전체','출근','데일리','모임','여행']); same_day=st.checkbox('당일발송만'); max_price=st.slider('최대 가격',30000,120000,80000,5000)
        refined=dict(parsed)
        if brand!='전체': refined['brand']=brand
        if size=='77까지': refined['min_max_size']=max(refined.get('min_max_size',0),77)
        elif size=='88까지': refined['min_max_size']=max(refined.get('min_max_size',0),88)
        elif size in ('55','66'): refined['size_contains']=size
        if concern!='전체': refined['concern']=concern
        if tpo!='전체': refined['tpo']=tpo
        if same_day: refined['same_day']=True
        refined['max_price']=max_price; refined_df=filter_products(products,refined)
        st.markdown(f"<div class='filter-count'>현재 <b>{len(refined_df)}개</b></div>",unsafe_allow_html=True)
    with pcol:
        tc1,tc2=st.columns([4,1])
        with tc1: st.markdown(f"<div class='product-count'>{len(refined_df)}개 상품</div>",unsafe_allow_html=True)
        with tc2: sort=st.selectbox('정렬',['추천순','낮은가격순','높은가격순'],label_visibility='collapsed')
        if sort=='낮은가격순': refined_df=refined_df.sort_values('price')
        elif sort=='높은가격순': refined_df=refined_df.sort_values('price',ascending=False)
        else: refined_df=refined_df.sort_values('rank_score',ascending=False)
        render_product_grid(refined_df,prefix='searchprod',cols_count=3,limit=12)

def category_page():
    category=st.session_state.selected_category
    st.markdown(f"<div class='eyebrow'>CATEGORY</div><h2 class='page-title'>{category}</h2>",unsafe_allow_html=True)
    mids=['전체']+sorted(products.loc[products['major_category']==category,'middle_category'].dropna().unique().tolist()); cols=st.columns(min(len(mids),7))
    for col,mid in zip(cols,mids):
        with col:
            if st.button(mid,key=f'mid_{category}_{mid}',use_container_width=True,type='primary' if st.session_state.selected_middle==mid else 'secondary'): st.session_state.selected_middle=mid; st.rerun()
    df=products[products['major_category']==category]
    if st.session_state.selected_middle!='전체': df=df[df['middle_category']==st.session_state.selected_middle]
    st.markdown("<div class='section-gap-sm'></div>",unsafe_allow_html=True)
    fcols=st.columns(5); labels=[('77까지','77까지'),('체형커버','체형커버'),('출근룩','출근룩'),('브랜드','__brands__'),('오늘출발','오늘출발')]
    for col,(label,q) in zip(fcols,labels):
        with col:
            if st.button(label,key=f'catquick_{category}_{label}',use_container_width=True): go('brands') if q=='__brands__' else run_search(f"{st.session_state.selected_middle if st.session_state.selected_middle!='전체' else category} {q}")
    section_title(st.session_state.selected_middle if st.session_state.selected_middle!='전체' else category,f'총 {len(df)}개')
    render_product_grid(df.sort_values('rank_score',ascending=False),prefix='catprod',cols_count=4,limit=16)

def brands_page():
    st.markdown("<div class='eyebrow'>BRANDS</div><h2 class='page-title'>브랜드</h2>",unsafe_allow_html=True)
    bq=st.text_input('브랜드명 검색',placeholder='브랜드명을 검색하세요'); view=brands[brands['brand'].str.contains(bq,case=False,na=False)] if bq else brands
    st.markdown("<div class='brand-index'>ㄱ　ㄴ　ㄷ　ㄹ　ㅁ　ㅂ　ㅅ　ㅇ　ㅈ　ㅊ　ㅋ　ㅌ　ㅍ　ㅎ<br>A　B　C　D　E　F　G　H　I　J　K　L　M　N　O　P　Q　R　S　T　U　V　W　X　Y　Z　#</div>",unsafe_allow_html=True)
    section_title('브랜드 찾기','브랜드는 Fashion Finder의 여러 탐색 방법 중 하나입니다'); cols=st.columns(4)
    for idx,(_,row) in enumerate(view.iterrows()):
        with cols[idx%4]:
            st.markdown(brand_card_html(row),unsafe_allow_html=True)
            if st.button('브랜드 보기',key=f'brand_{row["brand"]}',use_container_width=True): go('brand_detail',selected_brand=row['brand'])

def brand_detail_page():
    brand=st.session_state.selected_brand
    if not brand: go('brands')
    info=brands[brands['brand']==brand].iloc[0]; st.markdown(f"<div class='eyebrow'>BRAND</div><h2 class='page-title'>{brand}</h2><div class='brand-desc'>{info['description']}</div>",unsafe_allow_html=True)
    df=products[products['brand']==brand]; qcols=st.columns(5)
    for col,(label,q) in zip(qcols,[('전체상품',brand),('77까지',f'{brand} 77까지'),('체형커버',f'{brand} 체형커버'),('출근룩',f'{brand} 출근룩'),('오늘출발',f'{brand} 오늘출발')]):
        with col:
            if st.button(label,key=f'brandquick_{label}',use_container_width=True): st.rerun() if label=='전체상품' else run_search(q)
    section_title('전체상품',f'{len(df)}개'); render_product_grid(df.sort_values('rank_score',ascending=False),prefix='brandprod',cols_count=4,limit=16)

def product_page():
    pid=st.session_state.selected_product_id
    if pid is None or pid not in products['product_id'].values: go('home')
    row=products[products['product_id']==pid].iloc[0]; img,info=st.columns([1.05,1.0],gap='large')
    with img: st.markdown(placeholder_image('PRODUCT IMAGE',tall=True),unsafe_allow_html=True)
    with info:
        st.markdown(f"<div class='product-brand'>{row['brand']}</div><h2 class='detail-title'>{row['name']}</h2><div class='detail-price'>{int(row['price']):,}원</div>",unsafe_allow_html=True)
        chips=[f"{int(row['max_size'])}까지" if float(row['max_size'])>0 else 'FREE', row['body_concerns'].split('|')[0] if row['body_concerns'] else '편안한 핏', row['tpo'].split('|')[0] if row['tpo'] else '데일리', row['middle_category']]
        st.markdown("<div class='match-label'>FINDER MATCH</div><div class='chip-row'>"+''.join([f"<span class='filter-chip'>{c}</span>" for c in chips])+"</div>",unsafe_allow_html=True)
        st.markdown(f"<div class='why-box'><div class='why-title'>왜 잘 맞나요?</div><div class='why-copy'>{row['description']}</div></div>",unsafe_allow_html=True)
        st.selectbox('색상',row['color'].split('|')); st.selectbox('사이즈',row['sizes'].split('|')); st.button('구매하기 (시안)',use_container_width=True,type='primary')
        if st.button('비슷한 상품 찾아보기',use_container_width=True): run_search(f"{row['middle_category']} {row['tpo'].split('|')[0]} {int(row['max_size'])}까지" if float(row['max_size'])>0 else row['middle_category'])

nav_header(); page=st.session_state.page
{'home':home_page,'search':search_page,'category':category_page,'brands':brands_page,'brand_detail':brand_detail_page,'product':product_page}.get(page,home_page)()
