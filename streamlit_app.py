import streamlit as st
import os

# --- 1. 自動安裝 Gemini 套件 ---
try:
    import google.generativeai as genai
except ImportError:
    os.system('pip install google-generativeai')
    import google.generativeai as genai

# --- 2. 硬編碼您圖片中的最新 API Key ---
GEMINI_API_KEY = "AQ.Ab8RN6K5eZ-WJT-ZqH6U8efmO-oYpI-V-fVn4" # 請確認這串跟您圖片中的一模一樣
genai.configure(api_key=GEMINI_API_KEY)

# --- 3. 核心法律專家指令設定 ---
SYSTEM_PROMPT = """你是一位精通中華民國（台灣）法律體系的「法律工作台 AI 專家」。
你的原則：絕對嚴謹、事實導向、嚴禁瞎編。
輸出格式必須嚴格遵守：
#### 一、 核心爭點與法理分析
- [爭點描述與相關法條引用]
#### 二、 實務見解與判決比對
- [最高法院主流見解，若不確定字號請標註需查核司法院系統]
#### 三、 具體建議與風險評估
- [修訂建議條文與勝訴/敗訴風險分析]
"""

# --- 4. 頁面配置與專業 UI ---
st.set_page_config(page_title="強棒法律工作台", page_icon="⚖️", layout="centered")

if 'active_page' not in st.session_state: st.session_state.active_page = '合約審查'
if 'selected_tag' not in st.session_state: st.session_state.selected_tag = '租賃合約'

st.markdown(f"""
    <style>
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{ background-color: #FDFDFD; }}
    .header-text {{ font-size: 32px; font-weight: 800; color: #1A1A1A; margin-top: -60px; }}
    .subtitle-text {{ font-size: 16px; color: #8E8E8E; margin-bottom: 25px; }}
    .section-label {{ font-size: 16px; font-weight: 600; color: #4A4A4A; margin-top: 15px; }}
    .stButton > button {{ border-radius: 25px; border: 1px solid #E0E0E0; background-color: white; color: #4A4A4A; transition: 0.3s; font-size: 14px; }}
    .main-action-btn button {{ background-color: #1E293B !important; color: white !important; width: 100%; height: 60px; font-size: 20px; font-weight: 700; border-radius: 12px; border: none; margin-top: 20px; }}
    .nav-wrapper {{ position: fixed; bottom: 0; left: 0; width: 100%; height: 85px; background-color: #1E293B; display: flex; align-items: center; z-index: 9999; }}
    .nav-btn-box {{ flex: 1; text-align: center; }}
    .nav-btn-box button {{ background: none !important; border: none !important; color: #94A3B8 !important; font-size: 12px !important; }}
    .active-nav button {{ color: white !important; font-weight: bold !important; border-top: 3px solid #E11D48 !important; border-radius: 0 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. 呼叫 AI 邏輯 ---
def call_ai(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=SYSTEM_PROMPT)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ 分析失敗。請檢查 API Key 是否正確。錯誤資訊：{str(e)}"

# --- 6. 頁面內容 (合約審查) ---
if st.session_state.active_page == '合約審查':
    st.markdown('<div class="header-text">合約審查</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">逐條掃描風險條款，提供修訂建議</div>', unsafe_allow_html=True)
    
    tags1 = st.columns(3)
    if tags1[0].button("租賃合約"): st.session_state.selected_tag = "租賃合約"
    if tags1[1].button("買賣合約"): st.session_state.selected_tag = "買賣合約"
    if tags1[2].button("雇傭合約"): st.session_state.selected_tag = "雇傭合約"
    
    st.markdown(f'<div class="section-label">合約內容 (模式：{st.session_state.selected_tag})</div>', unsafe_allow_html=True)
    user_input = st.text_area("input", placeholder="請貼上合約條文...", height=300, label_visibility="collapsed")

    st.markdown('<div class="main-action-btn">', unsafe_allow_html=True)
    if st.button("開始審查"):
        if user_input:
            with st.spinner("⚖️ 正在調用 Gemini 法律專家進行審查..."):
                res = call_ai(f"請審查這份【{st.session_state.selected_tag}】並產出專業報告：\n\n{user_input}")
                st.markdown(f'<div style="background-color:white; padding:20px; border-radius:12px; border-left:6px solid #E11D48; margin-top:20px;">{res}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. 底部導覽列 ---
st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
nav_bar = st.container()
with nav_bar:
    st.markdown('<div class="nav-wrapper">', unsafe_allow_html=True)
    cols = st.columns(4)
    pages = ['合約審查', '案情分析', '法條檢索', '歷史記錄']
    icons = ['📝\n合約審查', '📊\n案情分析', '🔍\n法條檢索', '⏳\n歷史記錄']
    for i, p in enumerate(pages):
        with cols[i]:
            cls = "active-nav" if st.session_state.active_page == p else "nav-btn-box"
            st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
            if st.button(icons[i], key=f"nav_{p}"):
                st.session_state.active_page = p
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
