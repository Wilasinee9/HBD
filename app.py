import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. ตั้งค่าหน้าเว็บและดีไซน์เบื้องต้น
st.set_page_config(
    page_title="Thai Tax Calculator Pro 🇹🇭",
    page_icon="💰",
    layout="centered"
)

# 2. ปรับแต่ง UI ด้วย Custom CSS ให้สวยงาม น่าใช้งาน
st.markdown("""
    <style>
    /* ตั้งค่าฟอนต์และโทนสีพื้นหลังพาสเทลสะอาดตา */
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Sarabun', sans-serif !important;
        background-color: #F8FAFC;
    }
    
    /* สไตล์การ์ดหัวข้อใหญ่ */
    .header-card {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        padding: 30px;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
    }
    .header-card h1 {
        color: white !important;
        font-weight: 700;
        margin-bottom: 5px;
    }
    
    /* กล่องข้อแนะนำความปลอดภัย/ข้อมูลสรุป */
    .summary-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #10B981;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-top: 15px;
    }
    
    /* สไตล์ข้อความแนะนำในการประหยัดภาษี */
    .tips-box {
        background-color: #FFFBEB;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #FEF3C7;
        color: #D97706;
        font-size: 14px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# แสดงแถวหัวข้อสวยงาม
st.markdown("""
    <div class="header-card">
        <h1>🇹🇭 Thai Tax Calculator Pro</h1>
        <p>โปรแกรมคำนวณและวางแผนภาษีบุคคลธรรมดาเพื่อการออมเงินสูงสุด</p>
    </div>
""", unsafe_allow_html=True)

# ยินดีต้อนรับผู้ใช้งาน
st.write("กรอกข้อมูลรายได้และค่าลดหย่อนของคุณในแถบด้านล่าง ระบบจะคำนวณฐานภาษีแบบขั้นบันไดและแนะนำวิธีประหยัดภาษีให้อัตโนมัติ")

# --- ส่วนที่ 1: รายได้ ---
st.markdown("### 💵 1. ข้อมูลรายได้ทั้งปี")
income_col1, income_col2 = st.columns(2)

with income_col1:
    income_type = st.selectbox("รูปแบบรายได้หลัก", ["มนุษย์เงินเดือน (รายเดือน)", "ฟรีแลนซ์ / รายได้รวมทั้งปี"])

with income_col2:
    if income_type == "มนุษย์เงินเดือน (รายเดือน)":
        salary = st.number_input("เงินเดือนปัจจุบัน (บาท)", min_value=0, value=45000, step=5000)
        bonus = st.number_input("โบนัสที่ได้รับในปีนี้ (บาท)", min_value=0, value=0, step=5000)
        total_income = (salary * 12) + bonus
    else:
        total_income = st.number_input("รายรับรวมสุทธิทั้งปี (บาท)", min_value=0, value=540000, step=10000)

st.info(f"💰 **รายได้คำนวณรวมทั้งปีของคุณ:** {total_income:,.2f} บาท")


# --- ส่วนที่ 2: ค่าลดหย่อน (จัดกลุ่มเพื่อความสวยงามและใช้งานง่าย) ---
st.markdown("### 🏠 2. ค่าลดหย่อนและการออมเงิน")

exp1, exp2 = st.columns(2)
with exp1:
    st.markdown("**👪 ค่าลดหย่อนส่วนตัวและครอบครัว**")
    allowance_self = 60000  # หักส่วนตัวอัตโนมัติ 60,000 บาท
    st.caption("✓ หักลดหย่อนส่วนตัวอัตโนมัติ 60,000 บาท")
    
    has_spouse = st.checkbox("มีคู่สมรสที่ไม่มีรายได้ (-60,000 บาท)")
    children_count = st.number_input("จำนวนบุตร (คนละ -30,000 บาท)", min_value=0, value=0, step=1)
    
    allowance_spouse = 60000 if has_spouse else 0
    allowance_children = children_count * 30000
    family_total = allowance_self + allowance_spouse + allowance_children

with exp2:
    st.markdown("**🛡️ ประกัน สังคม และ ประกันชีวิต**")
    social_security = st.number_input("ประกันสังคมทั้งปี (บาท)", min_value=0, max_value=9000, value=9000, step=100)
    life_insurance = st.number_input("เบี้ยประกันชีวิต / ประกันสุขภาพ (สูงสุด 100,000 บาท)", min_value=0, max_value=100000, value=0, step=5000)
    insurance_total = social_security + life_insurance

# ส่วนลดหย่อนการลงทุนเชิงรุก (ฟีเจอร์เด่นช่วยวางแผนภาษี)
st.markdown("**📈 กองทุนรวมเพื่อการออมและการลงทุน (สิทธิประโยชน์ภาษี)**")
invest_col1, invest_col2, invest_col3 = st.columns(3)

with invest_col1:
    # SSF ซื้อได้สูงสุด 30% ของเงินได้ ไม่เกิน 200,000
    max_ssf = min(total_income * 0.3, 200000)
    ssf = st.number_input(f"กองทุน SSF (สูงสุด {max_ssf:,.0f})", min_value=0.0, max_value=max_ssf, value=0.0, step=5000.0)

with invest_col2:
    # RMF ซื้อได้สูงสุด 30% ของเงินได้ ไม่เกิน 500,000
    max_rmf = min(total_income * 0.3, 500000)
    rmf = st.number_input(f"กองทุน RMF (สูงสุด {max_rmf:,.0f})", min_value=0.0, max_value=max_rmf, value=0.0, step=5000.0)

with invest_col3:
    # Thai ESG ซื้อได้สูงสุด 30% ไม่เกิน 300,000 บาท
    max_tesg = min(total_income * 0.3, 300000)
    thai_esg = st.number_input(f"กองทุน Thai ESG (สูงสุด {max_tesg:,.0f})", min_value=0.0, max_value=max_tesg, value=0.0, step=5000.0)

# คำนวณขีดจำกัดรวมกองทุนเพื่อการเกษียณ (SSF + RMF + กองทุนสำรองเลี้ยงชีพ รวมกันห้ามเกิน 500,000 บาท)
investment_total = ssf + rmf + thai_esg
total_allowance = family_total + insurance_total + investment_total


# --- ส่วนที่ 3: ประมวลผลคำนวณเงินภาษี ---
# หักค่าใช้จ่ายตามกฎหมาย (50% ของรายได้ แต่ไม่เกิน 100,000 บาท)
expense = min(total_income * 0.5, 100000)
net_income = total_income - expense - total_allowance
if net_income < 0:
    net_income = 0

# ตารางคำนวณขั้นบันไดภาษีของประเทศไทย
brackets = [
    (150000, 0.00), (300000, 0.05), (500000, 0.10), (750000, 0.15),
    (1000000, 0.20), (2000000, 0.25), (5000000, 0.30), (float('inf'), 0.35)
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


# --- ส่วนที่ 4: หน้าจอสรุปผลลัพธ์ (UI สรุปผลเด่นชัด) ---
st.write("---")
st.markdown("### 📊 3. สรุปผลการประเมินภาษี")

# สรุปแบบ Metrics คู่
m_col1, m_col2 = st.columns(2)
with m_col1:
    st.metric(label="เงินได้สุทธิ (หลังหักค่าลดหย่อนแล้ว)", value=f"{net_income:,.2f} บาท")
with m_col2:
    if tax_total > 0:
        st.metric(label="ยอดภาษีที่ต้องจ่ายทั้งปี", value=f"{tax_total:,.2f} บาท", delta="ต้องชำระภาษี", delta_color="inverse")
    else:
        st.metric(label="ยอดภาษีที่ต้องจ่ายทั้งปี", value="0.00 บาท", delta="คุณได้รับยกเว้นภาษี 🎉")

# กล่องวิเคราะห์แนะนำการออมเงินอัจฉริยะ (Tax Optimizer Feature)
st.markdown("<div class='summary-box'>", unsafe_allow_html=True)
st.markdown("🎯 **บทวิเคราะห์และการวางแผน:**")
if tax_total > 0:
    possible_saving_investment = max_ssf - ssf + max_rmf - rmf + max_tesg - thai_esg
    if possible_saving_investment > 1000:
        st.markdown(f"💡 คุณยังมีสิทธิซื้อกองทุนลดหย่อนภาษีเหลืออยู่อีกประมาณ **{possible_saving_investment:,.2f} บาท** หากซื้อเพิ่มจะช่วยขยับฐานภาษีให้ต่ำลงและได้เงินคืนเพิ่มขึ้นอีกด้วยนะ!")
    else:
        st.markdown("👏 ยอดเยี่ยมมาก! คุณใช้สิทธิลดหย่อนการลงทุนเต็มเพดานหรือสิทธิเกือบสมบูรณ์แล้ว ช่วยเซฟเงินในกระเป๋าได้สูงสุด")
else:
    st.markdown("✨ รายได้และค่าลดหย่อนในปัจจุบันของคุณสมดุลดีมาก ทำให้คุณไม่มีภาระภาษีที่ต้องชำระในปีนี้ครับ")
st.markdown("</div>", unsafe_allow_html=True)

# ตารางแจกแจงแบบละเอียด
st.subheader("📋 รายละเอียดการคำนวณ")
summary_df = pd.DataFrame({
    "รายการวิเคราะห์": ["รายได้รวมทั้งปี", "หัก ค่าใช้จ่ายตามกฎหมาย (สูงสุด 100,000)", "หัก ค่าลดหย่อนทั้งหมด", "เงินได้สุทธิคงเหลือ"],
    "จำนวนเงิน (บาท)": [f"{total_income:,.2f}", f"- {expense:,.2f}", f"- {total_allowance:,.2f}", f"{net_income:,.2f}"]
})
st.table(summary_df)

# แสดงตารางแจกแจงแบบขั้นบันไดและกราฟวงกลม
if tax_total > 0:
    st.subheader("📈 ตารางแจกแจงภาษีตามฐานขั้นบันไดจริง")
    st.dataframe(pd.DataFrame(tax_details), use_container_width=True)

    # วาดรูปกราฟวงกลมแจกแจงการเงิน
    st.subheader("📉 สัดส่วนการกระจายรายได้ของคุณ")
    labels = ['เงินออมคงเหลือหลังภาษี', 'ค่าใช้จ่ายตามกฎหมาย', 'สิทธิประโยชน์ลดหย่อน', 'ภาษีที่ต้องจ่าย']
    sizes = [total_income - expense - total_allowance - tax_total, expense, total_allowance, tax_total]
    colors = ['#10B981', '#F59E0B', '#3B82F6', '#EF4444']
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  
    st.pyplot(fig)
