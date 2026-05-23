import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="centered",
)

# --- Global CSS Styling ---
# Custom CSS gives us the vibrant gradients, glass-like styling, and button animations seen in the video.
st.markdown("""
<style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    }
    
    /* Glassmorphism Container */
    .card {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 32px 0 rgba(31, 135, 211, 0.17);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 40px;
        text-align: center;
        color: #4a4a4a;
        margin-top: 50px;
    }
    
    /* Neon Glow Effects */
    .neon-text {
        font-family: 'Courier New', Courier, monospace;
        color: #ff4b4b;
        text-shadow: 0 0 10px rgba(255,75,75,0.5), 0 0 20px rgba(255,75,75,0.3);
        font-weight: bold;
    }
    
    /* Floating Animations */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .floating-cake {
        font-size: 80px;
        animation: float 3s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)


# --- State Management Initialization ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'wrong_password' not in st.session_state:
    st.session_state.wrong_password = False


# --- App Navigation Logic ---

# STEP 1: The Sweet Login Panel
if st.session_state.step == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("🔒 Sweet Login")
    st.write("Enter the secret key to unlock your surprise.")
    
    password = st.text_input("Secret Password", type="password", key="login_pass", label_visibility="collapsed")
    
    # Simple verification
    if st.button("Let's Go ✨", use_container_width=True):
        if password.lower() == "birthday":  # Change your secret password here
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
    st.markdown('<div class="card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white;">', unsafe_allow_html=True)
    st.subheader("💝 System Notification")
    st.markdown("<h3>There is a special surprise waiting just for you! 🌸✨</h3>", unsafe_allow_html=True)
    st.write("Are you ready to see what's inside?")
    
    if st.button("Open the Door 🎉", use_container_width=True):
        st.session_state.step = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 3: Magical Interactive Cake Time
elif st.session_state.step == 3:
    st.markdown('<div class="card" style="background: #111; color: #fff;">', unsafe_allow_html=True)
    st.markdown('<h2 class="neon-text">✨ Magical Cake Time! ✨</h2>', unsafe_allow_html=True)
    
    # Animated graphic placeholder
    st.markdown('<div class="floating-cake">🎂</div>', unsafe_allow_html=True)
    st.write("Make a wish and click below to blow out the virtual candles!")
    
    if st.button("Blow out Candles 🌬️", use_container_width=True):
        with st.spinner("Lighting up the skies..."):
            time.sleep(1.5)  # Creating a suspenseful transition delay
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# STEP 4: The Grand Finale Celebration
elif st.session_state.step == 4:
    # Trigger native Streamlit celebratory overlay effects
    st.balloons()
    st.snow()
    
    st.markdown('<div class="card" style="background: rgba(0,0,0,0.85); color: #fff; border: 2px solid #ff4b4b;">', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #ff4b4b; font-size: 3rem;">✨ HAPPY BIRTHDAY! ✨</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="font-size: 1.2rem; line-height: 1.6; color: #fecfef;">
        May your year ahead be filled with endless laughter, incredible adventures, 
        and spectacular joy. You deserve the absolute best today and every day! 🥂🍰
    </p>
    """, unsafe_allow_html=True)
    
    # Option to restart the experience loop
    if st.button("Replay Surprise 🔄", type="secondary"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
