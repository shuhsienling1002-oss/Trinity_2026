import streamlit as st
import pandas as pd

# ==========================================
# 1. 系統設定
# ==========================================
st.set_page_config(
    page_title="三一協會 - 2026新制快訊",
    page_icon="📢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學設計 (清新便民風)
# ==========================================
st.markdown("""
    <style>
    /* 全站字體與背景 */
    .stApp {
        background-color: #F0F8FF; /* 淡雅的愛麗絲藍 */
        font-family: "Microsoft JhengHei", sans-serif;
    }
    
    /* 隱藏官方浮水印 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 頂部標題設計 */
    .header-box {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        padding: 30px 20px;
        border-radius: 0 0 25px 25px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-top: -60px;
    }
    .header-title { font-size: 32px; font-weight: 900; letter-spacing: 2px; }
    .header-subtitle { font-size: 18px; margin-top: 10px; opacity: 0.9; background: rgba(255,255,255,0.2); display: inline-block; padding: 5px 15px; border-radius: 20px;}
    
    /* 資訊卡片設計 */
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #007bff;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .info-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .card-id {
        font-size: 14px;
        color: #888;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .card-content {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        line-height: 1.5;
    }
    .card-tag {
        display: inline-block;
        font-size: 12px;
        padding: 3px 10px;
        border-radius: 10px;
        color: white;
        margin-top: 10px;
    }
    
    /* 分類顏色 */
    .tag-money { background-color: #28a745; } /* 荷包/稅務 - 綠 */
    .tag-work { background-color: #17a2b8; }  /* 職場/勞保 - 藍 */
    .tag-health { background-color: #dc3545; } /* 醫療/長照 - 紅 */
    .tag-life { background-color: #ffc107; color: #333 !important; }   /* 生活/交通 - 黃 */

    /* 搜尋框優化 */
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #b3d7ff;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 資料庫建立 (18項新制)
# ==========================================
# 將圖片內容轉化為結構化資料，並加上分類標籤
data = [
    {"id": 1, "text": "綜所稅生活費調高即降稅", "category": "荷包/稅務", "tag_class": "tag-money", "icon": "💰"},
    {"id": 2, "text": "最低工資調漲至2.95萬", "category": "職場/勞保", "tag_class": "tag-work", "icon": "💼"},
    {"id": 3, "text": "勞保年金60歲領年減4%", "category": "職場/勞保", "tag_class": "tag-work", "icon": "📉"},
    {"id": 4, "text": "農保生育給付增至10萬", "category": "職場/勞保", "tag_class": "tag-work", "icon": "👶"},
    {"id": 5, "text": "勞工請假按比例扣全勤", "category": "職場/勞保", "tag_class": "tag-work", "icon": "📝"},
    {"id": 6, "text": "請育嬰假以日計領8成薪", "category": "職場/勞保", "tag_class": "tag-work", "icon": "🍼"},
    {"id": 7, "text": "長照3.0啟動第2、3階段", "category": "醫療/長照", "tag_class": "tag-health", "icon": "👵"},
    {"id": 8, "text": "長照特別扣除額大調升", "category": "醫療/長照", "tag_class": "tag-health", "icon": "💵"},
    {"id": 9, "text": "國民年金保費調漲84元", "category": "荷包/稅務", "tag_class": "tag-money", "icon": "💸"},
    {"id": 10, "text": "免費胃癌篩檢限一生1次", "category": "醫療/長照", "tag_class": "tag-health", "icon": "🏥"},
    {"id": 11, "text": "老人換駕照將降到70歲", "category": "生活/交通", "tag_class": "tag-life", "icon": "🚗"},
    {"id": 12, "text": "無照駕駛累犯罰6萬扣車", "category": "生活/交通", "tag_class": "tag-life", "icon": "👮"},
    {"id": 13, "text": "租金補貼排除頂加違建", "category": "荷包/稅務", "tag_class": "tag-money", "icon": "🏠"},
    {"id": 14, "text": "教召改14天退8年召2次", "category": "生活/交通", "tag_class": "tag-life", "icon": "🪖"},
    {"id": 15, "text": "北捷7月解鎖哀鳳嗶進站", "category": "生活/交通", "tag_class": "tag-life", "icon": "📱"},
    {"id": 16, "text": "家貓植晶片寵登違者罰款", "category": "生活/交通", "tag_class": "tag-life", "icon": "🐱"},
    {"id": 17, "text": "原民身分登記限期1/5前", "category": "生活/交通", "tag_class": "tag-life", "icon": "📝"},
    {"id": 18, "text": "國旅住宿補貼800元/晚", "category": "荷包/稅務", "tag_class": "tag-money", "icon": "🧳"},
]

# ==========================================
# 4. 頁面標題區
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">三一協會</div>
        <div class="header-subtitle">2026年新制報給您 📢</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. 搜尋與篩選區
# ==========================================
col_search, col_filter = st.columns([2, 1])

with col_search:
    search_query = st.text_input("🔍 關鍵字搜尋 (如：勞保、罰款、補助)", placeholder="輸入您想找的內容...")

with col_filter:
    category_filter = st.selectbox("📂 選擇分類", ["全部顯示", "荷包/稅務", "職場/勞保", "醫療/長照", "生活/交通"])

# ==========================================
# 6. 內容顯示邏輯
# ==========================================
filtered_data = data

# 1. 分類篩選
if category_filter != "全部顯示":
    filtered_data = [d for d in filtered_data if d["category"] == category_filter]

# 2. 關鍵字搜尋
if search_query:
    filtered_data = [d for d in filtered_data if search_query in d["text"]]

# 3. 顯示結果
st.markdown(f"### 📋 新制清單 (共 {len(filtered_data)} 項)")

# 初始化 Session State 用於儲存勾選狀態
if "checked_items" not in st.session_state:
    st.session_state.checked_items = []

# 遍歷資料生成卡片
for item in filtered_data:
    # 使用 container 模擬卡片
    col_check, col_content = st.columns([0.1, 0.9])
    
    with col_check:
        # 讓使用者勾選與自己有關的項目
        is_checked = st.checkbox("", key=f"check_{item['id']}")
        if is_checked and item['text'] not in st.session_state.checked_items:
            st.session_state.checked_items.append(item['text'])
        elif not is_checked and item['text'] in st.session_state.checked_items:
            st.session_state.checked_items.remove(item['text'])

    with col_content:
        st.markdown(f"""
        <div class="info-card" style="border-left-color: {
            '#28a745' if item['category'] == '荷包/稅務' else 
            '#17a2b8' if item['category'] == '職場/勞保' else 
            '#dc3545' if item['category'] == '醫療/長照' else '#ffc107'
        };">
            <div class="card-id">NO. {item['id']}</div>
            <div class="card-content">{item['icon']} {item['text']}</div>
            <span class="card-tag {item['tag_class']}">{item['category']}</span>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 7. 我的備忘錄 (勾選後顯示)
# ==========================================
if st.session_state.checked_items:
    with st.expander("📝 我的關注清單 (已勾選項目)", expanded=True):
        st.success("以下是您勾選與自身權益相關的項目，請截圖保存！")
        for i, text in enumerate(st.session_state.checked_items):
            st.markdown(f"**{i+1}. {text}**")

# ==========================================
# 8. 底部資訊
# ==========================================
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 📞 三一協會服務專線")
    st.markdown("週一至週五 09:00-17:00")
    st.markdown("☎️ (03) 123-4567")

with col2:
    st.markdown("#### 💡 小提醒")
    st.markdown("本資訊整理自 2026 新制預告，實際執行細節請以政府各主管機關公告為準。")

st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #aaa; font-size: 12px;">
    三一協會 © 2026 All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
