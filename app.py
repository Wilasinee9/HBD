import streamlit as st

# 1. ตั้งค่าหน้าเว็บและ Favicon
st.set_page_config(
    page_title="The Impact of Technology in the Modern World",
    page_icon="💻",
    layout="wide"
)

# 2. ใส่ CSS เพื่อสร้างสไตล์วินเทจ/อนิเมะ และกล่องข้อความจำลองตามภาพต้นแบบ
st.markdown("""
    <style>
    /* ตั้งค่าธีมพื้นหลังให้ดูสดใสแนวพาสเทล/อนิเมะ */
    .stApp {
        background-color: #E6F3FF;
    }
    
    /* สไตล์ของหัวข้อหลัก */
    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2B579A;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        border-bottom: 3px double #2B579A;
        margin-bottom: 20px;
    }
    
    /* สไตล์กล่องหน้าต่างโปรแกรม (Window Module) */
    .window-box {
        background-color: #FFFFFF;
        border: 2px solid #000000;
        box-shadow: 4px 4px 0px #888888;
        border-radius: 4px;
        margin-bottom: 25px;
        overflow: hidden;
    }
    
    /* แถบด้านบนของหน้าต่าง */
    .window-header {
        background: linear-gradient(90deg, #2B579A, #6085BB);
        color: white;
        padding: 6px 12px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 14px;
    }
    
    /* แถบควบคุมจำลอง (X, <, >, C) */
    .window-controls {
        font-family: monospace;
        letter-spacing: 5px;
        cursor: pointer;
    }
    
    /* ส่วนเนื้อหาในหน้าต่าง */
    .window-body {
        padding: 15px;
        color: #333333;
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* สไตล์สำหรับรูปภาพเพื่อให้เข้ากับธีมกล่อง */
    .window-img {
        width: 100%;
        border-radius: 4px;
        border: 1px solid #ddd;
        margin-top: 10px;
    }
    
    /* จำลองปุ่มกดย้อนยุคตามภาพ (Okay, Cancel, Delete) */
    .custom-btn {
        background-color: #EFEFEF;
        border: 2px solid #777;
        padding: 4px 14px;
        font-size: 13px;
        cursor: pointer;
        box-shadow: 1px 1px 0px #000;
        margin-right: 5px;
        display: inline-block;
        margin-top: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ลิงก์รูปภาพทุ่งดอกไม้แนวอนิเมะ (จำลองภาพแนว Pixel/Anime Cloud จากไฟล์แนบของคุณ)
IMAGE_URL = "https://images.unsplash.com/photo-1578301978693-85fa9c0320b9?w=600&auto=format&fit=crop"

# 4. ส่วนหัวของเว็บไซต์ตามหน้าหลัก
st.markdown("<h1 class='main-title'>📌 The Impact of Technology in the Modern World</h1>", unsafe_allow_html=True)

# 5. แถบเมนูด้านข้าง (Sidebar Navigation) เพื่อเลือกหน้าต่างที่จะดูเหมือนการกดเปิดโฟลเดอร์
st.sidebar.title("📁 Main Directory (Home)")
page = st.sidebar.radio(
    "เลือกหัวข้อที่ต้องการเข้าชม:",
    [
        "All Overview (ดูทั้งหมด)",
        "1. Introduction & Evolution",
        "2. Tech Categories (IT, Comm, Edu)",
        "3. AI & Environmental Tech",
        "4. Ethical Issues & Future"
    ]
)

# ฟังก์ชันตัวช่วยในการวาดหน้าต่างจำลอง (Window Component)
def draw_window(title, text, show_image=False, btn_type="okay"):
    btn_html = ""
    if btn_type == "okay":
        btn_html = "<div class='custom-btn'>Okay</div>"
    elif btn_type == "okay_cancel":
        btn_html = "<div class='custom-btn'>Okay</div><div class='custom-btn'>Cancel</div>"
    elif btn_type == "okay_delete":
        btn_html = "<div class='custom-btn'>Okay</div><div class='custom-btn'>Delete</div>"

    img_html = f"<img class='window-img' src='{IMAGE_URL}'>" if show_image else ""
    
    st.markdown(f"""
    <div class="window-box">
        <div class="window-header">
            <span>📄 {title}</span>
            <span class="window-controls">&lt; &gt; C X</span>
        </div>
        <div class="window-body">
            <strong>Content:</strong><br>
            {text}<br>
            {img_html}
            <br>
            {btn_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 6. แสดงผลเนื้อหาตามหน้าที่เลือก (ดึงรูปแบบตามภาพดีไซน์)
lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut blandit risus ac eros malesuada, sollicitudin tempus dui malesuada. Suspendisse venenatis vitae diam vitae placerat. Integer consequat hendrerit."

if page == "All Overview (ดูทั้งหมด)" or page == "1. Introduction & Evolution":
    st.subheader("🌐 Section 1: Foundations")
    col1, col2 = st.columns(2)
    with col1:
        draw_window("Introduction to Technology", lorem_text, show_image=True, btn_type="okay")
    with col2:
        draw_window("Evolution of Technology", lorem_text, show_image=False, btn_type="okay_cancel")

if page == "All Overview (ดูทั้งหมด)" or page == "2. Tech Categories (IT, Comm, Edu)":
    st.write("---")
    st.subheader("📲 Section 2: Core Technologies")
    col1, col2, col3 = st.columns(3)
    with col1:
        draw_window("Information Technology", lorem_text, show_image=True, btn_type="okay")
    with col2:
        draw_window("Communication Technology", lorem_text, show_image=True, btn_type="okay")
    with col3:
        draw_window("Education Technology", lorem_text, show_image=True, btn_type="okay")

if page == "All Overview (ดูทั้งหมด)" or page == "3. AI & Environmental Tech":
    st.write("---")
    st.subheader("🤖 Section 3: Advanced Frontiers")
    col1, col2 = st.columns(2)
    with col1:
        draw_window("Artificial Intelligence & Automation", lorem_text, show_image=False, btn_type="okay")
    with col2:
        draw_window("Environmental Technology", lorem_text, show_image=False, btn_type="okay_delete")

if page == "All Overview (ดูทั้งหมด)" or page == "4. Ethical Issues & Future":
    st.write("---")
    st.subheader("🔮 Section 4: Implications & Future")
    col1, col2 = st.columns(2)
    with col1:
        draw_window("Ethical and Social Issues", lorem_text, show_image=True, btn_type="okay")
    with col2:
        draw_window("Conclusion & Future Outlook", "<strong>Conclusion:</strong><br>" + lorem_text, show_image=True, btn_type="okay")
