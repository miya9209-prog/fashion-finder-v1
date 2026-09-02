import html


def inject_css():
    import streamlit as st
    st.markdown(r"""<style>
    :root{
      --ff-red:#E54456;--ff-ink:#1B1B1B;--ff-gray:#777;--ff-line:#E8E8E8;
      --ff-soft:#F7F7F7;--ff-beige:#F7F3EB;--ff-blue:#EEF4FF;
    }
    .stApp{background:#fff;color:var(--ff-ink)}
    .block-container{max-width:1420px;padding-top:1rem;padding-bottom:4rem}
    [data-testid='stSidebar'],[data-testid='stSidebarCollapsedControl']{display:none!important}
    header[data-testid='stHeader']{background:transparent}

    /* 기본 버튼 */
    .stButton>button{
      border-radius:999px;border:1px solid #E2E2E2;background:#fff;color:#252525;
      font-weight:650;min-height:40px;transition:.18s ease
    }
    .stButton>button:hover{border-color:#CFCFCF;color:var(--ff-red)}
    .stButton>button[kind='primary']{background:var(--ff-ink);color:#fff;border-color:var(--ff-ink)}

    /* 쇼핑몰형 GNB: 알약 버튼 제거 */
    .st-key-topnav .stButton>button{
      border:none!important;background:transparent!important;border-radius:0!important;box-shadow:none!important;
      min-height:42px!important;padding:.2rem .1rem!important;color:#252525!important;font-size:13px!important;font-weight:600!important
    }
    .st-key-topnav .stButton>button:hover{color:var(--ff-red)!important}
    .st-key-topnav [data-testid='column']:first-child .stButton>button{
      justify-content:flex-start;font-size:18px!important;font-weight:850!important;letter-spacing:-.035em
    }
    .nav-icon{text-align:center;font-size:14px;font-weight:700;padding-top:11px;color:#333}
    .nav-icon.bag{font-size:11px;letter-spacing:.04em;padding-top:13px}
    .nav-rule{height:1px;background:#ECECEC;margin:.15rem 0 2rem}

    .eyebrow{font-size:12px;font-weight:850;letter-spacing:.07em;color:#555;margin-bottom:.7rem}
    .eyebrow.red{color:var(--ff-red)}
    .hero-title{font-size:clamp(42px,4vw,64px);line-height:1.06;letter-spacing:-.055em;margin:.2rem 0 1.45rem}
    .page-title{font-size:38px;line-height:1.15;letter-spacing:-.04em;margin:.1rem 0 1.3rem}
    .helper-label{font-size:12px;color:#858585;margin:1.15rem 0 .45rem;font-weight:750}

    div[data-baseweb='input']>div{
      border-radius:999px!important;min-height:50px!important;background:#F7F7F8!important;border-color:#EEEEEE!important
    }

    /* TALK FINDER 전체를 하나의 Console로 */
    .st-key-finder_console{
      border:1px solid #EEEEEE;border-radius:28px;padding:1.55rem 1.7rem 1.5rem;background:#fff;
      box-shadow:0 10px 35px rgba(0,0,0,.025)
    }

    /* FINDER LIVE 존재감 강화 */
    .live-card{margin-top:1.15rem;background:var(--ff-beige);border-radius:22px;padding:1.15rem 1.35rem 1.25rem}
    .live-top{display:flex;align-items:center;justify-content:space-between;font-size:11px;font-weight:850;letter-spacing:.02em}
    .live-dot{display:inline-block;width:8px;height:8px;background:#2AA36B;border-radius:50%;margin-right:7px}
    .live-time{font-size:15px;font-weight:800;letter-spacing:.02em}
    .live-main{display:flex;align-items:baseline;gap:8px;margin-top:.45rem}
    .live-prefix{font-size:15px;color:#666;font-weight:700}
    .live-number{font-size:48px;line-height:1;font-weight:900;letter-spacing:-.055em}
    .live-unit{font-size:16px;font-weight:850}
    .live-label{font-size:13px;color:#666;margin-top:.25rem}

    /* Discovery: 이미지/카피/CTA를 하나의 카드에 */
    .st-key-discovery_panel{overflow:hidden;border:1px solid #EAEAEA;border-radius:28px;background:#fff;padding:0 0 1rem!important}
    .st-key-discovery_panel>div{gap:.55rem!important}
    .discovery-visual{
      height:360px;background:linear-gradient(135deg,#EAE7E2 0%,#D8DBDE 100%);
      display:flex;align-items:center;justify-content:center;border-radius:27px 27px 0 0
    }
    .image-note{font-size:11px;color:#919191;font-weight:850;letter-spacing:.14em}
    .discovery-copy{padding:1.2rem 1.35rem .65rem}
    .banner-title{font-size:31px;line-height:1.13;letter-spacing:-.045em;font-weight:850;margin:.18rem 0 .55rem}
    .banner-sub{color:#777;font-size:13px}
    .st-key-discovery_panel .stButton{padding-left:1.25rem;padding-right:1.25rem}
    .st-key-discovery_panel .stButton>button[kind='primary']{min-height:46px}

    .section-gap{height:2.5rem}.section-gap-sm{height:1.5rem}
    .section-title-row{margin:1.7rem 0 1rem}
    .section-title-main{font-size:25px;font-weight:850;letter-spacing:-.035em}
    .section-title-sub{color:#8B8B8B;font-size:12px;margin-top:.18rem}

    /* 상품 카드 */
    .product-card{border:1px solid #ECECEC;border-radius:20px;overflow:hidden;background:#fff;margin-bottom:.35rem}
    .product-image{height:245px;background:linear-gradient(135deg,#EFECE7,#DDE1E4);display:flex;align-items:center;justify-content:center}
    .product-image span{color:#989898;font-size:10px;font-weight:850;letter-spacing:.09em}
    .product-copy{padding:.9rem 1rem 1.05rem}
    .product-brand{font-size:10px;color:#8A8A8A;font-weight:750;margin-bottom:.22rem}
    .product-name{font-size:14px;font-weight:850;line-height:1.35;min-height:38px}
    .product-price{font-size:16px;font-weight:900;margin-top:.42rem}
    .product-meta{font-size:10px;color:#8A8A8A;margin-top:.38rem}
    .badge{display:inline-block;font-size:9px;font-weight:850;color:#fff;background:var(--ff-red);padding:3px 7px;border-radius:999px;margin-bottom:.45rem}

    /* '상품 보기' 큰 버튼 제거 → 링크형 */
    [class*='st-key-product_'] .stButton>button{
      border:none!important;background:transparent!important;border-radius:0!important;box-shadow:none!important;
      min-height:28px!important;padding:.05rem .1rem!important;font-size:11px!important;color:#555!important;justify-content:flex-start!important
    }
    [class*='st-key-product_'] .stButton>button:hover{color:var(--ff-red)!important}

    .search-summary{background:#FAFAFA;border-radius:18px;padding:1rem 1.15rem;margin:1rem 0 1.4rem}
    .result-title{font-size:17px;font-weight:750}
    .chip-row{margin-top:.7rem;display:flex;flex-wrap:wrap;gap:7px}
    .filter-chip{background:#FFF0F2;border:1px solid #F2B6BF;color:#C92D45;font-size:11px;font-weight:850;padding:6px 10px;border-radius:999px}
    .filter-title{font-size:16px;font-weight:850;margin-bottom:.9rem}
    .filter-count{background:#F7F3EB;padding:.8rem 1rem;border-radius:14px;margin-top:1rem;font-size:13px}
    .product-count{font-size:16px;font-weight:850;padding-top:.5rem}
    .empty-box{border:1px dashed #D9D9D9;border-radius:20px;padding:3rem;text-align:center}
    .empty-title{font-size:17px;font-weight:850}.muted{color:#888;font-size:12px;margin-top:.35rem}

    .brand-index{line-height:2.1;color:#555;border-top:1px solid #EEE;border-bottom:1px solid #EEE;padding:1rem 0;margin-bottom:1.5rem}
    .brand-card{border:1px solid #ECECEC;border-radius:18px;padding:1.2rem;min-height:125px;margin-bottom:.5rem}
    .brand-card-name{font-size:18px;font-weight:850}.brand-card-desc,.brand-desc{color:#777;font-size:12px;margin-top:.45rem;line-height:1.55}

    .product-image-tall{height:610px;border-radius:24px;background:linear-gradient(135deg,#EFECE7,#D9DDE1);display:flex;align-items:center;justify-content:center;color:#989898;font-size:12px;font-weight:850;letter-spacing:.1em}
    .detail-title{font-size:34px;line-height:1.2;letter-spacing:-.04em;margin:.35rem 0 .7rem}.detail-price{font-size:24px;font-weight:900;margin-bottom:1.25rem}
    .match-label{color:var(--ff-red);font-size:11px;font-weight:900;letter-spacing:.08em;margin-top:1.5rem}
    .why-box{background:var(--ff-blue);border-radius:18px;padding:1rem 1.1rem;margin:1.1rem 0 1rem}
    .why-title{color:#3565BC;font-size:12px;font-weight:900;margin-bottom:.35rem}.why-copy{font-size:13px;line-height:1.6;color:#3E4652}

    @media(max-width:900px){
      .block-container{padding-left:1rem;padding-right:1rem;padding-top:.5rem}
      .st-key-topnav [data-testid='column']:not(:first-child){display:none}
      .hero-title{font-size:42px}.page-title{font-size:30px}
      .st-key-finder_console{padding:1.2rem 1rem;border-radius:22px}
      .live-number{font-size:38px}
      .discovery-visual{height:280px}.banner-title{font-size:26px}
      .product-image{height:190px}.product-image-tall{height:430px}
    }
    </style>""",unsafe_allow_html=True)


def section_title(title,subtitle=''):
    import streamlit as st
    st.markdown(
        f"<div class='section-title-row'><div class='section-title-main'>{html.escape(str(title))}</div><div class='section-title-sub'>{html.escape(str(subtitle))}</div></div>",
        unsafe_allow_html=True
    )


def product_card_html(row):
    badge=str(row.get('badge','') or '')
    bh=f"<div class='badge'>{html.escape(badge)}</div>" if badge else ''
    max_size=float(row.get('max_size',0))
    size_label=f"{int(max_size)}까지" if max_size>0 else 'FREE'
    concern_raw=str(row.get('body_concerns','') or '')
    concern=concern_raw.split('|')[0] if concern_raw else '편안한 핏'
    return (
        f"<div class='product-card'><div class='product-image'><span>PRODUCT IMAGE</span></div>"
        f"<div class='product-copy'>{bh}<div class='product-brand'>{html.escape(str(row.get('brand','')))}</div>"
        f"<div class='product-name'>{html.escape(str(row.get('name','')))}</div>"
        f"<div class='product-price'>{int(row.get('price',0)):,}원</div>"
        f"<div class='product-meta'>♡ {html.escape(size_label)} · {html.escape(concern)}</div></div></div>"
    )


def brand_card_html(row):
    return (
        f"<div class='brand-card'><div class='brand-card-name'>{html.escape(str(row.get('brand','')))}</div>"
        f"<div class='brand-card-desc'>{html.escape(str(row.get('description','')))}</div></div>"
    )


def placeholder_image(label='IMAGE',tall=False):
    return f"<div class='{'product-image-tall' if tall else 'product-image'}'>{html.escape(label)}</div>"
