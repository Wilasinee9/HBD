import streamlit as st

# ตั้งค่าหน้าเว็บให้ธีมหวานๆ น่ารัก
st.set_page_config(
    page_title="Happy Birthday My Sweetheart 💖",
    page_icon="🎂",
    layout="centered"
)

# ใช้ CSS เพื่อตกแต่งหน้าต่างจำลอง (Window) ให้ดูมินิมอลและน่ารัก
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5;
    }
    .window-box {
        border: 2px solid #FFB6C1;
        border-radius: 10px;
        padding: 20px;
        background-color: #FFFFFF;
        box-shadow: 5px 5px 0px #FFB6C1;
        margin-bottom: 25px;
    }
    .window-header {
        border-bottom: 2px solid #FFE4E1;
        padding-bottom: 10px;
        margin-bottom: 15px;
        color: #FF69B4;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
    }
    h1, h2, h3 {
        color: #FF1493 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# URL รูปภาพทุ่งดอกไม้น่ารักๆ ตาม Reference ของคุณ
IMG_URL = "https://images.unsplash.com/photo-1576085898323-218337e3343c?w=600"

# --- SESSION STATE เพื่อเปลี่ยนหน้า ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# ----------------------------------------
# 1. หน้า HOME
# ----------------------------------------
if st.session_state.page == 'Home':
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Home</span><span>< > C</span></div>', unsafe_allow_html=True)
    st.markdown("# The Impact of \n# You in My Modern World 🌎💖")
    st.write("ยินดีต้อนรับเข้าสู่เว็บไซต์บันทึกเรื่องราวความรักและวันเกิดของเธอคนดี")
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start ✨", use_container_width=True):
            st.session_state.page = 'Intro'
            st.rerun()
    with col2:
        if st.button("Cancel ❌", use_container_width=True):
            st.warning("ง่ะ อย่าเพิ่งกดแคนเซิลเซ่! ไปดูก่อนเร็ววว")
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 2. หน้า INTRODUCTION
# ----------------------------------------
elif st.session_state.page == 'Intro':
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Content</span><span>☑ < > C</span></div>', unsafe_allow_html=True)
    st.markdown("## Introduction to \n## Our Journey Together 👩‍❤️‍👨")
    st.write("กาลครั้งหนึ่งนานมาแล้ว... ตั้งแต่วันแรกที่เธอเดินเข้ามาในชีวิต จากโลกสีเทาๆ ก็กลายเป็นโลกสีชมพูพาสเทลทันที ขอบคุณที่เกิดมาให้รักนะ")
    st.write("")
    
    if st.button("Okay แล้วไปต่อกันเลย ➡️", use_container_width=True):
        st.session_state.page = 'Evolution'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 3. หน้า EVOLUTION
# ----------------------------------------
elif st.session_state.page == 'Evolution':
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Content</span><span>< > C</span></div>', unsafe_allow_html=True)
    st.markdown("## Evolution of \n## Our Love Story 📈💕")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**วันแรกที่เจอ:** แอบเขินแอบมอง ไม่กล้าทัก")
        st.write("**หนึ่งเดือนผ่านไป:** คุยเก่ง โทรหาเช้าเย็น")
        st.write("**ปัจจุบัน:** ขาดเธอไม่ได้แล้ว หัวใจมันเรียกร้อง!")
        if st.button("Okay 💖", use_container_width=True):
            st.session_state.page = 'Main_Content'
            st.rerun()
    with col2:
        st.write("วันเวลาผ่านไป แต่ความน่ารักของเธอไม่เคยลดลงเลย มีแต่จะเพิ่มขึ้นทุกวันๆ จนใจเจ็บไปหมดแล้วเนี่ย")
        if st.button("Cancel 🥺", use_container_width=True):
            st.info("ยกเลิกไม่ได้หรอก รักไปแล้วรักเลย!")
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 4. หน้าเนื้อหาหลัก (รวมการ์ด 4 ส่วน)
# ----------------------------------------
elif st.session_state.page == 'Main_Content':
    
    # ส่วนที่ 1: Information Technology -> Information about My Sweetheart
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Information about You</span><span>Content</span></div>', unsafe_allow_html=True)
    st.markdown("### 🌸 ยัยหนูของเค้า")
    st.write("เจ้าของวันเกิดผู้น่ารักที่สุดในสามโลก นิสัยดื้อนิดๆ เอาใจเก่งหน่อยๆ ขี้งอนเป็นที่หนึ่ง แต่ก็น่ารักเป็นที่หนึ่งเหมือนกัน!")
    st.image(IMG_URL, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ส่วนที่ 2: Communication Technology -> Communication
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Communication</span><span>Content</span></div>', unsafe_allow_html=True)
    st.markdown("### 📱 สายใยของเรา")
    st.write("ไม่ว่าจะอยู่ใกล้หรือไกล แชทสีชมพูของเราไม่เคยเงียบเหงา ขอบคุณที่คอยตอบไว และคอยส่งสติกเกอร์หมีอ้วนมาอ้อนเสมอนะ")
    st.image(IMG_URL, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ส่วนที่ 3: Education Technology -> Future Learning
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Future Learning</span><span>☑ < > C</span></div>', unsafe_allow_html=True)
    st.markdown("### 📚 เรียนรู้ที่จะรักกัน")
    st.write("การมีเธอทำให้เค้าได้เรียนรู้สิ่งใหม่ๆ เรียนรู้ที่จะเอาใจใส่ เรียนรู้ที่จะเติบโตเป็นผู้ใหญ่ที่ดีขึ้นเพื่อเธอ")
    if st.button("Ok จ้า 🥰", use_container_width=True):
        pass
    st.markdown('</div>', unsafe_allow_html=True)

    # ส่วนที่ 4: Artificial Intelligence -> My True Intelligent Partner
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] My Best Partner</span><span>Content</span></div>', unsafe_allow_html=True)
    st.markdown("### 🤖 ยิ่งกว่า AI ก็ใจเธอนี่แหละ")
    st.write("บอตที่ไหนก็ไม่รู้ใจเท่าเธอ เธอฉลาดที่สุดที่รู้วิธีทำให้เค้ายิ้มได้ในวันที่เหนื่อยล้า ขอบคุณที่เป็นเซฟโซนที่ดีที่สุดนะ")
    st.image(IMG_URL, use_container_width=True)
    
    st.write("---")
    if st.button("ไปดูหน้าถัดไปกันเถอะ 🚀", use_container_width=True):
        st.session_state.page = 'Env_and_Ethic'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 5. หน้า ENVIRONMENTAL & ETHICAL ISSUES
# ----------------------------------------
elif st.session_state.page == 'Env_and_Ethic':
    
    # ส่วนที่ 1: Environmental Technology -> Our Love Environment
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Our Environment</span><span>☑ < > C</span></div>', unsafe_allow_html=True)
    st.markdown("### 🌿 บรรยากาศที่มีแต่เรา")
    st.write("ไม่ว่าจะไปเที่ยวทะเล ภูเขา หรือแค่คาเฟ่แถวบ้าน ขอแค่มีเธออยู่ด้วย ทุกที่ก็กลายเป็นสถานที่ที่สวยงามและมีความสุขที่สุด")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Okay ปลื้มปริ่ม 🌸", use_container_width=True):
            st.balloons()
    with col2:
        if st.button("Delete ความเศร้าออกไป 🗑️", use_container_width=True):
            st.snow()
    st.markdown('</div>', unsafe_allow_html=True)

    # ส่วนที่ 2: Ethical and Social Issues -> Promises
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Our Promises</span><span>Content</span></div>', unsafe_allow_html=True)
    st.markdown("### 🤝 สัญญาใจสายใยเราสอง")
    st.write("1. จะไม่แอบหนีไปนอนก่อนโดยไม่บอก \n2. จะเป็นผู้ฟังที่ดีเวลาเธอระบาย \n3. จะรักและซัพพอร์ตเธอในทุกๆ เส้นทางที่เธอเลือก")
    st.image(IMG_URL, use_container_width=True)
    
    st.write("---")
    if st.button("ไปหน้าสุดท้ายกันเถอะคุณแฟน! 🎁", use_container_width=True):
        st.session_state.page = 'Conclusion'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------
# 6. หน้า CONCLUSION
# ----------------------------------------
elif st.session_state.page == 'Conclusion':
    st.markdown('<div class="window-box"><div class="window-header"><span>[X] Conclusion & Future Outlook</span><span>☑ Conclusion</span></div>', unsafe_allow_html=True)
    st.markdown("## Happy Birthday & \n## Future Outlook 🎂🎉")
    st.write("สุขสันต์วันเกิดนะค้าบที่รัก! ขอให้ปีนี้เป็นปีที่ยอดเยี่ยม มีแต่รอยยิ้ม ไม่เจ็บไม่ป่วย ร่ำรวยความสุข และอยู่เป็นความสดใสให้เค้าไปนานๆ เลยนะ!")
    st.write("")
    
    # ปุ่มเปิดเอฟเฟกต์พลุฉลอง
    st.balloons()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ok รักเค้ามั้ย? 😍", use_container_width=True):
            st.success("งุ้ยยย เขินเลย รักเหมือนกันนะ!")
    with col2:
        if st.button("Yes รักที่สุด! ❤️", use_container_width=True):
            st.snow()
            st.success("เย้! แฟนใครเนี่ยน่ารักจัง")
            
    st.write("")
    if st.button("🔄 ย้อนกลับไปหน้าแรก", use_container_width=True):
        st.session_state.page = 'Home'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
