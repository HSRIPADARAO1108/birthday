import streamlit as st
import time
import base64

# --- Page Configuration ---
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="centered",
)

# --- State Management Initialization ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'wrong_password' not in st.session_state:
    st.session_state.wrong_password = False

# --- Sidebar Image Uploader ---
st.sidebar.title("🛠️ Setup Panel")
uploaded_file = st.sidebar.file_uploader("Upload Login Background Image", type=["png", "jpg", "jpeg"])

bg_style = ""
# If an image is uploaded, convert it to a Base64 string for CSS insertion
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    b64_bg = base64.b64encode(bytes_data).decode()
    # Apply full screen background image cover settings
    bg_style = f"""
    .stApp {{
        background: url("data:image/png;base64,{b64_bg}") no-repeat center center fixed !important;
        background-size: cover !important;
    }}
    """
else:
    # Fallback to the original pink gradient if no photo is uploaded yet
    bg_style = """
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%) !important;
    }
    """

# --- Global CSS Styling ---
st.markdown(f"""
<style>
    {bg_style}
    
    /* Glassmorphic Container - Frosted glass look helps text pop over busy photos */
    .card {{
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 40px;
        text-align: center;
        color: #ffffff; /* Swapped to white text for better visibility on custom images */
        margin-top: 50px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}
    
    .card h1, .card h2, .card h3, .card p {{
        color: #ffffff !important;
    }}
    
    /* Neon Glow Effects */
    .neon-text {{
        font-family: 'Courier New', Courier, monospace;
        color: #ff4b4b !important;
        text-shadow: 0 0 10px rgba(255,75,75,0.5), 0 0 20px rgba(255,75,75,0.3);
        font-weight: bold;
    }}
    
    /* Floating Animations */
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}
    .floating-cake {{
        font-size: 80px;
        animation: float 3s ease-in-out infinite;
    }}
</style>
""", unsafe_allow_html=True)


# --- App Navigation Logic ---

# STEP 1: The Sweet Login Panel
if st.session_state.step == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h1>🔒 Sweet Login</h1>", unsafe_allow_html=True)
    st.markdown("<p>Enter the secret key to unlock your surprise.</p>", unsafe_allow_html=True)
    
    password = st.text_input("Secret Password", type="password", key="login_pass", label_visibility="collapsed")
    
    if st.button("Let's Go ✨", use_container_width=True):
        if password.lower() == "birthday":
            st.session_state.step = 2
            st.session_state.wrong_password = False
            st.rerun()
        else:
            st.session_state.wrong_password = True
            
    if st.session_state.wrong_password:
        st.error("Oops! Wrong password. Hint: Try 'birthday'")
        
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 2: The Gateway / Transition Message
elif st.session_state.step == 2:
    st.markdown('<div class="card" style="background: rgba(79, 172, 254, 0.7); border: 1px solid rgba(255,255,255,0.4);">', unsafe_allow_html=True)
    st.markdown("<h3>💝 System Notification</h3>", unsafe_allow_html=True)
    st.markdown("<h2>There is a special surprise waiting just for you! 🌸✨</h2>", unsafe_allow_html=True)
    st.markdown("<p>Are you ready to see what's inside?</p>", unsafe_allow_html=True)
    
    if st.button("Open the Door 🎉", use_container_width=True):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 3: Magical Interactive Cake Time
elif st.session_state.step == 3:
    st.markdown('<div class="card" style="background: rgba(17, 17, 17, 0.85); border: 1px solid #ff4b4b;">', unsafe_allow_html=True)
    st.markdown('<h2 class="neon-text">✨ Magical Cake Time! ✨</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="floating-cake">🎂</div>', unsafe_allow_html=True)
    st.markdown("<p>Make a wish and click below to blow out the virtual candles!</p>", unsafe_allow_html=True)
    
    if st.button("Blow out Candles 🌬️", use_container_width=True):
        with st.spinner("Lighting up the skies..."):
            time.sleep(1.5)
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 4: The Grand Finale Celebration
elif st.session_state.step == 4:
    st.balloons()
    st.snow()
    
    st.markdown('<div class="card" style="background: rgba(0,0,0,0.85); border: 2px solid #ff4b4b;">', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #ff4b4b !important; font-size: 3rem;">✨ HAPPY BIRTHDAY! ✨</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="font-size: 1.2rem; line-height: 1.6; color: #fecfef !important;">
        May your year ahead be filled with endless laughter, incredible adventures, 
        and spectacular joy. You deserve the absolute best today and every day! 🥂🍰
    </p>
    """, unsafe_allow_html=True)
    
    if st.button("Replay Surprise 🔄", type="secondary"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
