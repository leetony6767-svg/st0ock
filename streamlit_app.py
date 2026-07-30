import streamlit as st

st.set_page_config(page_title="強棒法律工作台", page_icon="⚖️")
st.title("⚖️ 強棒法律工作台")

menu = st.sidebar.radio("任務選擇", ["📜 合約審查", "🔍 案情分析", "📚 法條檢索"])
st.header(f"目前執行：{menu}")

content = st.text_area("請在此輸入合約或案情內容：", height=300)

if st.button("🚀 開始分析"):
    if content:
        st.success("分析完成！請依據中華民國法律查驗最新判例字號。")
    else:
        st.warning("請先輸入內容。")

st.sidebar.markdown("---")
st.sidebar.caption("【法律免責聲明】本工具僅供參考，不構成正式法律意見。")
