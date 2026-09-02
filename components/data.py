from pathlib import Path
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]; DATA_DIR=ROOT/'data'
LIVE_PRODUCT_COUNT=28796
LIVE_BRAND_COUNT=271
@st.cache_data
def load_products(): return pd.read_csv(DATA_DIR/'products.csv',encoding='utf-8-sig')
@st.cache_data
def load_brands(): return pd.read_csv(DATA_DIR/'brands.csv',encoding='utf-8-sig')
