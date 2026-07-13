import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="โปรแกรมคำนวณภาษีเงินได้บุคคลธรรมดา 🇹🇭",
    page_icon="💰",
    layout="centered"
)

st.title("💰 โปรแกรมคำนวณภาษีเงินได้บุคคลธรรมดา")
st.write("เครื่องมือช่วยวางแผนและคำนวณภาษีเงินได้เบื้องต้นอย่างง่าย")

# --- ส่วนที่ 1: รับข้อมูลรายได้ ---
st.header("1. รายได้รวมทั้งปี")
income_type = st.radio("รูปแบบการระบุรายได้", ["รายเดือน (เงินเดือน)", "รายปีรวม"])

if income_type == "รายเดือน (เงินเดือน)":
    monthly_income = st.number_input("เงินเดือน (บาท)", min_value=0, value=30000, step=1000)
    bonus = st.number_input("โบนัส/รายได้อื่นๆ ทั้งปี (บาท)", min_value=0, value=0, step=1000)
    total_income = (monthly_income * 12) + bonus
else:
    total_income = st.number_input("รายได้ทั้งปี (บาท)", min_value=0, value=360000, step=5000)

st.info(f"📊 **รายได้รวมทั้งปีของคุณคือ:** {total_income:,.2f} บาท")

# --- ส่วนที่ 2: ค่าใช้จ่ายและค่าลดหย่อน ---
st.header("2. ค่าใช้จ่ายและค่าลดหย่อน")

# หักค่าใช้จ่ายตามกฎหมาย (50% แต่ไม่เกิน 100,000 บาท สำหรับเงินเดือน)
expense = min(total_income * 0.5, 100000)

# ค่าลดหย่อนพื้นฐาน
allowance_self = 60000  # ลดหย่อนส่วนตัว

st.subheader("🏠 ค่าลดหย่อนครอบครัวและการลงทุน")
has_spouse = st.checkbox("มีคู่สมรส (ไม่มีรายได้) [-60,000 บาท]")
children_count = st.number_input("จำนวนบุตร (คนที่ 1 เป็นต้นไป) [คนละ -30,000 บาท]", min_value=0, value=0, step=1)
social_security = st.number_input("ประกันสังคมทั้งปี (สูงสุด 9,000 บาท)", min_value=0, max_value=9000, value=9000, step=100)
other_allowance = st.number_input("ค่าลดหย่อนอื่นๆ (เช่น ประกันชีวิต, RMF, SSF, Easy E-Receipt) (บาท)", min_value=0, value=0, step=1000)

# คำนวณค่าลดหย่อนรวม
allowance_spouse = 60000 if has_spouse else 0
allowance_children = children_count * 30000
total_allowance = allowance_self + allowance_spouse + allowance_children + social_security + other_allowance

# --- ส่วนที่ 3: คำนวณเงินได้สุทธิ ---
net_income = total_income - expense - total_allowance
if net_income < 0:
    net_income = 0

# --- ส่วนที่ 4: คำนวณภาษีแบบขั้นบันได ---
brackets = [
    (150000, 0.00),
    (300000, 0.05),
    (500000, 0.10),
    (750000, 0.15),
    (1000000, 0.20),
    (2000000, 0.25),
    (5000000, 0.30),
    (float('inf'), 0.35)
]

tax_total = 0
previous_limit = 0
tax_details = []

remaining_income = net_income

for limit, rate in brackets:
    range_size = limit - previous_limit
    if remaining_income > range_size:
        income_in_bracket = range_size
        tax_in_bracket = income_in_bracket * rate
        remaining_income -= range_size
    else:
        income_in_bracket = remaining_income
        tax_in_bracket = income_in_bracket * rate
        remaining_income = 0
    
    if income_in_bracket > 0 or previous_limit == 0:
        tax_details.append({
            "ช่วงเงินได้สุทธิ": f"{previous_limit:,.0f} - {('ขึ้นไป' if limit == float('inf') else f'{limit:,.0f}')}",
            "อัตราภาษี": f"{rate*100:.0f}%",
            "เงินได้ในขั้น": f"{income_in_bracket:,.2f}",
            "ภาษีที่ต้องจ่าย": f"{tax_in_bracket:,.2f}"
        })
    
    tax_total += tax_in_bracket
    previous_limit = limit
    if remaining_income <= 0:
        break

# --- ส่วนที่ 5: แสดงผลลัพธ์ ---
st.write("---")
st.header("📋 สรุปผลการคำนวณภาษี")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="เงินได้สุทธิ (หลังหักลดหย่อน)", value=f"{net_income:,.2f} บาท")
with col2:
    if tax_total > 0:
        st.metric(label="ภาษีที่ต้องชำระทั้งปี", value=f"{tax_total:,.2f} บาท", delta="- ต้องจ่าย", delta_color="inverse")
    else:
        st.metric(label="ภาษีที่ต้องชำระทั้งปี", value="0.00 บาท", delta="ไม่ต้องจ่ายภาษี 🎉")

# แสดงแจกแจงแบบตาราง
st.subheader("📝 รายละเอียดการคำนวณ")
summary_data = {
    "รายการ": ["รายได้รวมทั้งปี", "หัก ค่าใช้จ่ายตามกฎหมาย", "หัก ค่าลดหย่อนรวม", "เงินได้สุทธิคงเหลือ"],
    "จำนวนเงิน (บาท)": [f"{total_income:,.2f}", f"- {expense:,.2f}", f"- {total_allowance:,.2f}", f"{net_income:,.2f}"]
}
st.table(pd.DataFrame(summary_data))

# แสดงตารางขั้นบันไดภาษี
if tax_total > 0:
    st.subheader("📊 ตารางแจกแจงภาษีแบบขั้นบันได")
    st.dataframe(pd.DataFrame(tax_details), use_container_width=True)

    # วาดกราฟวงกลมแสดงสัดส่วนเงิน
    st.subheader("📉 สัดส่วนการกระจายรายได้ของคุณ")
    labels = ['เงินคงเหลือหลังภาษี', 'ค่าใช้จ่ายกฎหมาย', 'ค่าลดหย่อน', 'ภาษีที่ต้องจ่าย']
    sizes = [net_income - tax_total, expense, total_allowance, tax_total]
    colors = ['#4CAF50', '#FF9800', '#2196F3', '#F44336']
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  
    st.pyplot(fig)    }
    
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
