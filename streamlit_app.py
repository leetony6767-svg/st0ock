
import streamlit as st

# --- 1. 頁面初始化與狀態管理 ---
st.set_page_config(page_title="強棒法律工作台", page_icon="⚖️", layout="centered")

# 初始化頁面狀態，確保切換功能正常
if 'page' not in st.session_state:
    st.session_state.page = '合約審查'
if 'contract_type' not in st.session_state:
    st.session_state.contract_type = None

# --- 2. 專業手機版 CSS 樣式 ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #F9F8F4; }
    
    /* 標題區樣式 */
    .app-header { font-size: 28px; font-weight: 800; color: #1A1A1A; margin-top: -50px; margin-bottom: 5px; }
    .app-subtitle { font-size: 14px; color: #8E8E8E; margin-bottom: 20px; }
    
    /* 按鈕樣式優化 */
    .stButton > button {
        border-radius: 12px; border: 1px solid #E0E0E0; background-color: white; 
        color: #4A4A4A; width: 100%; height: 45px; transition: 0.3s; font-weight: 500;
    }
    /* 底部導覽按鈕樣式 */
    .nav-col .stButton > button {
        background-color: transparent !important; border: none !important; color: #94A3B8 !important; height: 60px; font-size: 12px;
    }
    .nav-col-active .stButton > button {
        background-color: transparent !important; border: none !important; color: white !important; height: 60px; font-size: 12px; font-weight: bold;
    }
    
    /* 開始審查大按鈕 */
    .action-btn .stButton > button {
        background-color: #1E293B !important; color: white !important; height: 55px; font-size: 18px; font-weight: 700; border: none; margin-top: 20px;
    }

    /* 底部導覽列背景 */
    .nav-container {
        position: fixed; bottom: 0; left: 0; width: 100%; height: 80px; 
        background-color: #1E293B; z-index: 1000; display: flex; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 底部導覽功能邏輯 ---
# 這裡用 Streamlit 的 columns 來模擬可點擊的導覽列
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True) # 墊片
nav_placeholder = st.container()

with nav_placeholder:
    st.markdown('<div class="nav-container"></div>', unsafe_allow_html=True)
    cols = st.columns(4)
    with cols[0]:
        if st.button("📝\n合約審查"): st.session_state.page = '合約審查'
    with cols[1]:
        if st.button("📊\n案情分析"): st.session_state.page = '案情分析'
    with cols[2]:
        if st.button("🔍\n法條檢索"): st.session_state.page = '法條檢索'
    with cols[3]:
        if st.button("⏳\n歷史記錄"): st.session_state.page = '歷史記錄'

# --- 4. 根據分頁顯示內容 ---
if st.session_state.page == '合約審查':
    st.markdown('<div class="app-header">合約審查</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">逐條掃描風險條款，提供修訂建議</div>', unsafe_allow_html=True)

    # 合約類型選擇 (橫向排列)
    row1_cols = st.columns(3)
    if row1_cols[0].button("租賃合約"): st.session_state.contract_type = "租賃合約"
    if row1_cols[1].button("買賣合約"): st.session_state.contract_type = "買賣合約"
    if row1_cols[2].button("雇傭合約"): st.session_state.contract_type = "雇傭合約"

    row2_cols = st.columns(3)
    if row2_cols[0].button("服務合約"): st.session_state.contract_type = "服務合約"
    if row2_cols[1].button("保密協議"): st.session_state.contract_type = "保密協議"
    if row2_cols[2].button("其他類型"): st.session_state.contract_type = "其他"

    if st.session_state.contract_type:
        st.caption(f"當前模式：{st.session_state.contract_type}")

    # 輸入區
    st.markdown("<br><b>合約內容</b>", unsafe_allow_html=True)
    user_text = st.text_area("input", placeholder="請貼上合約條文全文...", height=250, label_visibility="collapsed")

    # 執行按鈕
    st.markdown('<div class="action-btn">', unsafe_allow_html=True)
    if st.button("開始審查"):
        if user_text:
            with st.spinner("AI 律師正在分析中..."):
                st.success(f"【{st.session_state.contract_type or '一般'}】風險分析完成")
                st.markdown("""
                    <div style="background-color:white; padding:20px; border-radius:12px; border-left:6px solid #1E293B;">
                    <b>🔍 偵測到 2 處法律風險：</b><br>
                    1. 違約金條款顯失公平。<br>
                    2. 終止契約條件模糊。
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("請先輸入內容。")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == '案情分析':
    st.markdown('<div class="app-header">案情分析</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">梳理法律事實，找出核心爭點</div>', unsafe_allow_html=True)
    st.text_area("請描述案情事實經過：", height=300)
    st.markdown('<div class="action-btn">', unsafe_allow_html=True)
    st.button("產出分析報告")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == '法條檢索':
    st.markdown('<div class="app-header">法條檢索</div>', unsafe_allow_html=True)
    st.text_input("輸入關鍵字 (如：勞基法 加班費)：")
    st.markdown('<div class="action-btn">', unsafe_allow_html=True)
    st.button("搜尋法條")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == '歷史記錄':
    st.markdown('<div class="app-header">歷史記錄</div>', unsafe_allow_html=True)
    st.write("目前尚無儲存的紀錄。")

# 墊高底部，避免內容被導覽列遮住
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
