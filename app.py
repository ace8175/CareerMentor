import streamlit as st
from PIL import Image

HUGGING_SPACE_CHATBOT_URL = "https://udify.app/chatbot/xqi6NTiBEQe97sCN"
# Page Config
st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: #1B3663;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }}
        .main-title {{
            color: #35577d;
            font-size: 3rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.5rem;
        }}
        .tagline {{
            font-size: 1.3rem;
            color: #d1d5db;
            text-align: center;
            margin-bottom: 3rem;
        }}
        .section-title {{
            color: #35577d;
            font-size: 1.8rem;
            font-weight: bold;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        .feature-box {{
            background: rgba(53, 87, 125, 0.15);
            padding: 20px;
            border-radius: 12px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
        .cta-button {{
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 0.9rem;
            color: #9ca3af;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown("<h1 class='main-title'>AI Career Mentor 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>Smart resume insights for students & freshers in India</p>", unsafe_allow_html=True)

# About Section
st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
st.write("""
The **AI Career Mentor** helps you understand your resume like a recruiter would. 
It highlights your strengths, points out weaknesses, suggests improvements, and adds industry-relevant keywords.

Your personal AI-powered guide for making your resume stand out.
""")

# Features Section
st.markdown("<h2 class='section-title'>Features</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='feature-box'>✅ Resume Strengths Analysis</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='feature-box'>⚡ Weaknesses & Gaps Detection</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='feature-box'>🎯 Industry Keyword Suggestions</div>", unsafe_allow_html=True)

col4, col5 = st.columns([1,1])
with col4:
    st.markdown("<div class='feature-box'>📈 Step-by-Step Improvements</div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div class='feature-box'>💡 Motivational Career Guidance</div>", unsafe_allow_html=True)

# CTA Button
#st.markdown("""
#<div class='cta-button'>
#    <a href="#" style="background:#35577d; color:white; padding:15px 25px; border-radius:8px; text-decoration:none; font-size:1.2rem; font-weight:600;">
#        🚀 Try the Mentor Bot (Coming Soon)
#    </a>
#</div>
#""", unsafe_allow_html=True)

st.markdown("""<iframe
 src="https://udify.app/chatbot/xqi6NTiBEQe97sCN"
 style="width: 100%; height: 100%; min-height: 700px"
 frameborder="0"
 allow="microphone">
</iframe>""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made with ❤️ by Rohit | <a href='https://github.com/ace8175' style='color:#35577d;'>GitHub</a> | <a href='https://www.linkedin.com/in/rohit-sai-sharan-bagwar-6a305027a' style='color:#35577d;'>LinkedIn</a></div>", unsafe_allow_html=True)
