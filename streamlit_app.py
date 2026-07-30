
import streamlit as st

# 1. 頁面基礎設定
st.set_page_config(page_title="強棒法律工作台", page_icon="⚖️", layout="centered")

# 2. 專業 App 介面 CSS (跟圖片一模一樣)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #F9F8F4; }
    .main-title { font-size: 28px; font-weight: 800; color: #1A1A1A; margin-top: -60px; }
    .sub-title { font-size: 14px; color: #8E8E8E; margin-bottom: 20px; }
    .stButton > button {
        border-radius: 20px; border: 1px solid #E0E0E0; background-color: white; color: #4A4A4A; width: 100%; transition: 0.3s;
    }
    .stButton > button:hover { background-color: #F0F0F0; border-color: #BBB; }
    div.stButton > button:first-child {
        background-color: #1E293B !important; color: white !important;
        width: 100%; height: 55px; font-size: 18px; font-weight: 700; border-radius: 12px; margin-top: 20px; border: none;
    }
    .stTextArea textarea { background-color: white !important; border-radius: 12px !important; border: 1px solid #E0E0E0 !important; padding: 15px !important; }
    .nav-bar {
        position: fixed; bottom: 0; left: 0; width: 100%; height: 75px; background-color: #1E293B;
        display: flex; justify-content: space-around; align-items: center; z-index: 1000; padding-bottom: 10px;
    }
    .nav-item { color: #94A3B8; text-align: center; font-size: 11px; font-weight: 500; cursor: pointer; }
    .nav-item.active { color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. 標題區
st.markdown('<div class="main-title">合約審查</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">逐條掃描風險條款，提供修訂建議</div>', unsafe_allow_html=True)

# 4. 合約標籤 (Pills)
c1, c2, c3 = st.columns(3)
with c1: st.button("租賃合約")
with c2: st.button("買賣合約")
with c3: st.button("雇傭合約")
c4, c5, c6 = st.columns(3)
with c4: st.button("服務合約")
with c5: st.button("保密協議")
with c6: st.button("股權投資")

# 5. 輸入框
st.markdown("<br><b>合約內容</b>", unsafe_allow_html=True)
contract_input = st.text_area(label="input", placeholder="請貼上合約條文全文，或欲審查的重點條款...", height=250, label_visibility="collapsed")

# 6. 執行按鈕
if st.button("開始審查"):
    if contract_input:
        st.info("⚖️ 強棒法律 AI 正在為您逐條掃描風險，請稍候...")
        st.markdown("""<div style="background-color:white; padding:20px; border-radius:12px; border-left:6px solid #1E293B; margin-top:20px;"><b>掃描完成：發現 2 項法律風險</b><br>1. 違約金高於市價 (民法 252 條)<br>2. 管轄法院不利於使用者</div>""", unsafe_allow_html=True)
    else:
        st.warning("請先貼入合約文字。")

# 7. 底部導覽列
st.markdown("""
    <div style="height: 100px;"></div>
    <div class="nav-bar">
        <div class="nav-item active">📝<br>合約審查</div>
        <div class="nav-item">📊<br>案情分析</div>
        <div class="nav-item">🔍<br>法條檢索</div>
        <div class="nav-item">⏳<br>歷史記錄</div>
    </div>
    """, unsafe_allow_html=True)
