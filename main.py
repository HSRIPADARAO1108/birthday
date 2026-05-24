import streamlit as st
import time
import base64
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="centered",
)

# 🛠️ HARDCODE YOUR FILE PATH HERE
# Example paths: "my_photo.jpg" or "C:/Users/Name/Pictures/birthday_bg.png"
BACKGROUND_IMAGE_PATH = "your_photo_here.jpg" 

# --- State Management Initialization ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'wrong_password' not in st.session_state:
    st.session_state.wrong_password = False

# --- Core Background Logic ---
bg_style = ""

# Check if the hardcoded image file path actually exists on your machine
if os.path.exists(BACKGROUND_IMAGE_PATH):
    with open(BACKGROUND_IMAGE_PATH, "rb") as image_file:
        bytes_data = image_file.read()
        b64_bg = base64.b64encode(bytes_data).decode()
        
    # Apply full screen background image only during step 1 (Login Screen)
    if st.session_state.step == 1:
        bg_style = f"""
        .stApp {{
            background: url("data:image/png;base64,{b64_bg}") no-repeat center center fixed !important;
            background-size: cover !important;
        }}
        """
    else:
        # Subtle celebration background transition once they log in
        bg_style = """
        .stApp {
            background: linear-gradient(135deg, #2c3e50 0%, #000000 100%) !important;
        }
        """
else:
    # Fallback to original pink gradient if the file path is incorrect or missing
    bg_style = """
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%) !important;
    }
    """

# --- Global CSS Styling ---
st.markdown(f"""
<style>
    {bg_style}
    
    /* Hide the top Streamlit decoration bar and main menu button */
    #MainMenu, header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    
    /* Frosted glass container card */
    .card {{
        background: rgba(255, 255, 255, 0.12);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 40px;
        text-align: center;
        color: #ffffff;
        margin-top: 60px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
    }}
    
    .card h1, .card h2, .card h3, .card p {{
        color: #ffffff !important;
    }}
    
    /* Neon Text for Cake Screen */
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

# STEP 1: The Sweet Login Panel (Displays your custom image background)
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
    
    # Simple alert block if your file path isn't pointing to a valid photo yet
    if not os.path.exists(BACKGROUND_IMAGE_PATH):
        st.info(f"💡 Developer Note: Place your photo at '{BACKGROUND_IMAGE_PATH}' or update line 12 in the script to view your custom background image.")
        
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 2: The Gateway / Transition Message
elif st.session_state.step == 2:
    st.markdown('<div class="card" style="background: rgba(79, 172, 254, 0.4); border: 1px solid rgba(255,255,255,0.3);">', unsafe_allow_html=True)
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
