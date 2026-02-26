import streamlit as st
from PIL import Image
import base64

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="BotBuddy Cikgu Moon",
    page_icon="🌙",
    layout="centered"
)

# =========================
# LOAD LOGO
# =========================
logo = Image.open("assets/logo.png")

# =========================
# CUSTOM CSS (PASTEL UI)
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fceff9, #e0f7fa);
}

.main {
    background-color: #ffffffcc;
    padding: 2rem;
    border-radius: 25px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    color: #ff69b4;
}

.stButton>button {
    background-color: #ffb6c1;
    color: white;
    border-radius: 20px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

.stTextInput>div>div>input {
    border-radius: 15px;
}

.stTextArea textarea {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.image(logo, width=180)
st.markdown("<h1>Prompt Generator 🌙<br>BOTBUDDY CIKGU MOON</h1>", unsafe_allow_html=True)
st.markdown("✨ Jana prompt imej comel gaya chibi seperti dalam contoh ✨")

st.divider()

# =========================
# FORM INPUT
# =========================
tajuk = st.text_input("📌 Tajuk Poster")
sasaran = st.text_input("🎯 Sasaran")
tarikh = st.text_input("📅 Tarikh")
masa = st.text_input("⏰ Masa")
lokasi = st.text_input("📍 Lokasi")
mesej = st.text_area("💬 Mesej Utama / Objektif")

saiz = st.selectbox("📐 Saiz Poster", ["A4 Portrait", "A4 Landscape", "Square 1:1"])
gaya = st.selectbox("🎨 Gaya", ["Chibi kartun pastel", "Anime lembut", "Cute classroom illustration"])
warna = st.selectbox("🌈 Warna Tema", ["Pastel pink + mint", "Pastel biru + ungu", "Soft rainbow pastel"])

st.divider()

# =========================
# GENERATE PROMPT
# =========================
if st.button("✨ Jana Prompt Poster"):
    
    prompt = f"""
    Cute chibi style classroom poster illustration.
    Theme: {tajuk}
    Target audience: {sasaran}
    Date: {tarikh}
    Time: {masa}
    Location: {lokasi}

    Main message: {mesej}

    Style: {gaya}
    Color palette: {warna}
    Size format: {saiz}

    Include adorable hijab teacher mascot holding laptop,
    pastel classroom background, chalkboard,
    soft lighting, kawaii illustration, high resolution,
    cute, wholesome, soft shading, storybook style.
    """

    st.success("🌟 Prompt Berjaya Dijana!")
    st.text_area("📋 Salin Prompt Ini:", prompt, height=300)
