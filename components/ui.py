import base64
import html
import mimetypes
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]


def asset_uri(relative_path):
    path = ROOT / relative_path
    if not path.exists():
        return None
    mime, _ = mimetypes.guess_type(path.name)
    mime = mime or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def qurl(query, page="search"):
    return f"?page={quote_plus(page)}&q={quote_plus(query)}"


def nav_url(page, value=None):
    if page == "category" and value:
        return f"?page=category&category={quote_plus(value)}"
    if page == "search" and value:
        return qurl(value)
    return f"?page={quote_plus(page)}"


def inject_css():
    import streamlit as st
    st.markdown(r"""
<style>
:root{
  --ff-ink:#171717;--ff-gray:#777;--ff-line:#e8e8e8;--ff-beige:#f8f3e9;
  --ff-red:#9a1e2b;--ff-green:#2aa36b;--ff-yellow:#e9e313;--ff-blue:#eef4ff;
}
*{box-sizing:border-box;font-family:Pretendard,"Noto Sans KR",Arial,sans-serif}
html,body,[data-testid="stAppViewContainer"],.stApp{background:#fff;color:var(--ff-ink)}
header[data-testid="stHeader"],[data-testid="stSidebar"],[data-testid="stSidebarCollapsedControl"]{display:none!important}
.block-container{max-width:1240px!important;padding:18px 22px 60px!important}

/* ---------- exact header ---------- */
.ff-header{width:1170px;max-width:100%;margin:0 auto 28px}
.ff-head-row{height:70px;display:grid;grid-template-columns:242px 1fr 92px;align-items:center;border-bottom:1px solid var(--ff-line)}
.ff-bi{display:block;width:242px;height:50px;object-fit:contain;object-position:left center}
.ff-nav{display:flex;align-items:center;justify-content:center;gap:38px;white-space:nowrap}
.ff-nav a,.ff-utils a{color:#222;text-decoration:none;font-size:12px;font-weight:600;transition:.15s}
.ff-nav a:hover,.ff-utils a:hover{color:#9a1e2b}
.ff-utils{display:flex;justify-content:flex-end;align-items:center;gap:24px}
.ff-utils .heart{font-size:18px;font-weight:400}.ff-utils .bag{font-size:10px;font-weight:800;letter-spacing:.04em}

/* ---------- target hero: left discovery / right finder ---------- */
.ff-hero{width:1170px;max-width:100%;margin:0 auto;display:grid;grid-template-columns:476fr 654fr;gap:40px;align-items:start}
.ff-discovery,.ff-finder-side{height:590px}
.ff-discovery{display:flex;flex-direction:column;background:#fff}
.ff-hero-image{height:364px;flex:0 0 364px;background:#e6e3dd center/cover no-repeat}
.ff-discovery-copy{height:178px;flex:0 0 178px;padding:21px 24px 12px}
.ff-eyebrow{font-size:11px;font-weight:850;letter-spacing:.08em;color:#4e4e4e;margin-bottom:13px}
.ff-discovery-title{font-size:29px;line-height:1.12;font-weight:900;letter-spacing:-.048em;margin:0 0 13px}
.ff-discovery-sub{font-size:11px;color:#777}
.ff-discovery-cta{height:48px;flex:0 0 48px;margin:0 24px;border-radius:999px;background:#1c1c1c;color:#fff;text-decoration:none;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800}
.ff-discovery-cta strong{color:var(--ff-yellow);font-size:17px;margin:0 4px}

.ff-finder-side{display:flex;flex-direction:column}
.ff-finder-card{height:362px;flex:0 0 362px;border:1px solid #e9e9e9;border-radius:27px;padding:22px 24px 16px;background:#fff;box-shadow:0 7px 22px rgba(0,0,0,.012);display:flex;flex-direction:column;justify-content:flex-start;box-sizing:border-box;overflow:hidden}
.ff-finder-top{transform:translateY(-21px)}
.ff-finder-title{font-size:43px;line-height:1.04;font-weight:900;letter-spacing:-.06em;margin:0 0 14px}
.ff-search-form{display:grid;grid-template-columns:1fr 67px;gap:12px;margin:0 0 2px 0}
.ff-search-input{width:100%;height:42px;border:0;outline:0;background:#f1f2f5;border-radius:5px;padding:0 15px;color:#333;font-size:12px}
.ff-search-input::placeholder{color:#a1a1a1}
.ff-search-submit{height:42px;border:0;border-radius:999px;background:#1c1c1c;color:#fff;font-size:12px;font-weight:800;cursor:pointer}
.ff-helper{font-size:10px;font-weight:750;color:#777;margin:18px 0 7px}
.ff-examples{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px}
.ff-example{height:23px;border-radius:3px;background:#f4f4f5;color:#343434;text-decoration:none;display:flex;align-items:center;justify-content:center;padding:0 9px;font-size:9.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;cursor:default}
.ff-example:hover{background:#f4f4f5;color:#343434;text-decoration:none}
.ff-live{height:86px;margin-top:auto;background:var(--ff-beige);border-radius:18px;padding:11px 16px 10px}
.ff-live-top{display:flex;justify-content:space-between;align-items:center;font-size:9px;font-weight:850;line-height:1}
.ff-live-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--ff-green);margin-right:7px}
.ff-live-time{font-size:11px;font-weight:850}
.ff-live-row{display:grid;grid-template-columns:1.2fr 1.7fr .82fr;gap:8px;align-items:end;margin-top:7px}
.ff-live-copy{font-size:11px;font-weight:800;letter-spacing:-.025em}
.ff-live-number{display:flex;align-items:baseline;justify-content:center;gap:5px}
.ff-live-number .prefix{font-size:9px;color:#777;font-weight:700}
.ff-live-number b{font-size:36px;line-height:1;font-weight:900;color:var(--ff-red);letter-spacing:-.055em}
.ff-live-number .unit{font-size:10px;font-weight:850}
.ff-live-brand{text-align:right;font-size:10px;font-weight:850}

.ff-quick{height:204px;flex:0 0 204px;padding-top:22px}
.ff-quick-title{font-size:27px;line-height:1.05;font-weight:900;letter-spacing:-.05em;margin:0 0 14px 4px}
.ff-quick-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.ff-quick-item{display:flex;flex-direction:column;align-items:center;text-decoration:none;color:#222;min-width:0}
.ff-quick-img{width:104px;height:104px;border-radius:50%;background:#e1dfda center/cover no-repeat;display:block}
.ff-quick-label{margin-top:10px;font-size:11px;font-weight:750;white-space:nowrap;text-align:center}

/* Floating toolbar copied from target */
.ff-floating{position:fixed;right:14px;top:484px;width:80px;height:auto;z-index:60;pointer-events:none}

/* ---------- below the requested top area ---------- */
.section-gap{height:2.2rem}.section-title-row{margin:1.5rem auto .9rem;max-width:1170px}.section-title-main{font-size:25px;font-weight:900;letter-spacing:-.04em}.section-title-sub{color:#888;font-size:12px;margin-top:.15rem}
.stButton>button{border-radius:999px;border:1px solid #e4e4e4;background:#fff;color:#252525;font-weight:650;min-height:38px}.stButton>button:hover{border-color:#cacaca;color:#9a1e2b}.stButton>button[kind="primary"]{background:#1b1b1b;color:#fff;border-color:#1b1b1b}
.page-title{font-size:38px;line-height:1.15;letter-spacing:-.04em;margin:.1rem 0 1.3rem}.eyebrow{font-size:11px;font-weight:850;letter-spacing:.08em;color:#555;margin-bottom:.65rem}.eyebrow.red{color:#e54456}
div[data-baseweb="input"]>div{min-height:44px!important;border-radius:5px!important;background:#f1f2f5!important;border-color:#f1f2f5!important}
.product-card{border:1px solid #ececec;border-radius:18px;overflow:hidden;background:#fff;margin-bottom:.35rem}.product-image{height:245px;background:linear-gradient(135deg,#efece7,#dde1e4);background-size:cover;background-position:center;display:flex;align-items:center;justify-content:center}.product-image span{color:#989898;font-size:10px;font-weight:850;letter-spacing:.09em}.product-copy{padding:.9rem 1rem 1rem}.product-brand{font-size:10px;color:#888;font-weight:750;margin-bottom:.2rem}.product-name{font-size:14px;line-height:1.35;font-weight:850;min-height:38px}.product-price{font-size:16px;font-weight:900;margin-top:.4rem}.product-meta{font-size:10px;color:#8a8a8a;margin-top:.35rem}.badge{display:inline-block;font-size:9px;font-weight:850;color:#fff;background:#e54456;padding:3px 7px;border-radius:999px;margin-bottom:.42rem}[class*="st-key-product_"] .stButton>button{border:none!important;background:transparent!important;border-radius:0!important;min-height:26px!important;padding:.05rem .1rem!important;font-size:11px!important;color:#555!important;justify-content:flex-start!important}
.search-summary{background:#fafafa;border-radius:18px;padding:1rem 1.15rem;margin:1rem 0 1.4rem}.result-title{font-size:17px;font-weight:750}.chip-row{margin-top:.7rem;display:flex;flex-wrap:wrap;gap:7px}.filter-chip{background:#fff0f2;border:1px solid #f2b6bf;color:#c92d45;font-size:11px;font-weight:850;padding:6px 10px;border-radius:999px}.filter-title{font-size:16px;font-weight:850;margin-bottom:.9rem}.filter-count{background:#f8f3e9;padding:.8rem 1rem;border-radius:14px;margin-top:1rem;font-size:13px}.empty-box{border:1px dashed #d9d9d9;border-radius:20px;padding:3rem;text-align:center}.empty-title{font-size:17px;font-weight:850}.muted{color:#888;font-size:12px;margin-top:.35rem}.brand-index{line-height:2.1;color:#555;border-top:1px solid #eee;border-bottom:1px solid #eee;padding:1rem 0;margin-bottom:1.5rem}.brand-card{border:1px solid #ececec;border-radius:18px;padding:1.2rem;min-height:125px;margin-bottom:.5rem}.brand-card-name{font-size:18px;font-weight:850}.brand-card-desc,.brand-desc{color:#777;font-size:12px;margin-top:.45rem;line-height:1.55}.product-image-tall{height:610px;border-radius:24px;background:linear-gradient(135deg,#efece7,#d9dde1);background-size:cover;background-position:center;display:flex;align-items:center;justify-content:center}.detail-title{font-size:34px;line-height:1.2;letter-spacing:-.04em;margin:.35rem 0 .7rem}.detail-price{font-size:24px;font-weight:900;margin-bottom:1.25rem}.match-label{color:#e54456;font-size:11px;font-weight:900;letter-spacing:.08em;margin-top:1.5rem}.why-box{background:#eef4ff;border-radius:18px;padding:1rem 1.1rem;margin:1.1rem 0 1rem}.why-title{color:#3565bc;font-size:12px;font-weight:900;margin-bottom:.35rem}.why-copy{font-size:13px;line-height:1.6;color:#3e4652}

@media(max-width:1000px){
 .block-container{padding:14px 18px 50px!important}.ff-header,.ff-hero{width:100%}.ff-head-row{grid-template-columns:205px 1fr 68px}.ff-bi{width:205px;height:auto}.ff-nav{gap:18px}.ff-nav a{font-size:10px}.ff-hero{grid-template-columns:42fr 58fr;gap:24px}.ff-discovery,.ff-finder-side{height:555px}.ff-hero-image{height:335px;flex-basis:335px}.ff-discovery-copy{height:172px;flex-basis:172px;padding:18px 18px 10px}.ff-discovery-cta{margin:0 18px}.ff-finder-card{height:348px;flex-basis:348px;padding:20px 22px 14px}.ff-finder-top{transform:translateY(-18px)}.ff-finder-title{font-size:36px;margin-bottom:12px}.ff-helper{margin:14px 0 6px}.ff-example{font-size:9px;height:22px}.ff-live{height:84px;margin-top:auto;padding:10px 14px 9px}.ff-live-row{margin-top:6px}.ff-live-number b{font-size:33px}.ff-quick{height:207px;flex-basis:207px;padding-top:18px}.ff-quick-img{width:82px;height:82px}.ff-quick-label{font-size:9px}.ff-floating{display:none}
}
@media(max-width:760px){
 .ff-head-row{height:62px;grid-template-columns:1fr 68px}.ff-nav{display:none}.ff-bi{width:220px}.ff-hero{display:flex;flex-direction:column}.ff-finder-side{order:1;height:auto}.ff-discovery{order:2;height:auto}.ff-finder-card{height:auto;min-height:350px;padding:18px 18px 14px}.ff-finder-top{transform:translateY(-8px)}.ff-finder-title{font-size:34px;margin-bottom:12px}.ff-helper{margin:14px 0 6px}.ff-examples{grid-template-columns:1fr}.ff-live{height:auto;margin-top:16px}.ff-live-row{grid-template-columns:1fr;gap:5px}.ff-live-number{justify-content:flex-start}.ff-live-brand{text-align:left}.ff-quick{height:auto;padding-top:16px;padding-bottom:20px}.ff-quick-grid{grid-template-columns:repeat(5,1fr);gap:8px}.ff-quick-img{width:64px;height:64px}.ff-quick-label{font-size:8px}.ff-hero-image{height:auto;aspect-ratio:1.307/1;flex-basis:auto}.ff-discovery-copy{height:auto;flex-basis:auto}.ff-discovery-cta{margin-bottom:14px}
}
</style>
""", unsafe_allow_html=True)


def section_title(title, subtitle=""):
    import streamlit as st
    st.markdown(f"<div class='section-title-row'><div class='section-title-main'>{html.escape(str(title))}</div><div class='section-title-sub'>{html.escape(str(subtitle))}</div></div>", unsafe_allow_html=True)


def product_card_html(row):
    badge = str(row.get("badge", "") or "")
    badge_html = f"<div class='badge'>{html.escape(badge)}</div>" if badge else ""
    max_size = float(row.get("max_size", 0)); size_label = f"{int(max_size)}까지" if max_size > 0 else "FREE"
    concern_raw = str(row.get("body_concerns", "") or ""); concern = concern_raw.split("|")[0] if concern_raw else "편안한 핏"
    uri = asset_uri(f"assets/products/{row.get('product_id')}.jpg")
    img_style = f"style=\"background-image:url('{uri}')\"" if uri else ""
    inner = "" if uri else "<span>PRODUCT IMAGE</span>"
    return f"<div class='product-card'><div class='product-image' {img_style}>{inner}</div><div class='product-copy'>{badge_html}<div class='product-brand'>{html.escape(str(row.get('brand','')))}</div><div class='product-name'>{html.escape(str(row.get('name','')))}</div><div class='product-price'>{int(row.get('price',0)):,}원</div><div class='product-meta'>♡ {html.escape(size_label)} · {html.escape(concern)}</div></div></div>"


def brand_card_html(row):
    return f"<div class='brand-card'><div class='brand-card-name'>{html.escape(str(row.get('brand','')))}</div><div class='brand-card-desc'>{html.escape(str(row.get('description','')))}</div></div>"


def asset_image_html(relative_path, fallback_label="IMAGE", class_name="product-image-tall"):
    uri = asset_uri(relative_path)
    if uri:
        return f"<div class='{class_name}' style=\"background-image:url('{uri}')\"></div>"
    return f"<div class='{class_name}'><span>{html.escape(fallback_label)}</span></div>"
