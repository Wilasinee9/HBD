import streamlit as st
import time

# ตั้งค่าหน้าเว็บให้ดูน่ารัก
st.set_page_config(
    page_title="Happy Birthday My Cake! 🎂",
    page_icon="💖",
    layout="centered"
)

# ใช้ CSS ตกแต่งพื้นหลังและฟอนต์เพิ่มความน่ารัก
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5; /* สีชมพูอ่อน LavenderBlush */
    }
    h1 {
        color: #FF69B4; /* สีชมพูเข้ม HotPink */
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .sweet-text {
        color: #FF1493;
        font-size: 20px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัวของเว็บ
st.markdown("<h1>Happy Birthday to You! 🎂✨</h1>", unsafe_allow_html=True)
st.write("")

# ใส่รูปแฟนหรือรูปคู่ (เปลี่ยนลิงก์รูปตรงนี้ได้เลย)
# แนะนำให้ใช้ลิงก์รูปที่อัปโหลดไว้บนเน็ต หรือจะเอาใส่ไว้ในโฟลเดอร์เดียวกับโค้ดก็ได้
st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=500", 
         caption="ขอบคุณที่มีเธออยู่ในทุกๆ วันนะ 💕", 
         use_container_width=True)

st.write("---")

# ปุ่มกดเพื่อจุดพลุฉลอง
st.markdown("<p class='sweet-text'>กดปุ่มข้างล่างนี้เพื่อรับของขวัญซิ! 👇</p>", unsafe_allow_html=True)

if st.button("✨ คลิกตรงนี้เลยคุณแฟน ✨", use_container_width=True):
    # ยิงลูกโป่งและพลุฉลองของ Streamlit
    st.balloons()
    st.snow()
    st.success("🎉 สุขสันต์วันเกิดนะค้าบ! ขอให้มีความสุขมากๆ ยิ้มเยอะๆ ในทุกๆ วันเลยนะ 🧸💖")
    
    # หน่วงเวลาให้ของขวัญค่อยๆ โผล่ขึ้นมา
    time.sleep(1)
    st.markdown("""
    ### 💌 ความในใจถึงเธอ...
    * **ขอบคุณความน่ารัก:** ที่คอยเป็นรอยยิ้มให้กันเสมอมานะ
    * **สัญญาใจ:** ปีนี้และปีต่อๆ ไป ก็จะคอยอยู่ข้างๆ คอยซัพพอร์ตเธอแบบนี้เรื่อยๆ เลย
    * **ของขวัญชิ้นใหญ่:** อยู่ที่เค้าแล้วนะ เย็นนี้เจอกันเดี๋ยวเอาไปให้ค้าบ! 🎁
    """)

st.write("---")

# ส่วนเพิ่มเติม: สไลเดอร์บอกระดับความรัก
st.subheader("📊 ระดับความรักที่เค้ามีให้เธอวันนี้")
love_level = st.slider("เลื่อนดูซิว่ารักแค่ไหน", 0, 100, 100)
if love_level == 100:
    st.write("🥰 เกินร้อยไปเลย! รักที่สุดในโลกกกกกก")
else:
    st.write("ง่ะ... เลื่อนให้สุด 100% เลยนะ!")
