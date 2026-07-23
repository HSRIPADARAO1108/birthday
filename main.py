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

# --- Birthday Anthem / Audio Track Mapping ---
SONG_FILENAME = "januma-dinavidu-birthday-song-in-kannada-anuradha-bhat-pramod-aravind-vi_lk1Ob9t4.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

# --- Page Setup configuration ---
st.set_page_config(
    page_title="Happy Birthday, Pavaman! 🏏🎉",
    page_icon="🏏",
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
    <title>Pavaman's Birthday Special</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;600;800&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body, html {
            width: 100%; height: 100%; overflow: hidden;
            font-family: 'Montserrat', sans-serif;
            background-color: #0a0505; color: #fff;
            -webkit-tap-highlight-color: transparent;
        }

        .watermark {
            position: fixed; bottom: 12px; left: 50%; transform: translateX(-50%);
            z-index: 99999; font-size: 11px; font-weight: bold;
            color: rgba(255, 199, 44, 0.6); letter-spacing: 1.5px;
            text-shadow: 0 0 10px rgba(255,199,44,0.4); pointer-events: none;
            white-space: nowrap;
        }

        /* ===== STADIUM AMBIENCE LAYER (floodlights + ground strip + scoreboard) ===== */
        .floodlights { position: fixed; inset: 0; z-index: 1; pointer-events: none; }
        .floodlights span {
            position: absolute; width: 340px; height: 340px; border-radius: 50%;
            background: radial-gradient(circle, rgba(255,236,180,0.16) 0%, rgba(255,236,180,0.05) 40%, transparent 70%);
        }
        .floodlights .fl-1 { top: -140px; left: -80px; }
        .floodlights .fl-2 { top: -140px; right: -80px; }
        .floodlights .fl-3 { top: -170px; left: 45%; width: 420px; height: 420px; }

        .ground-strip {
            position: fixed; left: 0; right: 0; bottom: 0; height: 26px; z-index: 2; pointer-events: none;
            background: repeating-linear-gradient(90deg, #163a1c 0px, #163a1c 22px, #1d4a24 22px, #1d4a24 44px);
            border-top: 2px dashed rgba(255,255,255,0.55);
            box-shadow: 0 -6px 18px rgba(0,0,0,0.5);
        }

        .scoreboard-badge {
            position: fixed; top: 12px; left: 12px; z-index: 10000;
            background: #050505; border: 1px solid rgba(255,199,44,0.4); border-radius: 8px;
            padding: 6px 12px; box-shadow: 0 0 14px rgba(0,0,0,0.6);
            font-family: 'Share Tech Mono', monospace; font-size: 11px; letter-spacing: 1px;
            color: #7CFF6B; text-shadow: 0 0 8px rgba(124,255,107,0.7);
        }
        .scoreboard-badge .sb-label { color: #FFC72C; text-shadow: 0 0 8px rgba(255,199,44,0.6); }

        /* All primary screens sit above the ambience layer */
        .screen-login, .screen-stage, .screen-game, .screen-showcase { position: relative; z-index: 3; }

        /* SCREEN 1: STADIUM FLOODLIGHT LOGIN AREA */
        .screen-login {
            position: absolute; width: 100%; height: 100%;
            background: linear-gradient(135deg, rgba(10,5,5,0.7), rgba(28,8,8,0.88)), url("__LOGIN_BG_URL__") no-repeat center center;
            background-size: cover; display: flex; align-items: center; justify-content: center;
            z-index: 10; transition: all 1.2s cubic-bezier(0.4, 0, 0.2, 1); padding: 16px;
        }
        .neon-login-box {
            background: rgba(10, 5, 5, 0.5);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 199, 44, 0.2);
            padding: 40px 24px; border-radius: 24px; text-align: center;
            max-width: 400px; width: 100%;
            box-shadow: 0 0 40px rgba(236, 28, 36, 0.25), inset 0 0 20px rgba(255,255,255,0.05);
            animation: pulseGlow 4s infinite alternate;
        }
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 30px rgba(236, 28, 36, 0.2); }
            100% { box-shadow: 0 0 50px rgba(236, 28, 36, 0.4); border-color: rgba(255, 199, 44, 0.4); }
        }
        .neon-login-box h2 {
            font-family: 'Bebas Neue', sans-serif; font-size: 48px; letter-spacing: 2px; color: #EC1C24;
            margin-bottom: 12px; text-shadow: 0 0 15px rgba(236,28,36,0.6);
        }
        .neon-login-box p { font-size: 13px; color: #e5ddd0; margin-bottom: 25px; font-family: 'Montserrat', sans-serif; line-height: 1.4; }
        
        .input-wrapper { position: relative; margin-bottom: 20px; }
        .input-wrapper input {
            width: 100%; padding: 14px 20px 14px 45px;
            background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.2);
            border-radius: 50px; color: #fff; font-size: 16px; outline: none;
            transition: all 0.3s; font-family: 'Montserrat', sans-serif;
        }
        .input-wrapper input:focus { border-color: #FFC72C; background: rgba(255,255,255,0.12); box-shadow: 0 0 15px rgba(255,199,44,0.4); }
        .input-wrapper i { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); color: #FFC72C; font-size: 16px; }
        
        .neon-btn {
            width: 100%; padding: 14px; background: linear-gradient(45deg, #EC1C24, #FF4C4C);
            border: none; border-radius: 50px; color: white; font-size: 15px; font-weight: 800;
            cursor: pointer; letter-spacing: 1px; box-shadow: 0 4px 20px rgba(236,28,36,0.4);
            transition: all 0.3s; font-family: 'Montserrat', sans-serif;
        }
        .neon-btn:active { transform: scale(0.98); filter: brightness(1.1); }
        .error-hint { color: #FF4C4C; font-size: 13px; margin-top: 12px; display: none; font-weight: bold; }

        /* SCREEN 2: STADIUM TUNNEL SLIDE CURTAINS */
        .screen-stage { position: absolute; width: 100%; height: 100%; display: none; z-index: 5; }
        .theater-bg {
            position: absolute; width: 100%; height: 100%;
            background: radial-gradient(circle at center, #1c0808 0%, #0a0505 100%);
            display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 16px;
        }
        
        .glass-photo-frame {
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,199,44,0.15);
            backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
            padding: 20px; border-radius: 20px; max-width: 400px; width: 100%; text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6); opacity: 0; transform: translateY(30px);
            transition: all 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        .glass-photo-frame.reveal { opacity: 1; transform: translateY(0); }
        
        .frame-img { 
            width: 100%; height: 280px; object-fit: contain; object-position: center center;
            background: rgba(255,255,255,0.02);
            border-radius: 14px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.15); 
        }
        
        .glass-photo-frame h3 { font-family: 'Bebas Neue', sans-serif; font-size: 32px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 8px; }
        .glass-photo-frame p { font-family: 'Montserrat', sans-serif; font-size: 13px; color: #e5ddd0; margin-bottom: 20px; line-height: 1.5; }

        .curtain-panel { position: absolute; top:0; width:50%; height:100%; background:#130606; z-index:10; transition: transform 2.5s cubic-bezier(0.77, 0, 0.175, 1); display:flex; align-items:center; }
        .curtain-left { left:0; border-right: 2px solid #EC1C24; background: linear-gradient(to right, #0a0303, #260808); }
        .curtain-right { right:0; border-left: 2px solid #EC1C24; background: linear-gradient(to left, #0a0303, #260808); }
        .curtain-trigger {
            position: absolute; top:50%; left:50%; transform: translate(-50%, -50%); z-index: 15;
            background: rgba(10, 5, 5, 0.9); border: 2px solid #EC1C24; padding: 16px 24px; border-radius: 16px;
            text-align:center; cursor:pointer; box-shadow: 0 0 30px rgba(236,28,36,0.4); transition: all 0.4s;
            width: 85%; max-width: 340px;
        }
        .curtain-trigger h4 { font-family: 'Bebas Neue', sans-serif; font-size: 20px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 4px; }
        .curtain-trigger p { font-size: 11px; color: #bbb; font-family: 'Montserrat', sans-serif; }
        .curtains-parted .curtain-left { transform: translateX(-100%); }
        .curtains-parted .curtain-right { transform: translateX(100%); }
        .curtains-parted .curtain-trigger { opacity: 0; pointer-events: none; transform: translate(-50%, -50%) scale(0.7); }

        /* SCREEN 3: NET PRACTICE — HIT THE SIX MINI GAME */
        .screen-game {
            position: absolute; width:100%; height:100%; display:none;
            background: radial-gradient(ellipse at center, #123018 0%, #0a0505 75%);
            align-items:center; justify-content:center; padding:16px 16px 40px;
        }
        .game-box { max-width: 420px; width: 100%; text-align: center; }
        .game-box h2 { font-family: 'Bebas Neue', sans-serif; font-size: 40px; letter-spacing: 1px; color: #EC1C24; margin-bottom: 4px; }
        .game-box .game-sub { font-size: 12.5px; color: #cfcfcf; margin-bottom: 16px; font-family: 'Montserrat', sans-serif; }

        .pitch-wrap {
            position: relative; width: 100%; height: 200px; margin: 0 auto 18px;
            background: linear-gradient(180deg, #2f7a35 0%, #245e29 100%);
            border-radius: 14px; overflow: hidden;
            border: 1px solid rgba(255,199,44,0.25);
            box-shadow: inset 0 0 40px rgba(0,0,0,0.35), 0 10px 24px rgba(0,0,0,0.4);
        }
        .pitch-lane {
            position: absolute; left: 50%; top: 0; bottom: 0; width: 34%; transform: translateX(-50%);
            background: repeating-linear-gradient(180deg, rgba(212,177,106,0.9) 0px, rgba(212,177,106,0.9) 3px, rgba(196,158,88,0.9) 3px, rgba(196,158,88,0.9) 26px);
        }
        .crease-line { position: absolute; left: 50%; width: 46%; height: 2px; background: rgba(255,255,255,0.85); transform: translateX(-50%); }
        .crease-top { top: 14px; }
        .crease-bottom { bottom: 14px; }
        .stump-set { position: absolute; left: 50%; transform: translateX(-50%); display: flex; gap: 3px; }
        .stump-set span { width: 3px; height: 20px; background: #f3e4c0; border-radius: 1px; box-shadow: 0 0 4px rgba(0,0,0,0.5); }
        .stump-top { top: 4px; }
        .stump-bottom { bottom: 4px; }
        .bowler-emoji, .batter-emoji { position: absolute; left: 50%; transform: translateX(-50%); font-size: 26px; filter: drop-shadow(0 2px 3px rgba(0,0,0,0.6)); }
        .bowler-emoji { top: 10px; }
        .batter-emoji { bottom: 6px; }
        #gameBall {
            position: absolute; left: 50%; top: 40px; width: 12px; height: 12px; border-radius: 50%;
            background: radial-gradient(circle at 35% 35%, #ff6b5b, #b3121f); transform: translateX(-50%);
            box-shadow: 0 0 8px rgba(255,80,60,0.7); transition: top 0.05s linear;
        }
        #gameBall.smashed { animation: ballFly 0.6s ease-out forwards; }
        @keyframes ballFly {
            0% { transform: translateX(-50%) scale(1); opacity: 1; }
            100% { transform: translateX(140%) translateY(-90px) scale(0.4); opacity: 0; }
        }

        .power-meter { margin: 0 auto 16px; max-width: 340px; }
        .meter-label { font-size: 11px; color: #FFC72C; font-family: 'Montserrat', sans-serif; margin-bottom: 6px; letter-spacing: 0.5px; }
        .meter-track {
            position: relative; height: 16px; border-radius: 10px; background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15); overflow: hidden;
        }
        .meter-zone { position: absolute; top: 0; bottom: 0; background: rgba(124,255,107,0.55); border-left: 1px solid #7CFF6B; border-right: 1px solid #7CFF6B; }
        .meter-indicator {
            position: absolute; top: -3px; width: 4px; height: 22px; background: #fff;
            box-shadow: 0 0 8px rgba(255,255,255,0.9); border-radius: 2px;
        }

        .swing-btn { max-width: 260px; margin: 0 auto 14px; display: block; font-size: 16px; }
        .game-status {
            font-family: 'Share Tech Mono', monospace; font-size: 13px; color: #7CFF6B;
            letter-spacing: 1px; margin-bottom: 10px; min-height: 18px;
        }
        .game-result { font-family: 'Bebas Neue', sans-serif; font-size: 26px; letter-spacing: 1px; min-height: 32px; margin-bottom: 6px; }
        .game-result.six { color: #FFC72C; text-shadow: 0 0 12px rgba(255,199,44,0.7); }
        .game-result.miss { color: #FF4C4C; }

        /* SCREEN 4: PREMIUM INTERACTIVE ALBUM SHOWCASE */
        .screen-showcase {
            position: absolute; width:100%; height:100%; display:none; z-index: 100;
            background: linear-gradient(150deg, #140505 0%, #220a0a 50%, #0a0202 100%);
            align-items: flex-start; justify-content: center; padding: 20px 16px; overflow-y: auto; -webkit-overflow-scrolling: touch;
        }
        .album-layout {
            max-width: 800px; width: 100%; display: flex; flex-direction: column; gap: 24px; align-items: center; margin: 0 auto 40px auto;
        }

        /* ALBUM HEADER CORE CARD */
        .hero-profile-card {
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,199,44,0.15);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-radius: 20px; padding: 30px 20px; text-align: center; width: 100%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4); display: flex; flex-direction: column; align-items: center;
        }
        .circle-avatar {
            width: 140px; height: 140px; border-radius: 50%; padding: 4px;
            background: linear-gradient(45deg, #EC1C24, #FFC72C); margin-bottom: 16px;
            box-shadow: 0 10px 25px rgba(236,28,36,0.4);
            display: flex; align-items: center; justify-content: center; overflow: hidden;
        }
        .circle-avatar img { 
            width: 100%; height: 100%; object-fit: cover; object-position: center 20%;
            border-radius: 50%; border: 3px solid #0a0505; 
        }
        .hero-profile-card h1 { font-family: 'Bebas Neue', sans-serif; font-size: 46px; letter-spacing: 2px; color: #EC1C24; margin-bottom: 5px; }
        .hero-profile-card .subtitle { font-size: 18px; color: #FFC72C; margin-bottom: 12px; font-weight: 800; letter-spacing: 0.5px; }
        .hero-profile-card p.wishes { font-family: 'Montserrat', sans-serif; font-size: 13px; line-height: 1.7; color: #e5ddd0; max-width: 600px; }

        /* THE CHIC 3D FLIP PHOTO GALLERY */
        .gallery-grid {
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%;
        }
        .flip-card { background-color: transparent; height: 260px; perspective: 1000px; cursor: pointer; }
        .flip-card-inner {
            position: relative; width: 100%; height: 100%; text-align: center;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); transform-style: preserve-3d;
        }
        .flip-card.flipped .flip-card-inner { transform: rotateY(180deg); }
        
        .flip-front, .flip-back {
            position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden;
            border-radius: 16px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);
        }
        
        .flip-front {
            background: rgba(255, 255, 255, 0.02);
            display: flex; align-items: center; justify-content: center;
        }
        .flip-front img { 
            width: 100%; height: 100%; object-fit: contain; object-position: center center; 
        }
        
        .flip-back {
            background: linear-gradient(135deg, #300b0b 0%, #140303 100%);
            color: white; display: flex; flex-direction: column; align-items: center; justify-content: center;
            transform: rotateY(180deg); padding: 16px; border: 1px solid rgba(236, 28, 36, 0.3);
        }
        .flip-back h4 { font-family: 'Bebas Neue', sans-serif; font-size: 20px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 6px; }
        .flip-back p { font-family: 'Montserrat', sans-serif; font-size: 11px; color: #e5ddd0; line-height: 1.4; }
        
        .hint-touch { 
            position: absolute; bottom: 12px; right: 12px; 
            background: rgba(236, 28, 36, 0.85); padding: 4px 10px; 
            border-radius: 20px; font-size: 10px; font-weight: bold; color: #fff;
            box-shadow: 0 0 10px rgba(236,28,36,0.5);
            animation: pulseBadge 1.5s infinite alternate; z-index: 5;
        }
        @keyframes pulseBadge {
            0% { transform: scale(1); opacity: 0.9; }
            100% { transform: scale(1.06); opacity: 1; box-shadow: 0 0 15px rgba(236,28,36,0.8); }
        }

        /* FLOATING MUSIC STATUS CAPSULE */
        .music-bar {
            position: fixed; top: 12px; right: 12px; z-index: 10000;
            background: rgba(10,5,5,0.85); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,199,44,0.3); padding: 8px 14px; border-radius: 50px;
            display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }
        .music-bar span { font-size: 10px; font-weight: bold; color: #e5ddd0; }
        .wave-container { display: flex; align-items: flex-end; gap: 2px; height: 11px; width: 16px; }
        .wave-active .wave-bar { animation: jumpWave 1.2s ease-in-out infinite alternate; }
        .wave-bar { width: 3px; height: 100%; background-color: #EC1C24; border-radius: 2px; transform-origin: bottom; }
        .wave-bar:nth-child(2) { animation-delay: 0.3s; }
        .wave-bar:nth-child(3) { animation-delay: 0.6s; }
        @keyframes jumpWave { 0% { transform: scaleY(0.2); } 100% { transform: scaleY(1); } }

        /* CELEBRATION FALLING ANIMATION */
        .petal { position: absolute; pointer-events: none; z-index: 99; opacity: 0.8; animation: dropPetal 7s linear infinite; }
        @keyframes dropPetal {
            0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; }
            10% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { transform: translateY(105vh) translateX(30px) rotate(360deg); opacity: 0; }
        }

        /* RESPONSIVE RETINA SCALING */
        @media(max-width: 600px) {
            .gallery-grid { grid-template-columns: 1fr; }
            .flip-card { height: 280px; }
            .hero-profile-card { padding: 25px 16px; }
            .hero-profile-card h1 { font-size: 38px; }
            .neon-login-box { padding: 35px 20px; }
            .neon-login-box h2 { font-size: 40px; }
            .watermark { font-size: 9px; bottom: 8px; }
            .frame-img { height: 230px; }
            .pitch-wrap { height: 170px; }
            .scoreboard-badge { font-size: 9px; padding: 5px 9px; }
        }
    </style>
</head>
<body>

    <div class="floodlights"><span class="fl-1"></span><span class="fl-2"></span><span class="fl-3"></span></div>
    <div class="ground-strip"></div>
    <div class="scoreboard-badge"><span class="sb-label">RCB</span> DUGOUT · LIVE</div>

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
            <h2>WELCOME PAVAMAN 🏏</h2>
            <p>Unlock your premium custom-curated cricket stadium birthday experience.</p>
            <div class="input-wrapper">
                <i class="fa-solid fa-key"></i>
                <input type="password" id="passCode" placeholder="Enter Magic Password (pavaman)" autocomplete="off">
            </div>
            <button class="neon-btn" onclick="validateKey()">Enter the Stadium ⚡</button>
            <p class="error-hint" id="errHint">❌ Not out yet! Give it another shot, Pavaman.</p>
        </div>
    </div>

    <div class="screen-stage" id="stageView">
        <div class="theater-bg">
            <div class="glass-photo-frame" id="glassFrame">
                <h3>BEFORE THE TOSS</h3>
                <img src="__BEHIND_CURTAIN_URL__" class="frame-img" alt="Stage Reveal">
                <p>Life is an incredible innings, and having you around makes every match more exciting. Cheers to another year of big hits, bold shots, and total victory! 🏏</p>
                <button class="neon-btn" style="background: linear-gradient(45deg, #FFC72C, #FF9E1B); color:#1a0505;" onclick="moveNextToGame()">Head to the Nets 🏏</button>
            </div>
        </div>
        <div id="curtainShell">
            <div class="curtain-panel curtain-left"></div>
            <div class="curtain-panel curtain-right"></div>
            <div class="curtain-trigger" onclick="partCurtains()">
                <h4>🏟️ Tap to Enter the Stadium 🏟️</h4>
                <p>Step inside your personal RCB dugout</p>
            </div>
        </div>
    </div>

    <div class="screen-game" id="gameView">
        <div class="game-box">
            <h2>NET PRACTICE</h2>
            <p class="game-sub">Time your swing as the ball reaches the crease. Land the white marker in the green zone to smash a SIX. Get 3 sixes to unlock the trophy album!</p>

            <div class="pitch-wrap">
                <div class="pitch-lane"></div>
                <div class="crease-line crease-top"></div>
                <div class="crease-line crease-bottom"></div>
                <div class="stump-set stump-top"><span></span><span></span><span></span></div>
                <div class="stump-set stump-bottom"><span></span><span></span><span></span></div>
                <div class="bowler-emoji">🤾</div>
                <div class="batter-emoji">🏏</div>
                <div id="gameBall"></div>
            </div>

            <div class="power-meter">
                <div class="meter-label">TIMING METER</div>
                <div class="meter-track">
                    <div class="meter-zone" id="meterZone"></div>
                    <div class="meter-indicator" id="meterIndicator"></div>
                </div>
            </div>

            <div class="game-result" id="gameResult">&nbsp;</div>
            <button class="neon-btn swing-btn" id="swingBtn" onclick="swingBat()">🏏 SWING!</button>
            <div class="game-status" id="gameStatus">SIXES: 0 / 3</div>
            <button class="neon-btn" style="background: transparent; border: 1.5px solid #EC1C24; max-width:260px; margin: 4px auto 0;" onclick="bypassGame()">Retire Not Out (Skip) ✨</button>
        </div>
    </div>

    <div class="screen-showcase" id="showcaseView">
        <div class="album-layout">
            
            <div class="hero-profile-card">
                <div class="circle-avatar">
                    <img src="__FINAL_PROFILE_URL__" alt="Pavaman Profile">
                </div>
                <h1>HAPPY BIRTHDAY,</h1>
                <div class="subtitle">Champion Pavaman! 🏆🏏</div>
                <p class="wishes">
                    May every ball you face turn into a boundary and every challenge feel like a home game.
                    You carry the confidence of an opener and the calm of a finisher — a true match-winner in every way.
                    Have a completely blockbuster, high-scoring, and unforgettable year ahead, Pavaman! ❤️
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
                            <h4>First Boundary 🏏</h4>
                            <p>Every great innings begins with a solid start. May this new age bring you fours, sixes, and unstoppable momentum!</p>
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
                            <h4>Century Moments 💯</h4>
                            <p>Keep chasing every target with that same fearless energy. It's the kind of spirit that wins matches and hearts!</p>
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
                            <h4>Perfect Yorker 🎯</h4>
                            <p>Life is like a tricky over, but every delivery lands right when you play it with focus, grit, and a big smile.</p>
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
                            <h4>Victory Lap 🏆</h4>
                            <p>Here's to a season full of trophies, loud cheers, great friends, and unforgettable memories. Play on, Pavaman!</p>
                        </div>
                    </div>
                </div>

            </div>

            <button class="neon-btn" style="max-width: 250px; margin-top:10px; background: linear-gradient(45deg, #FFC72C, #FF9E1B); color:#1a0505;" onclick="location.reload()">Replay the Innings 🔄</button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        let tracksRunning = false;

        document.addEventListener('DOMContentLoaded', () => {
            const codeField = document.getElementById('passCode');
            if(codeField) {
                codeField.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        validateKey();
                    }
                });
            }
        });

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
            if(code === 'pavaman' || code === 'rcb' || code === 'champion') {
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

        document.getElementById('passCode').addEventListener('input', () => {
            document.getElementById('errHint').style.display = 'none';
        });

        function partCurtains() {
            document.getElementById('stageView').classList.add('curtains-parted');
            setTimeout(() => {
                document.getElementById('glassFrame').classList.add('reveal');
                generateBlossoms();
            }, 1200);
        }

        function moveNextToGame() {
            document.getElementById('stageView').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('stageView').style.display = 'none';
                document.getElementById('gameView').style.display = 'flex';
                startNetPractice();
            }, 800);
        }

        /* ===================== NET PRACTICE MINI GAME ===================== */
        const SIXES_NEEDED = 3;
        const PITCH_HEIGHT = 200;      // must roughly match .pitch-wrap height
        const BALL_TOP_MIN = 32;
        const BALL_TOP_MAX = 168;
        let sixesScored = 0;
        let ballAnimId = null;
        let ballDir = 1;
        let ballPos = 0; // 0..1
        let meterAnimId = null;
        let meterDir = 1;
        let meterPos = 0; // 0..1
        let zoneStart = 0.4;
        let zoneWidth = 0.2;
        let gameActive = false;

        function startNetPractice() {
            sixesScored = 0;
            updateGameStatus();
            document.getElementById('gameResult').innerText = '\\u00A0';
            document.getElementById('gameResult').className = 'game-result';
            newRound();
        }

        function newRound() {
            gameActive = true;
            // randomize the green "sweet spot" zone a little each round for variety
            zoneWidth = 0.22 - (sixesScored * 0.02); // gets slightly tighter each six
            if (zoneWidth < 0.14) zoneWidth = 0.14;
            zoneStart = 0.15 + Math.random() * (0.85 - zoneWidth - 0.15);
            const zoneEl = document.getElementById('meterZone');
            zoneEl.style.left = (zoneStart * 100) + '%';
            zoneEl.style.width = (zoneWidth * 100) + '%';

            ballPos = 0; ballDir = 1;
            meterPos = 0; meterDir = 1;
            document.getElementById('gameBall').classList.remove('smashed');
            animateBall();
            animateMeter();
        }

        function animateBall() {
            if (ballAnimId) cancelAnimationFrame(ballAnimId);
            function step() {
                if (!gameActive) return;
                ballPos += 0.012 * ballDir;
                if (ballPos >= 1) { ballPos = 1; ballDir = -1; }
                if (ballPos <= 0) { ballPos = 0; ballDir = 1; }
                const top = BALL_TOP_MIN + ballPos * (BALL_TOP_MAX - BALL_TOP_MIN);
                document.getElementById('gameBall').style.top = top + 'px';
                ballAnimId = requestAnimationFrame(step);
            }
            step();
        }

        function animateMeter() {
            if (meterAnimId) cancelAnimationFrame(meterAnimId);
            function step() {
                if (!gameActive) return;
                meterPos += 0.014 * meterDir;
                if (meterPos >= 1) { meterPos = 1; meterDir = -1; }
                if (meterPos <= 0) { meterPos = 0; meterDir = 1; }
                document.getElementById('meterIndicator').style.left = (meterPos * 100) + '%';
                meterAnimId = requestAnimationFrame(step);
            }
            step();
        }

        function swingBat() {
            if (!gameActive) return;
            const resultEl = document.getElementById('gameResult');
            const hit = meterPos >= zoneStart && meterPos <= (zoneStart + zoneWidth);

            gameActive = false;
            if (ballAnimId) cancelAnimationFrame(ballAnimId);
            if (meterAnimId) cancelAnimationFrame(meterAnimId);

            if (hit) {
                sixesScored++;
                document.getElementById('gameBall').classList.add('smashed');
                resultEl.innerText = 'SIX! 🏆';
                resultEl.className = 'game-result six';
                if (typeof confetti === 'function') {
                    confetti({ particleCount: 60, spread: 55, origin: { y: 0.55 }, colors: ['#EC1C24', '#FFC72C', '#ffffff'] });
                }
                updateGameStatus();
                if (sixesScored >= SIXES_NEEDED) {
                    setTimeout(finishGame, 900);
                    return;
                }
            } else {
                resultEl.innerText = 'Missed! Try again';
                resultEl.className = 'game-result miss';
            }
            setTimeout(newRound, 800);
        }

        function updateGameStatus() {
            document.getElementById('gameStatus').innerText = 'SIXES: ' + sixesScored + ' / ' + SIXES_NEEDED;
        }

        function bypassGame() {
            gameActive = false;
            if (ballAnimId) cancelAnimationFrame(ballAnimId);
            if (meterAnimId) cancelAnimationFrame(meterAnimId);
            finishGame();
        }

        function finishGame() {
            document.getElementById('gameView').style.display = 'none';
            document.getElementById('showcaseView').style.display = 'flex';
            confetti({ particleCount: 150, spread: 80, origin: { y: 0.4 }, colors: ['#EC1C24', '#FFC72C', '#ffffff'] });
            triggerCascadeReveal();
        }

        function triggerCascadeReveal() {
            const cards = document.querySelectorAll('.flip-card');
            cards.forEach((card, index) => {
                setTimeout(() => {
                    card.classList.add('flipped');
                    setTimeout(() => {
                        card.classList.remove('flipped');
                    }, 1500);
                }, 600 + (index * 400));
            });
        }

        function toggleFlip(cardElement) {
            cardElement.classList.toggle('flipped');
        }

        function generateBlossoms() {
            const shapes = ["🏏","🏆","⚡","🎉","⭐"];
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
