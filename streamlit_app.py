
import streamlit as st

# --- 1. 頁面基礎設定 (隱藏原生組件) ---
st.set_page_config(page_title="強棒法律工作台", page_icon="⚖️", layout="centered")

# --- 2. 狀態管理 (紀錄當前分頁與選取的標籤) ---
if 'active_page' not in st.session_state:
    st.session_state.active_page = '合約審查'
if 'selected_tag' not in st.session_state:
    st.session_state.selected_tag = '租賃合約'

# --- 3. 完美還原截圖的 CSS ---
st.markdown(f"""
    <style>
    /* 隱藏上方導覽列與頁尾 */
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{ background-color: #FDFDFD; }}

    /* 頂部文字樣式 */
    .header-text {{ font-size: 32px; font-weight: 800; color: #1A1A1A; margin-top: -60px; }}
    .subtitle-text {{ font-size: 16px; color: #8E8E8E; margin-bottom: 25px; }}
    .section-label {{ font-size: 16px; font-weight: 600; color: #4A4A4A; margin-bottom: 10px; margin-top: 15px; }}

    /* 合約標籤(Pills)樣式 */
    .stButton > button {{
        border-radius: 25px; border: 1px solid #E0E0E0; background-color: white; 
        color: #4A4A4A; padding: 5px 20px; font-size: 15px; transition: 0.3s;
    }}
    /* 被選中標籤的樣式 (深色) */
    div[data-testid="stHorizontalBlock"] button[kind="secondary"]:active, 
    div[data-testid="stHorizontalBlock"] button:focus {{
        background-color: #1E293B !important; color: white !important; border-color: #1E293B !important;
    }}

    /* 開始審查大按鈕 */
    .main-action-btn button {{
        background-color: #1E293B !important; color: white !important;
        width: 100%; height: 60px; font-size: 20px; font-weight: 700; 
        border-radius: 12px; border: none; margin-top: 20px;
    }}

    /* 底部導覽列樣式 */
    .nav-wrapper {{
        position: fixed; bottom: 0; left: 0; width: 100%; height: 85px;
        background-color: #1E293B; display: flex; align-items: center; z-index: 9999;
    }}
    .nav-btn-box {{ flex: 1; text-align: center; }}
    .nav-btn-box button {{
        background: none !important; border: none !important; color: #94A3B8 !important;
        font-size: 12px !important; line-height: 1.5; padding: 10px 0;
    }}
    .active-nav button {{ color: white !important; font-weight: bold !important; border-top: 3px solid #E11D48 !important; border-radius: 0 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 頂部頁面內容切換邏輯 ---
if st.session_state.active_page == '合約審查':
    st.markdown('<div class="header-text">合約審查</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">逐條掃描風險條款，提供修訂建議</div>', unsafe_allow_html=True)

    # 合約類型選擇區
    st.markdown('<div class="section-label">合約類型</div>', unsafe_allow_html=True)
    
    # 用兩行排列按鈕
    tags1 = st.columns(3)
    if tags1[0].button("租賃合約"): st.session_state.selected_tag = "租賃合約"
    if tags1[1].button("買賣合約"): st.session_state.selected_tag = "買賣合約"
    if tags1[2].button("雇傭合約"): st.session_state.selected_tag = "雇傭合約"
    
    tags2 = st.columns(3)
    if tags2[0].button("服務合約"): st.session_state.selected_tag = "服務合約"
    if tags2[1].button("保密協議(NDA)"): st.session_state.selected_tag = "保密協議"
    if tags2[2].button("股權投資協助"): st.session_state.selected_tag = "股權投資"
    
    tags3 = st.columns(2)
    if tags3[0].button("承攬合約"): st.session_state.selected_tag = "承攬合約"
    if tags3[1].button("其他"): st.session_state.selected_tag = "其他"

    # 合約內容輸入區
    st.markdown(f'<div class="section-label">合約內容 <span style="font-weight:normal; font-size:12px; color:#8E8E8E;">(當前模式：{st.session_state.selected_tag})</span></div>', unsafe_allow_html=True)
    user_input = st.text_area("input", placeholder="請貼上合約條文全文，或欲審查的重點條款...", height=300, label_visibility="collapsed")

    # 開始審查按鈕
    st.markdown('<div class="main-action-btn">', unsafe_allow_html=True)
    if st.button("開始審查"):
        if user_input:
            with st.spinner("AI 律師正在掃描風險..."):
                st.markdown(f"""
                <div style="background-color:#F1F5F9; padding:20px; border-radius:12px; border-left:6px solid #E11D48; margin-top:20px;">
                    <h4 style="margin:0; color:#1E293B;">🔍 掃描報告：{st.session_state.selected_tag}</h4>
                    <p style="color:#475569; font-size:14px; margin-top:10px;">
                        發現 2 處高風險：<br>
                        1. <b>賠償條款</b>：比例高於法律常見標準，建議酌減。<br>
                        2. <b>管轄條款</b>：建議明確指定台灣台北地方法院。
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("請先輸入合約內容")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#8E8E8E; font-size:12px; text-align:center; margin-top:10px;">AI 會逐條掃描風險條款並提供修正建議，僅供輔助參考。</div>', unsafe_allow_html=True)

elif st.session_state.active_page == '案情分析':
    st.markdown('<div class="header-text">案情分析</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">梳理法律事實，找出核心爭點</div>', unsafe_allow_html=True)
    case_input = st.text_area("請描述案情經過：", height=400)
    st.markdown('<div class="main-action-btn">', unsafe_allow_html=True)
    if st.button("生成分析報告"):
        st.info("已為您梳理出 3 個法律爭點...")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_page == '法條檢索':
    st.markdown('<div class="header-text">法條檢索</div>', unsafe_allow_html=True)
    search_q = st.text_input("輸入關鍵字：", placeholder="例如：民法 184")
    st.markdown('<div class="main-action-btn">', unsafe_allow_html=True)
    if st.button("搜尋"):
        st.write("搜尋結果：")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_page == '歷史記錄':
    st.markdown('<div class="header-text">歷史記錄</div>', unsafe_allow_html=True)
    st.write("尚無歷史審查記錄。")

# --- 5. 固定在底部的真實功能導覽列 ---
st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True) # 防止內容被遮住的墊片

# 使用容器固定底部
nav_bar = st.container()
with nav_bar:
    # 這裡的黑背景是用 CSS 畫的
    st.markdown('<div class="nav-wrapper">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        # 判斷是否為當前頁面，給予不同的樣式
        css_class = "active-nav" if st.session_state.active_page == '合約審查' else "nav-btn-box"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button("📝\n合約審查"):
            st.session_state.active_page = '合約審查'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        css_class = "active-nav" if st.session_state.active_page == '案情分析' else "nav-btn-box"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button("📊\n案情分析"):
            st.session_state.active_page = '案情分析'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c3:
        css_class = "active-nav" if st.session_state.active_page == '法條檢索' else "nav-btn-box"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button("🔍\n法條檢索"):
            st.session_state.active_page = '法條檢索'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c4:
        css_class = "active-nav" if st.session_state.active_page == '歷史記錄' else "nav-btn-box"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button("⏳\n歷史記錄"):
            st.session_state.active_page = '歷史記錄'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
