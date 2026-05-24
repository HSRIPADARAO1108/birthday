import streamlit as st
import streamlit.components.v1 as components

# =========================================================================
# GITHUB CONFIGURATION
# =========================================================================
GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

# Construct raw URLs
LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{'Januma Dinavidu _ Birthday Song in Kannada _ Anuradha Bhat _ Pramod Aravind _ Vijay Krishna __.mp3'.replace(' ', '%20')}"

st.set_page_config(page_title="Happy Birthday, Gorgeous! 💖", page_icon="🌸", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for Fullscreen
st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
    .main .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; height: 100vh !important; overflow: hidden !important; }
    iframe { position: fixed !important; top: 0 !important; left: 0 !important; width: 100vw !important; height: 100vh !important; border: none !important; margin: 0 !important; padding: 0 !important; z-index: 999999 !important; }
    </style>
""", unsafe_allow_html=True)

interactive_birthday_experience = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {{ margin:0; font-family: 'Quicksand', sans-serif; background: #0d0407; color: white; overflow: hidden; }}
        .screen {{ position: absolute; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; }}
        .login-card {{ background: rgba(13,4,7,0.65); padding: 40px; border-radius: 24px; text-align: center; border: 2px solid #ff85a2; }}
        input {{ width: 250px; padding: 10px; border-radius: 20px; border: none; margin-bottom: 10px; }}
        button {{ padding: 10px 20px; border-radius: 20px; border: none; background: #ff758c; color: white; cursor: pointer; }}
        .hidden {{ display: none; }}
    </style>
</head>
<body>
    <audio id="birthday-audio" loop><source src="{SONG_URL}" type="audio/mpeg"></audio>

    <div class="screen" id="loginScreen">
        <div class="login-card">
            <h2>Enter Password</h2>
            <input type="password" id="passwordField" placeholder="Password">
            <br><button onclick="checkPassword()">Unlock Birthday surprise ▶️</button>
            <p id="errorMsg" style="color:red; display:none;">Wrong Password!</p>
        </div>
    </div>

    <div class="screen hidden" id="stageScreen"><h1>SURPRISE!</h1></div>

    <script>
        const audio = document.getElementById('birthday-audio');
        
        function startAudio() {{
            audio.play().catch(e => console.log("User interaction required for audio."));
        }}

        function checkPassword() {{
            startAudio(); // Force start on interaction
            if(document.getElementById("passwordField").value === "taperecord") {{
                document.getElementById("loginScreen").classList.add("hidden");
                document.getElementById("stageScreen").classList.remove("hidden");
            }} else {{
                document.getElementById("errorMsg").style.display = "block";
            }}
        }}

        // Catch clicks anywhere to start music
        document.addEventListener('click', startAudio, {{once: true}});
    </script>
</body>
</html>
"""

components.html(interactive_birthday_experience, height=1000)
