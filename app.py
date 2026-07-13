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

# หักค่าใช้จ่ายตามกฎหมาย (50% แต่ไม่เกิน 100,000 บาท สำหรับเงินเดือน/รายได้ทั่วไป)
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

# แสดงตารางขั้นบันไดภาษีและกราฟ (เฉพาะกรณีที่มีภาษีต้องจ่าย)
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
    st.pyplot(fig)
