import streamlit as st
import streamlit.components.v1 as components

# --- GitHub Repository Configuration ---
GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

# --- Asset Variable Setup (5 Photo Links Mapping) ---
LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"
BONUS_MEMORY_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BONUS_MEMORY_IMAGE.jpeg" 

# --- Kannada Audio Track Mapping ---
SONG_FILENAME = "januma-dinavidu-birthday-song-in-kannada-anuradha-bhat-pramod-aravind-vi_lk1Ob9t4.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

# --- Page Setup configuration ---
st.set_page_config(
    page_title="Happy Birthday, Shirlu! 💖✨",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Deep inject core Streamlit UI frame removals and enforce complete full-screen behavior
st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    footer { visibility: hidden; }
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
    }
    iframe {
        position: fixed !important;
        top: 0 !important; left: 0 !important;
        width: 100vw !important; 
        height: 100vh !important;
        border: none !important; margin: 0 !important;
        padding: 0 !important; z-index: 999999 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Premium Cinematic Layout Engine Core Code ---
html_layout = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Sreelakshmi's Birthday Special</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@500;700&family=Great+Vibes&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body, html {
            width: 100%; height: 100%; overflow: hidden;
            font-family: 'Comfortaa', cursive;
            background-color: #06020b; color: #fff;
            -webkit-tap-highlight-color: transparent;
        }

        .watermark {
            position: fixed; bottom: 12px; left: 50%; transform: translateX(-50%);
            z-index: 99999; font-size: 11px; font-weight: bold;
            color: rgba(255, 107, 157, 0.6); letter-spacing: 1.5px;
            text-shadow: 0 0 10px rgba(255,107,157,0.4); pointer-events: none;
            white-space: nowrap;
        }

        /* SCREEN 1: GLOWING LOGIN AREA */
        .screen-login {
            position: absolute; width: 100%; height: 100%;
            background: linear-gradient(135deg, rgba(6,2,11,0.65), rgba(20,5,25,0.85)), url("__LOGIN_BG_URL__") no-repeat center top;
            background-size: cover; display: flex; align-items: center; justify-content: center;
            z-index: 10; transition: all 1.2s cubic-bezier(0.4, 0, 0.2, 1); padding: 16px;
        }
        .neon-login-box {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 40px 24px; border-radius: 30px; text-align: center;
            max-width: 400px; width: 100%;
            box-shadow: 0 0 40px rgba(255, 107, 157, 0.2), inset 0 0 20px rgba(255,255,255,0.05);
            animation: pulseGlow 4s infinite alternate;
        }
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 30px rgba(255, 107, 157, 0.15); }
            100% { box-shadow: 0 0 50px rgba(255, 107, 157, 0.35); border-color: rgba(255, 107, 157, 0.4); }
        }
        .neon-login-box h2 {
            font-family: 'Great Vibes', cursive; font-size: 42px; color: #ff6b9d;
            margin-bottom: 12px; text-shadow: 0 0 15px rgba(255,107,157,0.6);
        }
        .neon-login-box p { font-size: 13px; color: #dcd1e5; margin-bottom: 25px; font-family: 'Montserrat', sans-serif; line-height: 1.4; }
        
        .input-wrapper { position: relative; margin-bottom: 20px; }
        .input-wrapper input {
            width: 100%; padding: 14px 20px 14px 45px;
            background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.2);
            border-radius: 50px; color: #fff; font-size: 16px; outline: none;
            transition: all 0.3s; font-family: 'Montserrat', sans-serif;
        }
        .input-wrapper input:focus { border-color: #ff6b9d; background: rgba(255,255,255,0.12); box-shadow: 0 0 15px rgba(255,107,157,0.4); }
        .input-wrapper i { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); color: #ff6b9d; font-size: 16px; }
        
        .neon-btn {
            width: 100%; padding: 14px; background: linear-gradient(45deg, #ff6b9d, #ff85a2);
            border: none; border-radius: 50px; color: white; font-size: 15px; font-weight: bold;
            cursor: pointer; letter-spacing: 1px; box-shadow: 0 4px 20px rgba(255,107,157,0.4);
            transition: all 0.3s; font-family: 'Comfortaa', cursive;
        }
        .neon-btn:active { transform: scale(0.98); filter: brightness(1.1); }
        .error-hint { color: #ff4b72; font-size: 13px; margin-top: 12px; display: none; font-weight: bold; }

        /* SCREEN 2: MODERN MINIMALIST SLIDE CURTAINS */
        .screen-stage { position: absolute; width: 100%; height: 100%; display: none; z-index: 5; }
        .theater-bg {
            position: absolute; width: 100%; height: 100%;
            background: radial-gradient(circle at center, #1b0a21 0%, #06020b 100%);
            display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 16px;
        }
        
        .glass-photo-frame {
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
            padding: 20px; border-radius: 24px; max-width: 400px; width: 100%; text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6); opacity: 0; transform: translateY(30px);
            transition: all 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .glass-photo-frame.reveal { opacity: 1; transform: translateY(0); }
        
        .frame-img { 
            width: 100%; height: 280px; object-fit: cover; object-position: center top;
            border-radius: 16px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.2); 
        }
        
        .glass-photo-frame h3 { font-family: 'Great Vibes', cursive; font-size: 36px; color: #ff6b9d; margin-bottom: 8px; }
        .glass-photo-frame p { font-family: 'Montserrat', sans-serif; font-size: 13px; color: #e2d9eb; margin-bottom: 20px; line-height: 1.5; }

        .curtain-panel { position: absolute; top:0; width:50%; height:100%; background:#130206; z-index:10; transition: transform 2.5s cubic-bezier(0.77, 0, 0.175, 1); display:flex; align-items:center; }
        .curtain-left { left:0; border-right: 2px solid #ff6b9d; background: linear-gradient(to right, #0a0103, #26040c); }
        .curtain-right { right:0; border-left: 2px solid #ff6b9d; background: linear-gradient(to left, #0a0103, #26040c); }
        .curtain-trigger {
            position: absolute; top:50%; left:50%; transform: translate(-50%, -50%); z-index: 15;
            background: rgba(6, 2, 11, 0.9); border: 2px solid #ff6b9d; padding: 16px 24px; border-radius: 50px;
            text-align:center; cursor:pointer; box-shadow: 0 0 30px rgba(255,107,157,0.4); transition: all 0.4s;
            width: 85%; max-width: 340px;
        }
        .curtain-trigger h4 { font-size: 15px; color: #ff6b9d; letter-spacing: 0.5px; margin-bottom: 4px; }
        .curtain-trigger p { font-size: 11px; color: #aaa; font-family: 'Montserrat', sans-serif; }
        .curtains-parted .curtain-left { transform: translateX(-100%); }
        .curtains-parted .curtain-right { transform: translateX(100%); }
        .curtains-parted .curtain-trigger { opacity: 0; pointer-events: none; transform: translate(-50%, -50%) scale(0.7); }

        /* SCREEN 3: HIGH TECH PIXEL PUZZLE */
        .screen-puzzle { position: absolute; width:100%; height:100%; display:none; background:#06020b; align-items:center; justify-content:center; padding:16px; }
        .puzzle-box { max-width: 400px; width: 100%; text-align: center; }
        .puzzle-box h2 { font-family: 'Great Vibes', cursive; font-size: 38px; color: #ff6b9d; margin-bottom: 6px; }
        .puzzle-box p { font-size: 13px; color: #aaa; margin-bottom: 20px; font-family: 'Montserrat', sans-serif; }
        
        .grid-container {
            display: grid; grid-template-columns: repeat(3, var(--tile-dim, 85px)); grid-template-rows: repeat(3, var(--tile-dim, 85px));
            gap: 5px; justify-content: center; background: rgba(255,255,255,0.03); padding: 8px; border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.1); margin: 0 auto 20px; width: fit-content;
        }
        .tile {
            width: var(--tile-dim, 85px); height: var(--tile-dim, 85px); border-radius: 8px; cursor: pointer;
            background-image: url("__PUZZLE_IMG_URL__"); background-size: calc(var(--tile-dim, 85px) * 3) calc(var(--tile-dim, 85px) * 3);
            position: relative; transition: all 0.2s ease; border: 1px solid rgba(255,255,255,0.1);
        }
        .tile.active-pick { transform: scale(0.94); border-color: #ff6b9d; box-shadow: 0 0 15px #ff6b9d; filter: brightness(1.2); }
        .tile-hint-num { position: absolute; bottom: 4px; right: 4px; font-size: 9px; background: rgba(0,0,0,0.6); padding: 1px 4px; border-radius: 3px; font-weight: bold; color: #fff; }

        /* SCREEN 4: PREMIUM INTERACTIVE ALBUM SHOWCASE */
        .screen-showcase {
            position: absolute; width:100%; height:100%; display:none; z-index: 100;
            background: linear-gradient(150deg, #090314 0%, #150722 50%, #05010a 100%);
            align-items: flex-start; justify-content: center; padding: 20px 16px; overflow-y: auto; -webkit-overflow-scrolling: touch;
        }
        .album-layout {
            max-width: 800px; width: 100%; display: flex; flex-direction: column; gap: 24px; align-items: center; margin: 0 auto 40px auto;
        }

        /* ALBUM HEADER CORE CARD */
        .hero-profile-card {
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-radius: 24px; padding: 30px 20px; text-align: center; width: 100%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4); display: flex; flex-direction: column; align-items: center;
        }
        .circle-avatar {
            width: 130px; height: 130px; border-radius: 50%; padding: 4px;
            background: linear-gradient(45deg, #ff6b9d, #bb6bff); margin-bottom: 16px;
            box-shadow: 0 10px 25px rgba(255,107,157,0.4);
        }
        .circle-avatar img { 
            width:100%; height:100%; object-fit:cover; object-position: center top;
            border-radius:50%; border: 3px solid #06020b; 
        }
        .hero-profile-card h1 { font-family: 'Great Vibes', cursive; font-size: 38px; color: #ff6b9d; margin-bottom: 5px; }
        .hero-profile-card .subtitle { font-size: 16px; color: #bb6bff; margin-bottom: 12px; font-weight: bold; letter-spacing: 0.5px; }
        .hero-profile-card p.wishes { font-family: 'Montserrat', sans-serif; font-size: 13px; line-height: 1.7; color: #e2d9eb; max-width: 600px; }

        /* THE CHIC 3D FLIP PHOTO GALLERY */
        .gallery-grid {
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%;
        }
        .flip-card { background-color: transparent; height: 240px; perspective: 1000px; cursor: pointer; }
        .flip-card-inner {
            position: relative; width: 100%; height: 100%; text-align: center;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); transform-style: preserve-3d;
        }
        .flip-card.flipped .flip-card-inner { transform: rotateY(180deg); }
        .flip-front, .flip-back {
            position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden;
            border-radius: 16px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);
        }
        
        .flip-front img { width: 100%; height: 100%; object-fit: cover; object-position: center top; }
        
        .flip-back {
            background: linear-gradient(135deg, #200b30 0%, #0c0314 100%);
            color: white; display: flex; flex-direction: column; align-items: center; justify-content: center;
            transform: rotateY(180deg); padding: 16px; border: 1px solid rgba(255, 107, 157, 0.3);
        }
        .flip-back h4 { font-size: 15px; color: #ff6b9d; margin-bottom: 6px; }
        .flip-back p { font-family: 'Montserrat', sans-serif; font-size: 11px; color: #dcd1e5; line-height: 1.4; }
        
        /* Pulse Hint Badge styling to explicitly guide users to interact */
        .hint-touch { 
            position: absolute; bottom: 12px; right: 12px; 
            background: rgba(255, 107, 157, 0.85); padding: 4px 10px; 
            border-radius: 20px; font-size: 10px; font-weight: bold; color: #fff;
            box-shadow: 0 0 10px rgba(255,107,157,0.5);
            animation: pulseBadge 1.5s infinite alternate;
        }
        @keyframes pulseBadge {
            0% { transform: scale(1); opacity: 0.9; }
            100% { transform: scale(1.06); opacity: 1; box-shadow: 0 0 15px rgba(255,107,157,0.8); }
        }

        /* FLOATING MUSIC STATUS CAPSULE */
        .music-bar {
            position: fixed; top: 12px; right: 12px; z-index: 10000;
            background: rgba(6,2,11,0.85); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,107,157,0.3); padding: 8px 14px; border-radius: 50px;
            display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }
        .music-bar span { font-size: 10px; font-weight: bold; color: #e2d9eb; }
        .wave-container { display: flex; align-items: flex-end; gap: 2px; height: 11px; width: 16px; }
        .wave-bar { width: 3px; height: 100%; background-color: #ff6b9d; border-radius: 2px; transform-origin: bottom; }
        .wave-active .wave-bar { animation: jumpWave 1.2s ease-in-out infinite alternate; }
        .wave-bar:nth-child(2) { animation-delay: 0.3s; }
        .wave-bar:nth-child(3) { animation-delay: 0.6s; }
        @keyframes jumpWave { 0% { transform: scaleY(0.2); } 100% { transform: scaleY(1); } }

        /* CELEBRATION FALLING ANIMATION BLOSSOMS */
        .petal { position: absolute; pointer-events: none; z-index: 99; opacity: 0.7; animation: dropPetal 7s linear infinite; }
        @keyframes dropPetal {
            0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; }
            10% { opacity: 0.7; }
            90% { opacity: 0.7; }
            100% { transform: translateY(105vh) translateX(30px) rotate(360deg); opacity: 0; }
        }

        /* RESPONSIVE RETINA SCALING */
        @media(max-width: 600px) {
            .gallery-grid { grid-template-columns: 1fr; }
            .flip-card { height: 260px; }
            .hero-profile-card { padding: 25px 16px; }
            .hero-profile-card h1 { font-size: 32px; }
            .neon-login-box { padding: 35px 20px; }
            .neon-login-box h2 { font-size: 36px; }
            .watermark { font-size: 9px; bottom: 8px; }
            .frame-img { height: 230px; }
        }
    </style>
</head>
<body>

    <div class="watermark">✨ Created by Sripada Rao H ✨</div>

    <div class="music-bar" id="musicBar" onclick="forcePlayStream()">
        <div class="wave-container" id="waveBox">
            <div class="wave-bar"></div>
            <div class="wave-bar"></div>
            <div class="wave-bar"></div>
        </div>
        <span id="musicText">Tap for Audio</span>
        <audio id="bgAudio" loop autoplay>
            <source src="__SONG_URL__" type="audio/mpeg">
        </audio>
    </div>

    <div class="screen-login" id="loginView">
        <div class="neon-login-box">
            <h2>Welcome Shirlu ✨</h2>
            <p>Unlock your premium custom-curated cinematic dynamic birthday showcase room.</p>
            <div class="input-wrapper">
                <i class="fa-solid fa-key"></i>
                <input type="password" id="passCode" placeholder="Enter Magic Password (shirlu)" autocomplete="off">
            </div>
            <button class="neon-btn" onclick="validateKey()">Unlock Scrapbook ⚡</button>
            <p class="error-hint" id="errHint">❌ Incorrect entry! Give it another shot, Shirlu.</p>
        </div>
    </div>

    <div class="screen-stage" id="stageView">
        <div class="theater-bg">
            <div class="glass-photo-frame" id="glassFrame">
                <h3>Behind the Scenes</h3>
                <img src="__BEHIND_CURTAIN_URL__" class="frame-img" alt="Stage Reveal">
                <p>Life is an incredible journey, and having you around makes it infinitely more colorful. Cheers to another year of grace, beauty, and happiness! ✨</p>
                <button class="neon-btn" style="background: linear-gradient(45deg, #a26bff, #bb6bff);" onclick="moveNextToPuzzle()">Go to Special Challenge 🧩</button>
            </div>
        </div>
        <div id="curtainShell">
            <div class="curtain-panel curtain-left"></div>
            <div class="curtain-panel curtain-right"></div>
            <div class="curtain-trigger" onclick="partCurtains()">
                <h4>🎭 Tap to Pull Back Curtains 🎭</h4>
                <p>Step inside your mini theatre showcase room</p>
            </div>
        </div>
    </div>

    <div class="screen-puzzle" id="puzzleView">
        <div class="puzzle-box">
            <h2>The Special Challenge</h2>
            <p>Arrange the scrambled blocks into correct sequential structure to unleash the prize album.</p>
            <div class="grid-container" id="puzzGrid"></div>
            <button class="neon-btn" style="background: transparent; border: 1.5px solid #ff6b9d;" onclick="bypassPuzzle()">Instant Auto-Solve Layout ✨</button>
        </div>
    </div>

    <div class="screen-showcase" id="showcaseView">
        <div class="album-layout">
            
            <div class="hero-profile-card">
                <div class="circle-avatar">
                    <img src="__FINAL_PROFILE_URL__" alt="Sreelakshmi Profile">
                </div>
                <h1>Happy Birthday,</h1>
                <div class="subtitle">Beautiful Girl Sreelakshmi! 🌸</div>
                <p class="wishes">
                    May every little path you step on open up into beautifully rewarding journeys. 
                    You carry an incredibly elegant charm and positive spark that lights up environments effortlessly. 
                    Have a completely mesmerizing, beautiful, and blissful year ahead, Shirlu! ❤️
                </p>
            </div>

            <div class="gallery-grid">
                
                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front">
                            <img src="__LOGIN_BG_URL__" alt="Memory 1">
                            <div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div>
                        </div>
                        <div class="flip-back">
                            <h4>Enchanted Beginnings 🌟</h4>
                            <p>Every milestone begins with an exceptional spark. May your brand new age bring unexpected beautiful miracles and infinite joy!</p>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front">
                            <img src="__BEHIND_CURTAIN_URL__" alt="Memory 2">
                            <div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div>
                        </div>
                        <div class="flip-back">
                            <h4>Radiant Moments 💫</h4>
                            <p>Keep that breathtaking smile completely active all year round. It possesses the gorgeous ability to brighten up anyone's day!</p>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front">
                            <img src="__PUZZLE_IMG_URL__" alt="Memory 3">
                            <div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div>
                        </div>
                        <div class="flip-back">
                            <h4>The Perfect Picture 🧩</h4>
                            <p>Life is like a complex puzzle, but pieces magically fit perfectly when you live with pure joy, grace, and confidence.</p>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front">
                            <img src="__BONUS_MEMORY_URL__" alt="Memory 4">
                            <div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div>
                        </div>
                        <div class="flip-back">
                            <h4>Endless Celebrations 🎉</h4>
                            <p>Here's to a future filled with laughter, great coffee, wonderful stories, and precious memories. Have the best day ever, Shirlu!</p>
                        </div>
                    </div>
                </div>

            </div>

            <button class="neon-btn" style="max-width: 250px; margin-top:10px;" onclick="location.reload()">Reset & Replay Layout 🔄</button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        let tracksRunning = false;
        let matrixOrder = [1, 2, 0, 4, 3, 5, 7, 6, 8];
        let baseSelectedIdx = null;

        document.addEventListener('DOMContentLoaded', () => {
            const codeField = document.getElementById('passCode');
            if(codeField) {
                codeField.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        validateKey();
                    }
                });
            }
            adaptTileLayout();
        });

        function adaptTileLayout() {
            const boundary = Math.min(window.innerWidth - 48, window.innerHeight - 260, 320);
            const computedSize = Math.floor((boundary - 16) / 3);
            document.documentElement.style.setProperty('--tile-dim', computedSize + 'px');
        }
        window.addEventListener('resize', () => { adaptTileLayout(); renderMatrix(); });

        function forcePlayStream() {
            const player = document.getElementById('bgAudio');
            if(!player) return;
            player.play().then(() => {
                tracksRunning = true;
                document.getElementById('waveBox').classList.add('wave-active');
                document.getElementById('musicText').innerText = "Playing";
            }).catch(()=>{});
        }
        document.addEventListener('click', () => { if(!tracksRunning) forcePlayStream(); }, {once: true});

        function validateKey() {
            const code = document.getElementById('passCode').value.trim().toLowerCase();
            if(code === 'shirlu' || code === 'srilakshmi' || code === 'sreelakshmi') {
                document.getElementById('loginView').style.opacity = '0';
                forcePlayStream();
                setTimeout(() => {
                    document.getElementById('loginView').style.display = 'none';
                    document.getElementById('stageView').style.display = 'block';
                }, 1200);
            } else {
                document.getElementById('errHint').style.display = 'block';
            }
        }

        function partCurtains() {
            document.getElementById('stageView').classList.add('curtains-parted');
            setTimeout(() => {
                document.getElementById('glassFrame').classList.add('reveal');
                generateBlossoms();
            }, 1200);
        }

        function moveNextToPuzzle() {
            document.getElementById('stageView').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('stageView').style.display = 'none';
                document.getElementById('puzzleView').style.display = 'flex';
                adaptTileLayout();
                renderMatrix();
            }, 800);
        }

        function renderMatrix() {
            const board = document.getElementById('puzzGrid');
            if(!board) return;
            board.innerHTML = '';
            const dim = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--tile-dim')) || 85;

            matrixOrder.forEach((val, idx) => {
                const element = document.createElement('div');
                element.className = 'tile';
                const r = Math.floor(val / 3);
                const c = val % 3;
                element.style.backgroundPosition = `-${c * dim}px -${r * dim}px`;
                element.style.backgroundSize = `${dim * 3}px ${dim * 3}px`;

                const numeric = document.createElement('span');
                numeric.className = 'tile-hint-num';
                numeric.innerText = val + 1;
                element.appendChild(numeric);

                element.addEventListener('click', () => processTileTap(idx));
                board.appendChild(element);
            });
        }

        function processTileTap(idx) {
            const items = document.getElementsByClassName('tile');
            if(baseSelectedIdx === null) {
                baseSelectedIdx = idx;
                items[idx].classList.add('active-pick');
            } else {
                const primary = baseSelectedIdx;
                items[primary].classList.remove('active-pick');
                if(primary !== idx) {
                    [matrixOrder[primary], matrixOrder[idx]] = [matrixOrder[idx], matrixOrder[primary]];
                    renderMatrix();
                    evaluateResolution();
                }
                baseSelectedIdx = null;
            }
        }

        function bypassPuzzle() {
            matrixOrder = [0,1,2,3,4,5,6,7,8];
            renderMatrix();
            setTimeout(evaluateResolution, 300);
        }

        function evaluateResolution() {
            if(matrixOrder.every((v, i) => v === i)) {
                confetti({ particleCount: 150, spread: 80, origin: { y: 0.4 } });
                document.getElementById('puzzleView').style.display = 'none';
                document.getElementById('showcaseView').style.display = 'flex';
                
                triggerCascadeReveal();
            }
        }

        function triggerCascadeReveal() {
            const cards = document.querySelectorAll('.flip-card');
            cards.forEach((card, index) => {
                setTimeout(() => {
                    card.classList.add('flipped');
                }, 600 + (index * 400));
            });
        }

        function toggleFlip(cardElement) {
            cardElement.classList.toggle('flipped');
        }

        function generateBlossoms() {
            const shapes = ["🌸","✨","💖","🎈","🍁"];
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const leaf = document.createElement("div");
                    leaf.className = "petal";
                    leaf.innerText = shapes[Math.floor(Math.random() * shapes.length)];
                    leaf.style.left = Math.random() * 90 + "vw";
                    leaf.style.fontSize = Math.random() * 14 + 14 + "px";
                    leaf.style.animationDuration = Math.random() * 4 + 5 + "s";
                    document.body.appendChild(leaf);
                    setTimeout(() => leaf.remove(), 8000);
                }, i * 400);
            }
        }
    </script>
</body>
</html>"""

# Execute asset mapping logic directly safely outside the string declaration block
final_layout_rendered = html_layout.replace("__LOGIN_BG_URL__", LOGIN_BACKGROUND_IMAGE)\
                                  .replace("__BEHIND_CURTAIN_URL__", BEHIND_CURTAIN_IMAGE)\
                                  .replace("__PUZZLE_IMG_URL__", PUZZLE_IMAGE)\
                                  .replace("__FINAL_PROFILE_URL__", FINAL_PROFILE_IMAGE)\
                                  .replace("__BONUS_MEMORY_URL__", BONUS_MEMORY_IMAGE)\
                                  .replace("__SONG_URL__", SONG_URL)

# Mount the layout engine into components frame
components.html(final_layout_rendered, height=1000, scrolling=False)
