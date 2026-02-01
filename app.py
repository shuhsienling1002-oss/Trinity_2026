import streamlit as st

# ==========================================
# 1. 系統設定
# ==========================================
st.set_page_config(
    page_title="2026 新制度權益通 | 三一協會",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (三一協會專屬藍色系)
# ==========================================
st.markdown("""
    <style>
    .stApp {
        background-color: #F0F4F8;
        font-family: "Microsoft JhengHei", sans-serif;
    }
    
    /* 頂部標題區 */
    .header-box {
        background: linear-gradient(135deg, #0056b3 0%, #3399ff 100%);
        padding: 30px 20px;
        border-radius: 0 0 30px 30px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-top: -60px;
    }
    .header-title { font-size: 28px; font-weight: bold; letter-spacing: 1px; }
    
    /* 資訊卡片 */
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .info-card:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    /* 標籤樣式 */
    .card-tag {
        font-size: 13px;
        padding: 4px 12px;
        border-radius: 20px;
        color: white;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
    }
    .tag-labor { background-color: #3182CE; } /* 藍 */
    .tag-money { background-color: #38A169; } /* 綠 */
    .tag-health { background-color: #D69E2E; } /* 黃 */
    .tag-life { background-color: #805AD5; } /* 紫 */
    
    /* 按鈕優化 */
    .stLinkButton > a {
        border-radius: 10px !important;
        background-color: #f8f9fa !important;
        color: #0056b3 !important;
        border: 1px solid #dee2e6 !important;
        font-weight: bold !important;
        transition: 0.3s;
        text-align: center;
    }
    .stLinkButton > a:hover {
        border-color: #0056b3 !important;
        background-color: #e7f1ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 完整資料庫 (18項 + 連結)
# ==========================================
regulations = [
    # --- 荷包/稅務 (福利) ---
    {
        "cat": "福利", "title": "綜所稅生活費調高即降稅", "desc": "免稅額調升，5月報稅自動適用。", 
        "detail": "基本生活費調高至 21.3 萬，免申請。",
        "url": "https://tax.nat.gov.tw/", "btn": "財政部稅務入口網"
    },
    {
        "cat": "福利", "title": "最低工資調漲 2.95 萬", "desc": "月薪 29,500 / 時薪 196 元。", 
        "detail": "2026/1/1 生效，勞健保級距同步調整。",
        "url": "https://www.mol.gov.tw/", "btn": "勞動部公告"
    },
    {
        "cat": "福利", "title": "勞保年金 60 歲領減 20%", "desc": "法定請領年齡調高至 65 歲。", 
        "detail": "提早 5 年請領會被扣 20% 減給年金。",
        "url": "https://www.bli.gov.tw/0000009.html", "btn": "勞保局年金專區"
    },
    {
        "cat": "福利", "title": "農保生育給付增至 10 萬", "desc": "雙胞胎可領 20 萬。", 
        "detail": "補助金額翻倍，減輕農友負擔。",
        "url": "https://www.bli.gov.tw/0000009.html", "btn": "農保給付說明"
    },
    {
        "cat": "福利", "title": "長照特別扣除額大調升", "desc": "每人調升至 18 萬元。", 
        "detail": "報稅時適用，減輕照顧者負擔。",
        "url": "https://www.ntbt.gov.tw/", "btn": "國稅局專區"
    },
    {
        "cat": "福利", "title": "國民年金保費調漲", "desc": "每月自付額增加 84 元。", 
        "detail": "隨物價指數調整費率。",
        "url": "https://www.bli.gov.tw/0013552.html", "btn": "國保保費試算"
    },
    {
        "cat": "福利", "title": "租金補貼排除頂加違建", "desc": "資格變嚴，僅限合法建物。", 
        "detail": "頂樓加蓋將不再補助範圍內。",
        "url": "https://pip.moi.gov.tw/V3/B/SCRB0102.aspx", "btn": "300億租金補貼專區"
    },
    {
        "cat": "福利", "title": "國旅住宿補貼 800元/晚", "desc": "平日入住才有，續住加碼。", 
        "detail": "預計 4 月開跑，需上網登錄證件。",
        "url": "https://gostay.tbroc.gov.tw/", "btn": "台灣旅宿網(待更新)"
    },

    # --- 職場/勞保 (勞工) ---
    {
        "cat": "勞工", "title": "勞工請假扣全勤限制", "desc": "必須「按比例」扣發。", 
        "detail": "不能因請假 1 小時就扣光整月全勤。",
        "url": "https://www.mol.gov.tw/1607/28162/28166/28268/", "btn": "勞動部請假規定"
    },
    {
        "cat": "勞工", "title": "育嬰假以日計領 8 成薪", "desc": "更彈性，不需一次請長假。", 
        "detail": "方便雙薪家庭短期調度。",
        "url": "https://www.bli.gov.tw/0017280.html", "btn": "育嬰留停津貼申請"
    },
    {
        "cat": "勞工", "title": "教召改 14 天退 8 年召 2 次", "desc": "新制教召，1 次抵 2 次。", 
        "detail": "針對退伍 8 年內後備軍人。",
        "url": "https://afrc.mnd.gov.tw/EFR/index.aspx", "btn": "後備軍人召集查詢"
    },

    # --- 醫療/長照 (健康) ---
    {
        "cat": "健康", "title": "長照 3.0 啟動", "desc": "納入年輕型失智症。", 
        "detail": "增加智慧輔具租賃補助。",
        "url": "https://1966.gov.tw/LTC/mp-201.html", "btn": "長照 2.0/3.0 專區"
    },
    {
        "cat": "健康", "title": "免費胃癌篩檢", "desc": "45-74 歲終身 1 次免費。", 
        "detail": "公費胃幽門螺旋桿菌篩檢。",
        "url": "https://www.hpa.gov.tw/Pages/List.aspx?nodeid=24", "btn": "癌症篩檢資格查詢"
    },

    # --- 生活/交通 (生活) ---
    {
        "cat": "生活", "title": "高齡換照降至 70 歲", "desc": "需體檢+認知測驗。", 
        "detail": "2026/5 起實施，駕照效期 3 年。",
        "url": "https://www.mvdis.gov.tw/", "btn": "監理服務網"
    },
    {
        "cat": "生活", "title": "無照駕駛重罰 6 萬", "desc": "累犯罰 6 萬 + 扣車。", 
        "detail": "得沒入車輛，罰則大幅加重。",
        "url": "https://www.mvdis.gov.tw/", "btn": "交通違規罰則查詢"
    },
    {
        "cat": "生活", "title": "北捷 7 月解鎖 iPhone 進站", "desc": "Apple Pay 快速通關。", 
        "detail": "閘門系統更新，支援手機感應。",
        "url": "https://www.metro.taipei/", "btn": "台北捷運公告"
    },
    {
        "cat": "生活", "title": "家貓植晶片", "desc": "違者最高罰 1.5 萬。", 
        "detail": "請至獸醫院完成寵物登記。",
        "url": "https://www.pet.gov.tw/", "btn": "寵物登記管理資訊網"
    },
    {
        "cat": "生活", "title": "原民身分登記 (1/5前)", "desc": "未回復傳統名恐失效。", 
        "detail": "最後補救期 30 天，請速洽戶政。",
        "url": "https://www.ris.gov.tw/app/portal/671", "btn": "全國戶政據點查詢"
    }
]

# ==========================================
# 4. 頁面邏輯
# ==========================================

# 標題
st.markdown("""
    <div class="header-box">
        <div class="header-title">三一協會</div>
        <div style="margin-top:5px; font-size:16px;">📢 2026 便民新制通 (完整版)</div>
    </div>
""", unsafe_allow_html=True)

# 篩選器
categories = ["全部", "福利", "勞工", "健康", "生活"]
selected_cat = st.selectbox("請選擇您想了解的類別：", categories)

# 過濾資料
if selected_cat == "全部":
    display_data = regulations
else:
    display_data = [r for r in regulations if r['cat'] == selected_cat]

# 顯示內容
st.write(f"共找到 **{len(display_data)}** 項相關新制")

for item in display_data:
    # 決定顏色
    color_map = {"福利": "tag-money", "勞工": "tag-labor", "健康": "tag-health", "生活": "tag-life"}
    tag_class = color_map.get(item['cat'], "tag-life")
    
    # 卡片 HTML
    st.markdown(f"""
    <div class="info-card">
        <span class="card-tag {tag_class}">{item['cat']}</span>
        <h3 style="margin: 0 0 8px 0; font-size: 20px; color: #2d3748;">{item['title']}</h3>
        <div style="color:#4a5568; margin-bottom:8px; font-weight:bold;">{item['desc']}</div>
        <div style="font-size:14px; color:#718096; line-height: 1.5;">💡 {item['detail']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 外部連結按鈕 (滿版)
    if "url" in item:
        st.link_button(
            label=f"🔗 {item['btn']}", 
            url=item['url'], 
            use_container_width=True
        )
    
    st.write("") # 間距

# 頁尾
st.divider()
st.markdown("<div style='text-align:center; color:#999; font-size:12px;'>© 2026 三一教育文化協會 | 資料來源：政府公告</div>", unsafe_allow_html=True)
