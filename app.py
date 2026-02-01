import streamlit as st

# ==========================================
# 1. 系統設定 (升級版)
# ==========================================
st.set_page_config(
    page_title="三一協會 - 2026便民新制通",
    page_icon="📢",
    layout="wide", # 改為寬版，資訊呈現更清楚
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CSS 美學設計 (行動優先、按鈕優化)
# ==========================================
st.markdown("""
    <style>
    /* 全站字體與背景 */
    .stApp {
        background-color: #f4f8fb;
        font-family: "Microsoft JhengHei", sans-serif;
    }
    
    /* 隱藏官方浮水印 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 頂部標題設計 */
    .header-box {
        background: linear-gradient(120deg, #2980b9, #6dd5fa);
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: -60px;
    }
    .header-title { font-size: 36px; font-weight: 900; letter-spacing: 2px; }
    .header-subtitle { font-size: 20px; margin-top: 10px; opacity: 0.95; background: rgba(0,0,0,0.1); display: inline-block; padding: 5px 20px; border-radius: 50px;}
    
    /* 資訊卡片設計 (升級版) */
    .info-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #2980b9;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        height: 100%; /* 讓卡片等高 */
        transition: transform 0.2s;
    }
    .info-card:hover {
        transform: translateY(-5px);
    }
    .card-title {
        font-size: 22px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 15px;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    .card-method {
        font-size: 16px;
        color: #555;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 3px solid #ccc;
    }
    
    /* 分類標籤樣式 */
    .category-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 15px;
        color: white;
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* 按鈕樣式優化 */
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 超詳細資料庫 (含連結與辦理方式)
# ==========================================
data = [
    {
        "id": 1, "category": "💰 荷包/稅務", "title": "綜所稅生活費調高即降稅", "icon": "📉",
        "method": "每年5月報稅時自動適用，免申請。若符合扶養親屬條件，系統會自動扣除。",
        "link_text": "財政部電子申報繳稅服務網", "link_url": "https://tax.nat.gov.tw/"
    },
    {
        "id": 2, "category": "💼 職場/勞保", "title": "最低工資調漲至2.95萬", "icon": "💵",
        "method": "無需申請。雇主應自動調整薪資，若低於標準可向勞工局申訴。",
        "link_text": "勞動部基本工資專區", "link_url": "https://www.mol.gov.tw/1607/28162/28166/28180/"
    },
    {
        "id": 3, "category": "💼 職場/勞保", "title": "勞保年金60歲領年減4%", "icon": "📉",
        "method": "向勞保局提出申請。建議至勞保局e化服務系統試算最划算的請領年齡。",
        "link_text": "勞保局e化服務系統", "link_url": "https://edesk.bli.gov.tw/na/"
    },
    {
        "id": 4, "category": "💼 職場/勞保", "title": "農保生育給付增至10萬", "icon": "👶",
        "method": "備妥出生證明等文件，向投保農會提出申請，或委託農會轉交勞保局。",
        "link_text": "勞保局-農保生育給付說明", "link_url": "https://www.bli.gov.tw/0013605.html"
    },
    {
        "id": 5, "category": "💼 職場/勞保", "title": "勞工請假按比例扣全勤", "icon": "📝",
        "method": "依公司內部請假規定辦理。若雇主違法扣薪，可申請勞資爭議調解。",
        "link_text": "全民勞教e網", "link_url": "https://labor-elearning.mol.gov.tw/"
    },
    {
        "id": 6, "category": "💼 職場/勞保", "title": "請育嬰假以日計領8成薪", "icon": "🍼",
        "method": "向雇主請假後，檢附證明文件向勞保局申請「育嬰留職停薪津貼」。",
        "link_text": "勞保局-育嬰津貼線上申辦", "link_url": "https://www.bli.gov.tw/0017280.html"
    },
    {
        "id": 7, "category": "🏥 醫療/長照", "title": "長照3.0啟動第2、3階段", "icon": "👵",
        "method": "手機或市話直接撥打「1966」長照專線，將有專人到府評估。",
        "link_text": "衛福部長照專區 (1966)", "link_url": "https://1966.gov.tw/"
    },
    {
        "id": 8, "category": "🏥 醫療/長照", "title": "長照特別扣除額大調升", "icon": "🧾",
        "method": "每年5月報稅時申報。需檢附身心障礙證明或長照失能等級核定函。",
        "link_text": "財政部-長照扣除額專區", "link_url": "https://www.etax.nat.gov.tw/etwmain/tax-info/long-term-care-special-deduction-area"
    },
    {
        "id": 9, "category": "💰 荷包/稅務", "title": "國民年金保費調漲84元", "icon": "💸",
        "method": "依收到之繳款單繳納。可設定銀行帳戶自動扣繳以避免遺忘。",
        "link_text": "勞保局-國民年金專區", "link_url": "https://www.bli.gov.tw/0013605.html"
    },
    {
        "id": 10, "category": "🏥 醫療/長照", "title": "免費胃癌篩檢限一生1次", "icon": "🩺",
        "method": "45-74歲民眾，持健保卡至健保特約醫療院所即可辦理 (糞便抗原檢測)。",
        "link_text": "國民健康署-癌症篩檢", "link_url": "https://www.hpa.gov.tw/Pages/List.aspx?nodeid=212"
    },
    {
        "id": 11, "category": "🚗 生活/交通", "title": "老人換駕照將降到70歲", "icon": "🪪",
        "method": "收到通知單後，至監理站進行體檢與認知功能測驗，合格後換發。",
        "link_text": "監理服務網-高齡駕駛專區", "link_url": "https://www.mvdis.gov.tw/"
    },
    {
        "id": 12, "category": "🚗 生活/交通", "title": "無照駕駛累犯罰6萬扣車", "icon": "👮",
        "method": "請勿以身試法。若需查詢違規罰款，可上監理服務網查詢。",
        "link_text": "監理服務網-罰單查詢", "link_url": "https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQuery"
    },
    {
        "id": 13, "category": "💰 荷包/稅務", "title": "租金補貼排除頂加違建", "icon": "🏠",
        "method": "線上申請。需準備租賃契約、存摺封面。注意房屋稅籍需符合規定。",
        "link_text": "300億租金補貼線上申請", "link_url": "https://pip.moi.gov.tw/V3/B/SCRB0102.aspx"
    },
    {
        "id": 14, "category": "🚗 生活/交通", "title": "教召改14天退8年召2次", "icon": "🪖",
        "method": "可上「後備軍人網路服務臺」查詢年度教召資訊。",
        "link_text": "後備軍人召集查詢系統", "link_url": "https://afrc.mnd.gov.tw/EFR/FAQ.aspx"
    },
    {
        "id": 15, "category": "🚗 生活/交通", "title": "北捷7月解鎖哀鳳嗶進站", "icon": "📱",
        "method": "無需申請。屆時將iPhone綁定Apple Pay或快速交通卡功能即可直接感應。",
        "link_text": "台北捷運公司官網", "link_url": "https://www.metro.taipei/"
    },
    {
        "id": 16, "category": "🚗 生活/交通", "title": "家貓植晶片寵登違者罰款", "icon": "🐱",
        "method": "帶貓咪至動物醫院施打晶片並辦理寵物登記。",
        "link_text": "寵物登記管理資訊網", "link_url": "https://www.pet.gov.tw/"
    },
    {
        "id": 17, "category": "🚗 生活/交通", "title": "原民身分登記限期1/5前", "icon": "📝",
        "method": "請儘速攜帶身分證、戶口名簿至任一戶政事務所辦理身分回復或登記。",
        "link_text": "內政部戶政司全球資訊網", "link_url": "https://www.ris.gov.tw/"
    },
    {
        "id": 18, "category": "💰 荷包/稅務", "title": "國旅住宿補貼800元/晚", "icon": "🧳",
        "method": "入住前至「台灣旅宿網」上傳身分證件，入住配合旅宿時折抵。",
        "link_text": "台灣旅宿網", "link_url": "https://taiwanstay.net.tw/"
    },
]

# ==========================================
# 4. 側邊選單設計 (直覺好用)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/942/942748.png", width=100)
    st.title("三一協會便民通")
    st.write("👋 您好！請選擇您感興趣的分類：")
    
    # 使用 Radio Button 作為直覺選單
    category_selection = st.radio(
        "快速導航",
        ["🏠 全部顯示", "💰 荷包/稅務", "💼 職場/勞保", "🏥 醫療/長照", "🚗 生活/交通"],
        index=0
    )
    
    st.info("💡 小撇步：點擊右側卡片下方的按鈕，可以直接連到政府網站辦理喔！")
    st.markdown("---")
    st.caption("版本：2026.1.0 | 三一協會")

# ==========================================
# 5. 主畫面內容
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">三一協會</div>
        <div class="header-subtitle">2026年新制報給您 📢</div>
    </div>
""", unsafe_allow_html=True)

# 標題顯示
display_category = category_selection.split(" ")[1] if category_selection != "🏠 全部顯示" else "所有新制"
st.subheader(f"📌 目前顯示：{display_category}")

# 資料篩選
if category_selection == "🏠 全部顯示":
    display_data = data
else:
    # 取出 icon 後面的文字進行比對
    filter_key = category_selection
    display_data = [d for d in data if d["category"] == filter_key]

# ==========================================
# 6. 卡片式內容呈現 (RWD Grid Layout)
# ==========================================
# 設定每行顯示的卡片數量 (在大螢幕2張，小螢幕自動調整)
cols = st.columns(2) 

for index, item in enumerate(display_data):
    with cols[index % 2]:
        # 決定分類標籤顏色
        tag_color = "#28a745" # 預設綠
        if "職場" in item["category"]: tag_color = "#17a2b8"
        elif "醫療" in item["category"]: tag_color = "#dc3545"
        elif "生活" in item["category"]: tag_color = "#f39c12"
        
        # 卡片容器
        with st.container():
            st.markdown(f"""
            <div class="info-card" style="border-top-color: {tag_color};">
                <div style="margin-bottom:10px;">
                    <span class="category-badge" style="background-color: {tag_color};">{item['category']}</span>
                </div>
                <div class="card-title">{item['icon']} {item['title']}</div>
                <div class="card-method">
                    <b>💡 該怎麼做？</b><br>
                    {item['method']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 傳送門按鈕 (獨立出來以確保 Streamlit 功能正常)
            st.link_button(f"🔗 前往：{item['link_text']}", item['link_url'], use_container_width=True)
            st.write("") # 增加一點間距

# ==========================================
# 7. 底部聲明
# ==========================================
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #888; font-size: 13px;">
    本資訊整理自 2026 預告新制，詳細規定請依各主管機關公告為準。<br>
    Designed by 三一協會 © 2026
    </div>
""", unsafe_allow_html=True)
