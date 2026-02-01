import streamlit as st

# ==========================================
# 1. 系統設定 (手機版優化)
# ==========================================
st.set_page_config(
    page_title="三一協會便民APP",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (手機觸控 + 勾選優化)
# ==========================================
st.markdown("""
    <style>
    /* 全站基礎 */
    .stApp {
        background-color: #f2f2f7; /* iOS 淺灰背景 */
        font-family: -apple-system, BlinkMacSystemFont, "Microsoft JhengHei", sans-serif;
    }
    
    /* 隱藏官方元件 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 手機版頂部 Header (固定式質感) */
    .mobile-header {
        background: linear-gradient(180deg, #007AFF 0%, #0063CC 100%);
        padding: 25px 20px 20px 20px;
        color: white;
        text-align: center;
        border-radius: 0 0 25px 25px;
        margin-top: -60px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,122,255,0.3);
    }
    .app-title { font-size: 26px; font-weight: 900; letter-spacing: 1px; }
    .app-subtitle { font-size: 14px; opacity: 0.95; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; display: inline-block; margin-top: 5px;}
    
    /* 資訊卡片容器 */
    .mobile-card-container {
        background: white;
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        border: 1px solid #eee;
    }
    
    /* 卡片內容樣式 */
    .card-title {
        font-size: 19px;
        font-weight: bold;
        color: #1c1c1e;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    
    /* 辦理方式區塊 */
    .method-box {
        background-color: #f2f2f7;
        padding: 12px;
        border-radius: 12px;
        font-size: 14px;
        color: #3a3a3c;
        margin-bottom: 15px;
        margin-top: 10px;
        border-left: 4px solid #007AFF;
    }
    
    /* 分類標籤 */
    .tag {
        font-size: 12px;
        font-weight: bold;
        padding: 4px 10px;
        border-radius: 6px;
        color: white;
        display: inline-block;
        margin-bottom: 5px;
    }
    
    /* 選單優化 */
    .stRadio > div {
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        gap: 8px;
        padding-bottom: 5px;
    }
    .stRadio label {
        background-color: white !important;
        border: 1px solid #ddd;
        padding: 8px 12px !important;
        border-radius: 20px !important;
        font-size: 14px;
        white-space: nowrap;
    }

    /* 按鈕優化 */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 42px;
        font-weight: 600;
    }
    
    /* 備忘錄區塊 */
    .memo-box {
        background: #fffbea;
        border: 2px dashed #ffd700;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 完整資料庫 (18項新制 + 連結)
# ==========================================
data = [
    # 💰 荷包/稅務
    {"id": 1, "cat": "💰 荷包/稅務", "title": "綜所稅生活費調高即降稅", "icon": "📉", "color": "#34C759",
     "method": "5月報稅自動適用，免申請。符合扶養條件系統會自動扣除。", "link": "https://tax.nat.gov.tw/", "btn": "前往報稅網"},
    {"id": 2, "cat": "💰 荷包/稅務", "title": "國民年金保費調漲84元", "icon": "💸", "color": "#34C759",
     "method": "依收到的繳款單繳納，建議設定銀行帳戶自動扣繳。", "link": "https://www.bli.gov.tw/0013605.html", "btn": "國保專區"},
    {"id": 3, "cat": "💰 荷包/稅務", "title": "租金補貼排除頂加違建", "icon": "🏠", "color": "#34C759",
     "method": "線上申請，需準備租約與存摺。注意房屋稅籍需符合規定。", "link": "https://pip.moi.gov.tw/V3/B/SCRB0102.aspx", "btn": "線上申請"},
    {"id": 4, "cat": "💰 荷包/稅務", "title": "國旅住宿補貼800元/晚", "icon": "🧳", "color": "#34C759",
     "method": "入住前至「台灣旅宿網」上傳身分證，入住時折抵。", "link": "https://taiwanstay.net.tw/", "btn": "登錄證件"},

    # 💼 職場/勞保
    {"id": 5, "cat": "💼 職場/勞保", "title": "最低工資調漲至2.95萬", "icon": "💵", "color": "#007AFF",
     "method": "無需申請。若薪資低於標準，可向勞工局申訴。", "link": "https://www.mol.gov.tw/", "btn": "勞動部官網"},
    {"id": 6, "cat": "💼 職場/勞保", "title": "勞保年金60歲領年減4%", "icon": "📉", "color": "#007AFF",
     "method": "向勞保局申請。建議先試算最划算的請領年齡。", "link": "https://edesk.bli.gov.tw/na/", "btn": "年金試算"},
    {"id": 7, "cat": "💼 職場/勞保", "title": "農保生育給付增至10萬", "icon": "👶", "color": "#007AFF",
     "method": "備妥出生證明，向投保農會提出申請。", "link": "https://www.bli.gov.tw/0013605.html", "btn": "申請書下載"},
    {"id": 8, "cat": "💼 職場/勞保", "title": "勞工請假按比例扣全勤", "icon": "📝", "color": "#007AFF",
     "method": "依公司規定。若雇主違法扣薪，可申請調解。", "link": "https://labor-elearning.mol.gov.tw/", "btn": "權益查詢"},
    {"id": 9, "cat": "💼 職場/勞保", "title": "育嬰假以日計領8成薪", "icon": "🍼", "color": "#007AFF",
     "method": "向雇主請假後，向勞保局申請「育嬰留職停薪津貼」。", "link": "https://www.bli.gov.tw/0017280.html", "btn": "線上申辦"},

    # 🏥 醫療/長照
    {"id": 10, "cat": "🏥 醫療/長照", "title": "長照3.0啟動第2、3階段", "icon": "👵", "color": "#FF3B30",
     "method": "手機直接撥打「1966」長照專線，專人到府評估。", "link": "https://1966.gov.tw/", "btn": "1966 專區"},
    {"id": 11, "cat": "🏥 醫療/長照", "title": "長照特別扣除額大調升", "icon": "🧾", "color": "#FF3B30",
     "method": "5月報稅申報。需檢附身心障礙證明或失能核定函。", "link": "https://www.etax.nat.gov.tw/", "btn": "扣除額說明"},
    {"id": 12, "cat": "🏥 醫療/長照", "title": "免費胃癌篩檢限一生1次", "icon": "🩺", "color": "#FF3B30",
     "method": "45-74歲民眾，持健保卡至特約院所即可。", "link": "https://www.hpa.gov.tw/", "btn": "查詢院所"},

    # 🚗 生活/交通
    {"id": 13, "cat": "🚗 生活/交通", "title": "老人換駕照降到70歲", "icon": "🪪", "color": "#FF9500",
     "method": "收到通知後，至監理站體檢與認知測驗，合格換發。", "link": "https://www.mvdis.gov.tw/", "btn": "監理服務網"},
    {"id": 14, "cat": "🚗 生活/交通", "title": "無照駕駛累犯罰6萬", "icon": "👮", "color": "#FF9500",
     "method": "違規查詢與繳款，可上監理服務網。", "link": "https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQuery", "btn": "罰單查詢"},
    {"id": 15, "cat": "🚗 生活/交通", "title": "教召改14天退8年召2次", "icon": "🪖", "color": "#FF9500",
     "method": "上「後備軍人網路服務臺」查詢年度教召資訊。", "link": "https://afrc.mnd.gov.tw/EFR/FAQ.aspx", "btn": "教召查詢"},
    {"id": 16, "cat": "🚗 生活/交通", "title": "北捷7月解鎖iPhone進站", "icon": "📱", "color": "#FF9500",
     "method": "屆時將iPhone綁定快速交通卡即可感應。", "link": "https://www.metro.taipei/", "btn": "北捷官網"},
    {"id": 17, "cat": "🚗 生活/交通", "title": "家貓植晶片違者罰款", "icon": "🐱", "color": "#FF9500",
     "method": "帶貓咪至動物醫院施打晶片並辦理寵物登記。", "link": "https://www.pet.gov.tw/", "btn": "寵物登記網"},
    {"id": 18, "cat": "🚗 生活/交通", "title": "原民身分登記限期1/5前", "icon": "📝", "color": "#FF9500",
     "method": "攜帶身分證、戶口名簿至任一戶政事務所辦理。", "link": "https://www.ris.gov.tw/", "btn": "戶政司官網"},
]

# ==========================================
# 4. 手機版頭部
# ==========================================
st.markdown("""
    <div class="mobile-header">
        <div class="app-title">2026 便民新制通</div>
        <div class="app-subtitle">三一協會 📢</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. 導航與狀態管理
# ==========================================
# 初始化 session state 來儲存勾選狀態
if "checklist" not in st.session_state:
    st.session_state.checklist = []

category = st.radio(
    "分類導航",
    ["全部", "💰 荷包/稅務", "💼 職場/勞保", "🏥 醫療/長照", "🚗 生活/交通"],
    horizontal=True,
    label_visibility="collapsed"
)

# 篩選資料
if category == "全部":
    display_items = data
else:
    display_items = [item for item in data if item["cat"] == category]

st.write("") 

# ==========================================
# 6. 動態牆 (含勾選功能)
# ==========================================
for item in display_items:
    # 外層容器：白色卡片
    with st.container():
        # 版面配置：左邊主要內容 (0.85)，右邊勾選框 (0.15)
        col_content, col_check = st.columns([0.85, 0.15])
        
        with col_content:
            st.markdown(f"""
            <div class="mobile-card-container">
                <span class="tag" style="background-color: {item['color']};">{item['cat'].split(" ")[1]}</span>
                <div class="card-title">{item['icon']} {item['title']}</div>
                <div class="method-box">
                    <b>💡 辦理方式：</b><br>{item['method']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 按鈕獨立放置，避免被 HTML 包覆影響點擊
            st.link_button(f"🔗 {item['btn']}", item['link'], use_container_width=True)
            
        with col_check:
            # 垂直置中調整 (讓勾選框不會跑太上面)
            st.write("")
            st.write("")
            
            # 檢查是否已在清單中
            is_checked = item['title'] in st.session_state.checklist
            
            # 勾選框互動
            if st.checkbox("", key=f"chk_{item['id']}", value=is_checked):
                if item['title'] not in st.session_state.checklist:
                    st.session_state.checklist.append(item['title'])
            else:
                if item['title'] in st.session_state.checklist:
                    st.session_state.checklist.remove(item['title'])
        
        st.write("---") # 分隔線

# ==========================================
# 7. 我的備忘錄 (自動生成)
# ==========================================
if st.session_state.checklist:
    st.markdown("""<div class="memo-box">""", unsafe_allow_html=True)
    st.subheader("📝 我的待辦清單")
    st.caption("這是您勾選的項目，請截圖保存！")
    
    for i, title in enumerate(st.session_state.checklist):
        st.markdown(f"**{i+1}. {title}**")
        
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 8. 底部版權
# ==========================================
st.markdown("""
    <div style="text-align: center; margin-top: 30px; padding-bottom: 20px; color: #8e8e93; font-size: 12px;">
    三一協會 © 2026<br>
    Designed for Mobile
    </div>
""", unsafe_allow_html=True)

