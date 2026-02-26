import streamlit as st
from PIL import Image

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="BotBuddy Cikgu Moon",
    page_icon="🌈",
    layout="centered"
)

# ======================
# LOAD LOGO
# ======================
logo = Image.open("assets/logo.png")

# ======================
# CUSTOM CSS (UNICORN UI UPGRADE)
# ======================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"]  {
    font-family: 'Baloo 2', cursive !important;
}

body {
    background: linear-gradient(135deg, #ffe6f7, #e6f7ff, #f0fff0);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* BESARKAN FONT LABEL */
label {
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* BESARKAN INPUT TEXT */
input, textarea, select {
    font-size: 17px !important;
    border-radius: 15px !important;
}

/* Badge */
.badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    background: #f3e8ff;
    margin-right: 8px;
    font-size: 15px;
}

/* Button Style */
.stButton>button {
    background: linear-gradient(90deg,#ff9ecf,#b388ff);
    color: white;
    border-radius: 25px;
    height: 3.2em;
    font-weight: bold;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg,#ff6fb5,#9c6bff);
}

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER ROW (LOGO + TITLE SEBELAH)
# ======================
col_logo, col_title = st.columns([1,2])

with col_logo:
    st.image(logo, width=260)

with col_title:
    st.markdown("""
    <h1 style='font-size:38px; margin-bottom:5px;'>🌈 Borang Poster Comel ✨</h1>
    <p style='font-size:20px;'>Isi ikut kotak — saya jana prompt imej + ayat poster 🥰</p>
    """, unsafe_allow_html=True)

st.markdown("""
<span class="badge">🌸 Pastel</span>
<span class="badge">🦄 Comel</span>
<span class="badge">💜 Chibi vibe</span>
<span class="badge">📋 Siap copy</span>
""", unsafe_allow_html=True)

st.markdown("---")

# ======================
# FORM
# ======================
tajuk = st.text_input("📌 Tajuk Poster")

col1, col2 = st.columns(2)

with col1:
    sasaran = st.text_input("🎯 Sasaran")
    masa = st.text_input("⏰ Masa")

with col2:
    tarikh = st.text_input("📅 Tarikh")
    lokasi = st.text_input("📍 Lokasi")

mesej = st.text_area("💬 Mesej Utama / Objektif")

col3, col4, col5 = st.columns(3)

with col3:
    saiz = st.selectbox("📐 Saiz", ["A4 portrait", "A4 landscape", "Square 1:1"])

with col4:
    gaya = st.selectbox(
    "🎨 Gaya",
    [
        "Chibi Educational",
        "Chibi Scrapbook",
        "Chibi Sketchnotes",
        "Studygram Notes",
        "Komik Edukasi",
        "Chibi Edu Sticker",
        "3D Pixar Crochet",
        "Sticker Cut / Diecut",
        "Chibi Doodle",
        "Graffiti / Street Art",
        "Pixar Felt Sticker",
        "Minecraft Style",
        "Roblox Style",
        "Anime Style"
    ]
)

with col5:
    warna = st.selectbox("🌈 Warna tema", ["Pastel mix", "Pink unicorn", "Rainbow soft"])

col6, col7 = st.columns(2)

with col6:
    elemen = st.text_input("✅ Elemen wajib")

with col7:
    nada = st.selectbox("🎵 Nada ayat", ["Mesra & semangat (BM)", "Formal sekolah", "Fun & ceria"])

st.markdown("---")

col_btn1, col_btn2 = st.columns([1,2])

with col_btn1:
    if st.button("Reset"):
        st.rerun()

with col_btn2:
    generate = st.button("✨ Jana Prompt Poster")

# ======================
# GENERATE PROMPT
# ======================
if generate:
    prompt = f"""
Cute chibi pastel classroom poster.
Theme: {tajuk}
Target: {sasaran}
Date: {tarikh}
Time: {masa}
Location: {lokasi}
Main message: {mesej}
Style: {gaya}
Color theme: {warna}
Required elements: {elemen}
Tone: {nada}
High resolution, soft lighting, kawaii illustration, storybook style.
"""

    st.success("🌟 Prompt berjaya dijana!")
    st.text_area("📋 Salin Prompt:", prompt, height=250)
