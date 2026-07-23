import streamlit as st
import streamlit.components.v1 as components

# --- GitHub Repository Configuration ---
GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

# --- Asset Variable Setup ---
LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"
BONUS_MEMORY_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BONUS_MEMORY_IMAGE.jpeg"

# Upload this yourself to the repo root (e.g. "rcb_logo.png") — the crest badge will use it
# everywhere automatically. If it isn't found, it quietly falls back to a text crest, so
# nothing ever breaks even before you upload it.
RCB_LOGO_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/rcb_logo.png"

# Optional wide team-huddle photo for the "Dugout Roll Call" screen.
DUGOUT_TEAM_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/DUGOUT_TEAM_IMAGE.jpeg"

# --- Birthday Anthem / Audio Track Mapping ---
SONG_FILENAME = "januma-dinavidu-birthday-song-in-kannada-anuradha-bhat-pramod-aravind-vi_lk1Ob9t4.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

st.set_page_config(
    page_title="Happy Birthday, Pavaman! 🏏🔥",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    footer { visibility: hidden; }
    .main .block-container {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
        height: 100vh !important; overflow: hidden !important;
    }
    iframe {
        position: fixed !important; top: 0 !important; left: 0 !important;
        width: 100vw !important; height: 100vh !important;
        border: none !important; margin: 0 !important; padding: 0 !important; z-index: 999999 !important;
    }
    </style>
""", unsafe_allow_html=True)

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
            text-shadow: 0 0 10px rgba(255,199,44,0.4); pointer-events: none; white-space: nowrap;
        }

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
            border-top: 2px dashed rgba(255,255,255,0.55); box-shadow: 0 -6px 18px rgba(0,0,0,0.5);
        }

        .scoreboard-badge {
            position: fixed; top: 12px; left: 12px; z-index: 10000;
            background: #050505; border: 1px solid rgba(255,199,44,0.4); border-radius: 8px;
            padding: 6px 12px; box-shadow: 0 0 14px rgba(0,0,0,0.6);
            font-family: 'Share Tech Mono', monospace; font-size: 11px; letter-spacing: 1px;
            color: #7CFF6B; text-shadow: 0 0 8px rgba(124,255,107,0.7);
        }
        .scoreboard-badge .sb-label { color: #FFC72C; text-shadow: 0 0 8px rgba(255,199,44,0.6); }

        .screen-login, .screen-stage, .screen-game, .screen-showcase, .screen-dugout { position: relative; z-index: 3; }

        /* --- Crest badge: uses your uploaded logo, falls back to a text crest if missing --- */
        .fan-crest {
            width: 92px; height: 92px; border-radius: 50%; margin: 0 auto 14px;
            background: radial-gradient(circle at 35% 30%, #ff5a5f 0%, #EC1C24 45%, #7a0d10 100%);
            border: 3px solid #FFC72C; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 0 25px rgba(236,28,36,0.55), inset 0 0 12px rgba(0,0,0,0.4);
            position: relative; animation: crestSpinIn 1.2s cubic-bezier(0.34,1.56,0.64,1); overflow: hidden;
        }
        .fan-crest::before {
            content: ""; position: absolute; inset: -8px; border-radius: 50%;
            border: 2px dashed rgba(255,199,44,0.5); animation: crestRing 12s linear infinite;
        }
        .fan-crest img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
        .fan-crest span { font-family: 'Bebas Neue', sans-serif; font-size: 30px; color: #FFC72C; letter-spacing: 1px; text-shadow: 0 0 8px rgba(0,0,0,0.5); }
        @keyframes crestSpinIn { 0% { transform: rotate(-200deg) scale(0.3); opacity: 0; } 100% { transform: rotate(0) scale(1); opacity: 1; } }
        @keyframes crestRing { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

        /* SCREEN 1: LOGIN */
        .screen-login {
            position: absolute; width: 100%; height: 100%;
            background: linear-gradient(135deg, rgba(10,5,5,0.7), rgba(28,8,8,0.88)), url("__LOGIN_BG_URL__") no-repeat center center;
            background-size: cover; display: flex; align-items: center; justify-content: center;
            z-index: 10; transition: all 1.2s cubic-bezier(0.4, 0, 0.2, 1); padding: 16px;
        }
        .neon-login-box {
            background: rgba(10, 5, 5, 0.5); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 199, 44, 0.2); padding: 40px 24px; border-radius: 24px; text-align: center;
            max-width: 400px; width: 100%; box-shadow: 0 0 40px rgba(236, 28, 36, 0.25), inset 0 0 20px rgba(255,255,255,0.05);
            animation: pulseGlow 4s infinite alternate;
        }
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 30px rgba(236, 28, 36, 0.2); }
            100% { box-shadow: 0 0 50px rgba(236, 28, 36, 0.4); border-color: rgba(255, 199, 44, 0.4); }
        }
        .neon-login-box h2 {
            font-family: 'Bebas Neue', sans-serif; font-size: 46px; letter-spacing: 2px; color: #EC1C24;
            margin-bottom: 12px; text-shadow: 0 0 15px rgba(236,28,36,0.6);
        }
        .neon-login-box p { font-size: 13px; color: #e5ddd0; margin-bottom: 25px; line-height: 1.4; }
        .input-wrapper { position: relative; margin-bottom: 20px; }
        .input-wrapper input {
            width: 100%; padding: 14px 20px 14px 45px; background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.2); border-radius: 50px; color: #fff; font-size: 16px;
            outline: none; transition: all 0.3s;
        }
        .input-wrapper input:focus { border-color: #FFC72C; background: rgba(255,255,255,0.12); box-shadow: 0 0 15px rgba(255,199,44,0.4); }
        .input-wrapper i { position: absolute; left: 18px; top: 50%; transform: translateY(-50%); color: #FFC72C; font-size: 16px; }
        .neon-btn {
            width: 100%; padding: 14px; background: linear-gradient(45deg, #EC1C24, #FF4C4C);
            border: none; border-radius: 50px; color: white; font-size: 15px; font-weight: 800;
            cursor: pointer; letter-spacing: 1px; box-shadow: 0 4px 20px rgba(236,28,36,0.4); transition: all 0.3s;
        }
        .neon-btn:active { transform: scale(0.98); filter: brightness(1.1); }
        .error-hint { color: #FF4C4C; font-size: 13px; margin-top: 12px; display: none; font-weight: bold; }

        .chant-marquee {
            position: absolute; top: 0; left: 0; width: 100%; z-index: 6; overflow: hidden;
            background: rgba(0,0,0,0.35); border-bottom: 1px solid rgba(255,199,44,0.3); padding: 6px 0; white-space: nowrap;
        }
        .chant-marquee span {
            display: inline-block; padding-left: 100%; animation: marqueeScroll 16s linear infinite;
            font-family: 'Share Tech Mono', monospace; font-size: 12px; letter-spacing: 2px; color: #FFC72C;
        }
        @keyframes marqueeScroll { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }

        /* SCREEN 2: CURTAIN STAGE */
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
            background: rgba(255,255,255,0.02); border-radius: 14px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.15);
        }
        .glass-photo-frame h3 { font-family: 'Bebas Neue', sans-serif; font-size: 32px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 8px; }
        .glass-photo-frame p { font-size: 13px; color: #e5ddd0; margin-bottom: 20px; line-height: 1.5; }
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
        .curtain-trigger p { font-size: 11px; color: #bbb; }
        .curtains-parted .curtain-left { transform: translateX(-100%); }
        .curtains-parted .curtain-right { transform: translateX(100%); }
        .curtains-parted .curtain-trigger { opacity: 0; pointer-events: none; transform: translate(-50%, -50%) scale(0.7); }

        /* SCREEN 3: POWER-HIT CHALLENGE — timing based batting mini-game */
        .screen-game {
            position: absolute; width:100%; height:100%; display:none;
            background: radial-gradient(ellipse at center, #123018 0%, #0a0505 78%);
            align-items:center; justify-content:center; padding:16px 16px 40px; overflow-y: auto;
        }
        .game-box { max-width: 460px; width: 100%; text-align: center; margin: auto; }
        .game-box h2 {
            font-family: 'Bebas Neue', sans-serif; font-size: 40px; letter-spacing: 1px; color: #EC1C24;
            margin-bottom: 4px; text-shadow: 0 0 14px rgba(236,28,36,0.5);
        }
        .game-box .game-sub { font-size: 12.5px; color: #cfcfcf; margin-bottom: 16px; line-height: 1.5; }

        .over-tracker { display: flex; justify-content: center; gap: 8px; margin-bottom: 16px; }
        .ball-pip {
            width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-family: 'Share Tech Mono', monospace; font-size: 11px; font-weight: bold;
            background: rgba(255,255,255,0.06); border: 1.5px solid rgba(255,255,255,0.2); color: #999;
            transition: all 0.3s;
        }
        .ball-pip.current { border-color: #FFC72C; color: #FFC72C; box-shadow: 0 0 10px rgba(255,199,44,0.6); transform: scale(1.15); }
        .ball-pip.done-6 { background: #FFC72C; color: #1a0505; border-color: #FFC72C; }
        .ball-pip.done-4 { background: #7CFF6B; color: #0a2f0a; border-color: #7CFF6B; }
        .ball-pip.done-1, .ball-pip.done-2 { background: rgba(255,255,255,0.25); color: #fff; }
        .ball-pip.done-0 { background: rgba(236,28,36,0.35); color: #fff; }

        .pitch-strip {
            position: relative; width: 100%; height: 64px; margin: 0 auto 20px; border-radius: 32px;
            background: linear-gradient(90deg, #3a2a0a 0%, #b58a3a 12%, #3a2a0a 20%, #1d4a24 20%, #2f7a35 50%, #1d4a24 80%, #3a2a0a 88%, #b58a3a 92%, #3a2a0a 100%);
            border: 2px solid rgba(255,199,44,0.3); overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
        }
        .sweet-zone {
            position: absolute; top: 0; bottom: 0; background: rgba(124,255,107,0.28);
            border-left: 2px dashed rgba(124,255,107,0.9); border-right: 2px dashed rgba(124,255,107,0.9);
        }
        .good-zone-l, .good-zone-r {
            position: absolute; top: 0; bottom: 0; width: 13%; background: rgba(255,199,44,0.18);
        }
        .swing-marker {
            position: absolute; top: -6px; bottom: -6px; width: 6px; border-radius: 3px;
            background: #fff; box-shadow: 0 0 14px rgba(255,255,255,0.9), 0 0 6px #EC1C24;
        }
        .zone-labels { display: flex; justify-content: space-between; font-size: 9px; color: #999; margin: -12px 4px 16px; font-family: 'Share Tech Mono', monospace; letter-spacing: 1px; }

        .swing-btn {
            width: 100%; padding: 18px; background: linear-gradient(45deg, #EC1C24, #FF4C4C);
            border: none; border-radius: 50px; color: white; font-size: 20px; font-weight: 800;
            cursor: pointer; letter-spacing: 2px; box-shadow: 0 6px 24px rgba(236,28,36,0.5);
            transition: all 0.15s; font-family: 'Bebas Neue', sans-serif; margin-bottom: 14px;
        }
        .swing-btn:active { transform: scale(0.95); filter: brightness(1.2); }
        .swing-btn:disabled { opacity: 0.4; cursor: not-allowed; }

        .shot-result { font-family: 'Bebas Neue', sans-serif; font-size: 34px; letter-spacing: 1px; min-height: 42px; margin-bottom: 6px; }
        .shot-result.r6 { color: #FFC72C; text-shadow: 0 0 16px rgba(255,199,44,0.8); animation: resultPop 0.5s ease; }
        .shot-result.r4 { color: #7CFF6B; text-shadow: 0 0 14px rgba(124,255,107,0.7); animation: resultPop 0.5s ease; }
        .shot-result.r1 { color: #e5ddd0; }
        .shot-result.r0 { color: #FF4C4C; }
        @keyframes resultPop { 0% { transform: scale(0.5); opacity: 0; } 60% { transform: scale(1.15); } 100% { transform: scale(1); opacity: 1; } }

        .total-runs {
            font-family: 'Share Tech Mono', monospace; font-size: 13px; color: #7CFF6B; letter-spacing: 1px; margin-bottom: 16px;
        }
        .total-runs b { color: #FFC72C; font-size: 16px; }

        .game-btn-row { display: flex; gap: 10px; max-width: 380px; margin: 6px auto 0; }
        .game-btn-row .neon-btn { font-size: 13px; padding: 12px 10px; }

        /* SCREEN 3.5: DUGOUT ROLL CALL */
        .screen-dugout {
            position: absolute; width:100%; height:100%; display:none; z-index: 40;
            background: radial-gradient(circle at top, #1c0808 0%, #0a0505 80%);
            align-items: center; justify-content: center; padding: 20px 16px; overflow-y: auto;
        }
        .dugout-box { max-width: 560px; width: 100%; text-align: center; margin: auto; }
        .dugout-box h2 { font-family: 'Bebas Neue', sans-serif; font-size: 40px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 6px; text-shadow: 0 0 14px rgba(255,199,44,0.5); }
        .dugout-box .dugout-sub { font-size: 13px; color: #e5ddd0; margin-bottom: 18px; line-height: 1.5; }
        .dugout-photo {
            width: 100%; max-height: 220px; object-fit: cover; border-radius: 16px;
            border: 1px solid rgba(255,199,44,0.3); margin-bottom: 18px; box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        }
        .jersey-row { display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-bottom: 20px; }
        .jersey {
            width: 78px; height: 92px; border-radius: 10px; background: linear-gradient(160deg, #EC1C24, #7a0d10);
            border: 1.5px solid rgba(255,199,44,0.5); display: flex; flex-direction: column;
            align-items: center; justify-content: center; box-shadow: 0 8px 18px rgba(0,0,0,0.4);
            animation: jerseyBob 3s ease-in-out infinite;
        }
        .jersey:nth-child(2n) { animation-delay: 0.4s; }
        .jersey:nth-child(3n) { animation-delay: 0.8s; }
        @keyframes jerseyBob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
        .jersey .num { font-family: 'Bebas Neue', sans-serif; font-size: 26px; color: #FFC72C; }
        .jersey .tag { font-size: 8px; letter-spacing: 1px; color: #f4e9d8; margin-top: 2px; }
        .dugout-quote {
            font-size: 13px; color: #e5ddd0; line-height: 1.6; background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,199,44,0.15); border-radius: 14px; padding: 16px; margin-bottom: 18px;
        }

        /* SCREEN 4: ALBUM SHOWCASE */
        .screen-showcase {
            position: absolute; width:100%; height:100%; display:none; z-index: 100;
            background: linear-gradient(150deg, #140505 0%, #220a0a 50%, #0a0202 100%);
            align-items: flex-start; justify-content: center; padding: 20px 16px; overflow-y: auto; -webkit-overflow-scrolling: touch;
        }
        .album-layout { max-width: 800px; width: 100%; display: flex; flex-direction: column; gap: 24px; align-items: center; margin: 0 auto 40px auto; }
        .hero-profile-card {
            background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,199,44,0.15);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-radius: 20px; padding: 30px 20px; text-align: center; width: 100%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4); display: flex; flex-direction: column; align-items: center;
        }
        .circle-avatar {
            width: 140px; height: 140px; border-radius: 50%; padding: 4px;
            background: linear-gradient(45deg, #EC1C24, #FFC72C); margin-bottom: 16px;
            box-shadow: 0 10px 25px rgba(236,28,36,0.4); display: flex; align-items: center; justify-content: center; overflow: hidden;
        }
        .circle-avatar img { width: 100%; height: 100%; object-fit: cover; object-position: center 20%; border-radius: 50%; border: 3px solid #0a0505; }
        .hero-profile-card h1 { font-family: 'Bebas Neue', sans-serif; font-size: 46px; letter-spacing: 2px; color: #EC1C24; margin-bottom: 5px; }
        .hero-profile-card .subtitle { font-size: 18px; color: #FFC72C; margin-bottom: 12px; font-weight: 800; letter-spacing: 0.5px; }
        .hero-profile-card p.wishes { font-size: 13px; line-height: 1.7; color: #e5ddd0; max-width: 600px; }
        .gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%; }
        .flip-card { background-color: transparent; height: 260px; perspective: 1000px; cursor: pointer; }
        .flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); transform-style: preserve-3d; }
        .flip-card.flipped .flip-card-inner { transform: rotateY(180deg); }
        .flip-front, .flip-back { position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 16px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); }
        .flip-front { background: rgba(255, 255, 255, 0.02); display: flex; align-items: center; justify-content: center; }
        .flip-front img { width: 100%; height: 100%; object-fit: contain; object-position: center center; }
        .flip-back { background: linear-gradient(135deg, #300b0b 0%, #140303 100%); color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; transform: rotateY(180deg); padding: 16px; border: 1px solid rgba(236, 28, 36, 0.3); }
        .flip-back h4 { font-family: 'Bebas Neue', sans-serif; font-size: 20px; letter-spacing: 1px; color: #FFC72C; margin-bottom: 6px; }
        .flip-back p { font-size: 11px; color: #e5ddd0; line-height: 1.4; }
        .hint-touch { position: absolute; bottom: 12px; right: 12px; background: rgba(236, 28, 36, 0.85); padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: bold; color: #fff; box-shadow: 0 0 10px rgba(236,28,36,0.5); animation: pulseBadge 1.5s infinite alternate; z-index: 5; }
        @keyframes pulseBadge { 0% { transform: scale(1); opacity: 0.9; } 100% { transform: scale(1.06); opacity: 1; box-shadow: 0 0 15px rgba(236,28,36,0.8); } }

        .music-bar {
            position: fixed; top: 12px; right: 12px; z-index: 10000; background: rgba(10,5,5,0.85);
            backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,199,44,0.3);
            padding: 8px 14px; border-radius: 50px; display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        }
        .music-bar span { font-size: 10px; font-weight: bold; color: #e5ddd0; }
        .wave-container { display: flex; align-items: flex-end; gap: 2px; height: 11px; width: 16px; }
        .wave-active .wave-bar { animation: jumpWave 1.2s ease-in-out infinite alternate; }
        .wave-bar { width: 3px; height: 100%; background-color: #EC1C24; border-radius: 2px; transform-origin: bottom; }
        .wave-bar:nth-child(2) { animation-delay: 0.3s; }
        .wave-bar:nth-child(3) { animation-delay: 0.6s; }
        @keyframes jumpWave { 0% { transform: scaleY(0.2); } 100% { transform: scaleY(1); } }

        .petal { position: absolute; pointer-events: none; z-index: 99; opacity: 0.8; animation: dropPetal 7s linear infinite; }
        @keyframes dropPetal { 0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; } 10% { opacity: 0.8; } 90% { opacity: 0.8; } 100% { transform: translateY(105vh) translateX(30px) rotate(360deg); opacity: 0; } }

        .firework-dot { position: absolute; width: 6px; height: 6px; border-radius: 50%; pointer-events: none; z-index: 98; animation: fireworkPop 1.1s ease-out forwards; }
        @keyframes fireworkPop { 0% { transform: translate(0,0) scale(1); opacity: 1; } 100% { transform: translate(var(--fx), var(--fy)) scale(0.2); opacity: 0; } }

        @media(max-width: 600px) {
            .gallery-grid { grid-template-columns: 1fr; }
            .flip-card { height: 280px; }
            .hero-profile-card { padding: 25px 16px; }
            .hero-profile-card h1 { font-size: 38px; }
            .neon-login-box { padding: 35px 20px; }
            .neon-login-box h2 { font-size: 38px; }
            .watermark { font-size: 9px; bottom: 8px; }
            .frame-img { height: 230px; }
            .scoreboard-badge { font-size: 9px; padding: 5px 9px; }
            .game-btn-row { flex-direction: column; }
            .jersey { width: 64px; height: 78px; }
            .dugout-box h2 { font-size: 32px; }
            .game-box h2 { font-size: 32px; }
            .swing-btn { font-size: 17px; padding: 16px; }
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
            <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
        </div>
        <span id="musicText">Tap for Audio</span>
        <audio id="bgAudio" loop autoplay>
            <source src="__SONG_URL__" type="audio/mpeg">
        </audio>
    </div>

    <div class="screen-login" id="loginView">
        <div class="chant-marquee"><span>🔴 THE DUGOUT IS ROARING FOR PAVAMAN &nbsp;•&nbsp; HAPPY BIRTHDAY CHAMP &nbsp;•&nbsp; PLAY BOLD, PLAY LOUD &nbsp;•&nbsp; 🔴 THE DUGOUT IS ROARING FOR PAVAMAN &nbsp;•&nbsp; HAPPY BIRTHDAY CHAMP &nbsp;•&nbsp;</span></div>
        <div class="neon-login-box">
            <div class="fan-crest" id="crestLogin"><img src="__RCB_LOGO_URL__" onerror="this.replaceWith(Object.assign(document.createElement('span'),{textContent:'RCB'}))" alt="RCB"></div>
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
                <button class="neon-btn" style="background: linear-gradient(45deg, #FFC72C, #FF9E1B); color:#1a0505;" onclick="moveNextToGame()">Take Strategic Guard 🏏</button>
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
            <h2>POWER-HIT CHALLENGE 🏏🔥</h2>
            <p class="game-sub">Face one over — 6 balls. Watch the white marker race across the pitch and tap <b>SWING!</b> the instant it's inside the green zone for a SIX. Timing is everything!</p>

            <div class="over-tracker" id="overTracker"></div>

            <div class="pitch-strip" id="pitchStrip">
                <div class="good-zone-l"></div>
                <div class="good-zone-r"></div>
                <div class="sweet-zone" id="sweetZone"></div>
                <div class="swing-marker" id="swingMarker"></div>
            </div>
            <div class="zone-labels"><span>DOT</span><span>4</span><span>SIX ZONE</span><span>4</span><span>DOT</span></div>

            <div class="shot-result" id="shotResult">&nbsp;</div>
            <div class="total-runs">BALL <span id="ballNum">1</span>/6 &nbsp;·&nbsp; SCORE: <b id="scoreVal">0</b></div>

            <button class="swing-btn" id="swingBtn" onclick="attemptSwing()">SWING!</button>

            <div class="game-btn-row">
                <button class="neon-btn" style="background: transparent; border: 1.5px solid #FFC72C;" onclick="restartOver()">New Over 🔄</button>
                <button class="neon-btn" style="background: transparent; border: 1.5px solid #EC1C24;" onclick="bypassGame()">Retire Not Out (Skip) ✨</button>
            </div>
        </div>
    </div>

    <div class="screen-dugout" id="dugoutView">
        <div class="dugout-box">
            <div class="fan-crest"><img src="__RCB_LOGO_URL__" onerror="this.replaceWith(Object.assign(document.createElement('span'),{textContent:'RCB'}))" alt="RCB"></div>
            <h2>THE WHOLE DUGOUT IS UP! 🙌</h2>
            <p class="dugout-sub" id="dugoutScoreLine">Every jersey in the squad, every fan in the stands — all on their feet for one reason today.</p>
            <img src="__DUGOUT_TEAM_URL__" class="dugout-photo" alt="Team Huddle" onerror="this.style.display='none'">
            <div class="jersey-row" id="jerseyRow"></div>
            <div class="dugout-quote">
                🎙️ <b>Stadium Announcer:</b> "Ladies and gentlemen, put your hands together — today the whole ground is here to wish a very special member of our extended squad, <b>Pavaman</b>, a rocking birthday! May your year ahead be full of sixes, not out innings, and trophy-lifting moments!" 🏆
            </div>
            <button class="neon-btn" style="background: linear-gradient(45deg, #FFC72C, #FF9E1B); color:#1a0505;" onclick="moveToShowcase()">Walk Out to the Crowd 🎉</button>
        </div>
    </div>

    <div class="screen-showcase" id="showcaseView">
        <div class="album-layout">
            <div class="hero-profile-card">
                <div class="fan-crest"><img src="__RCB_LOGO_URL__" onerror="this.replaceWith(Object.assign(document.createElement('span'),{textContent:'RCB'}))" alt="RCB"></div>
                <div class="circle-avatar"><img src="__FINAL_PROFILE_URL__" alt="Pavaman Profile"></div>
                <h1>HAPPY BIRTHDAY,</h1>
                <div class="subtitle">Champion Pavaman! 🏆🏏</div>
                <p class="wishes">
                    May every ball you face turn into a boundary and every challenge feel like a home game.
                    You carry the confidence of an opener, the calm of a finisher, and the mind of a grandmaster — a true match-winner in every way.
                    Have a completely blockbuster, high-scoring, and unforgettable year ahead, Pavaman! ❤️
                </p>
            </div>

            <div class="gallery-grid">
                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front"><img src="__LOGIN_BG_URL__" alt="Memory 1"><div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div></div>
                        <div class="flip-back"><h4>First Boundary 🏏</h4><p>Every great innings begins with a solid start. May this new age bring you fours, sixes, and unstoppable momentum!</p></div>
                    </div>
                </div>
                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front"><img src="__BEHIND_CURTAIN_URL__" alt="Memory 2"><div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div></div>
                        <div class="flip-back"><h4>Century Moments 💯</h4><p>Keep chasing every target with that same fearless energy. It's the kind of spirit that wins matches and hearts!</p></div>
                    </div>
                </div>
                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front"><img src="__PUZZLE_IMG_URL__" alt="Memory 3"><div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div></div>
                        <div class="flip-back"><h4>Perfect Yorker 🎯</h4><p>Life is like a tricky over, but every delivery lands right when you play it with focus, grit, and a big smile.</p></div>
                    </div>
                </div>
                <div class="flip-card" onclick="toggleFlip(this)">
                    <div class="flip-card-inner">
                        <div class="flip-front"><img src="__BONUS_MEMORY_URL__" alt="Memory 4"><div class="hint-touch"><i class="fa-solid fa-rotate"></i> Flip Me</div></div>
                        <div class="flip-back"><h4>Victory Lap 🏆</h4><p>Here's to a season full of trophies, loud cheers, great friends, and unforgettable memories. Play on, Pavaman!</p></div>
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
                    if (e.key === 'Enter') validateKey();
                });
            }
            buildJerseyRow();
            layoutPitchZones();
        });
        window.addEventListener('resize', layoutPitchZones);

        function buildJerseyRow() {
            const numbers = [1, 7, 11, 18, 24, 99];
            const row = document.getElementById('jerseyRow');
            numbers.forEach((n) => {
                const div = document.createElement('div');
                div.className = 'jersey';
                div.innerHTML = '<div class="num">#' + n + '</div><div class="tag">CHEERING</div>';
                row.appendChild(div);
            });
        }

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
                layoutPitchZones();
                restartOver();
            }, 800);
        }

        function moveToShowcase() {
            document.getElementById('dugoutView').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('dugoutView').style.display = 'none';
                document.getElementById('showcaseView').style.display = 'flex';
                confetti({ particleCount: 150, spread: 80, origin: { y: 0.4 }, colors: ['#EC1C24', '#FFC72C', '#ffffff'] });
                triggerCascadeReveal();
                launchFireworks();
            }, 600);
        }

        /* ===================== POWER-HIT CHALLENGE ===================== */
        const ZONES = { sixStart: 40, sixEnd: 60, fourLStart: 27, fourLEnd: 40, fourRStart: 60, fourREnd: 73 };
        let markerPos = 0;
        let markerDir = 1;
        let markerSpeed = 0.9;
        let rafId = null;
        let ballIndex = 0;
        let totalScore = 0;
        let ballLocked = false;
        const ballHistory = [];

        function layoutPitchZones() {
            const strip = document.getElementById('pitchStrip');
            if (!strip) return;
            const sweet = document.getElementById('sweetZone');
            sweet.style.left = ZONES.sixStart + '%';
            sweet.style.width = (ZONES.sixEnd - ZONES.sixStart) + '%';
        }

        function buildOverTracker() {
            const tracker = document.getElementById('overTracker');
            tracker.innerHTML = '';
            for (let i = 0; i < 6; i++) {
                const pip = document.createElement('div');
                pip.className = 'ball-pip';
                pip.id = 'pip-' + i;
                pip.innerText = (i + 1);
                tracker.appendChild(pip);
            }
        }

        function restartOver() {
            cancelAnimationFrame(rafId);
            ballIndex = 0;
            totalScore = 0;
            markerSpeed = 0.9;
            ballHistory.length = 0;
            ballLocked = false;
            document.getElementById('shotResult').innerHTML = '&nbsp;';
            document.getElementById('shotResult').className = 'shot-result';
            document.getElementById('scoreVal').innerText = '0';
            document.getElementById('ballNum').innerText = '1';
            document.getElementById('swingBtn').disabled = false;
            buildOverTracker();
            markPipCurrent(0);
            startBallAnimation();
        }

        function markPipCurrent(idx) {
            for (let i = 0; i < 6; i++) {
                const pip = document.getElementById('pip-' + i);
                if (!pip) continue;
                pip.classList.remove('current');
                if (i === idx) pip.classList.add('current');
            }
        }

        function startBallAnimation() {
            markerPos = 0;
            markerDir = 1;
            ballLocked = false;
            const marker = document.getElementById('swingMarker');
            function tick() {
                markerPos += markerDir * markerSpeed;
                if (markerPos >= 100) { markerPos = 100; markerDir = -1; }
                if (markerPos <= 0) { markerPos = 0; markerDir = 1; }
                marker.style.left = markerPos + '%';
                if (!ballLocked) rafId = requestAnimationFrame(tick);
            }
            rafId = requestAnimationFrame(tick);
        }

        function attemptSwing() {
            if (ballLocked || ballIndex >= 6) return;
            ballLocked = true;
            cancelAnimationFrame(rafId);

            const pos = markerPos;
            let runs = 0;
            let label = 'DOT BALL';
            let cls = 'r0';

            if (pos >= ZONES.sixStart && pos <= ZONES.sixEnd) {
                runs = 6; label = 'SIX!! 🚀'; cls = 'r6';
            } else if ((pos >= ZONES.fourLStart && pos < ZONES.sixStart) || (pos > ZONES.sixEnd && pos <= ZONES.fourREnd)) {
                runs = 4; label = 'FOUR! 🔥'; cls = 'r4';
            } else if (pos > ZONES.fourLEnd - 15 && pos < ZONES.fourRStart + 15) {
                runs = 1; label = 'QUICK SINGLE'; cls = 'r1';
            } else {
                runs = 0; label = 'DOT BALL'; cls = 'r0';
            }

            totalScore += runs;
            ballHistory.push(runs);

            const resultEl = document.getElementById('shotResult');
            resultEl.innerText = label;
            resultEl.className = 'shot-result ' + cls;
            document.getElementById('scoreVal').innerText = totalScore;

            const pip = document.getElementById('pip-' + ballIndex);
            pip.classList.remove('current');
            pip.classList.add('done-' + runs);
            pip.innerText = runs;

            if (runs === 6 && typeof confetti === 'function') {
                confetti({ particleCount: 90, spread: 65, origin: { y: 0.55 }, colors: ['#FFC72C', '#EC1C24', '#ffffff'] });
            }

            ballIndex++;
            markerSpeed = Math.min(markerSpeed + 0.28, 2.4);

            if (ballIndex >= 6) {
                document.getElementById('swingBtn').disabled = true;
                setTimeout(showOverSummary, 900);
            } else {
                document.getElementById('ballNum').innerText = (ballIndex + 1);
                markPipCurrent(ballIndex);
                setTimeout(startBallAnimation, 700);
            }
        }

        function showOverSummary() {
            const resultEl = document.getElementById('shotResult');
            let verdict = 'SOLID OVER, WELL PLAYED 👏';
            if (totalScore >= 24) verdict = 'ABSOLUTE MASTERBLASTER!! 🏆🔥';
            else if (totalScore >= 16) verdict = "THAT'S A MATCH-WINNING OVER! 💥";
            else if (totalScore >= 8) verdict = 'STEADY INNINGS, NICE HITTING 🏏';
            resultEl.innerText = 'OVER DONE — ' + totalScore + ' RUNS';
            resultEl.className = 'shot-result r6';
            setTimeout(() => {
                document.getElementById('dugoutScoreLine').innerText =
                    verdict + ' Final over score: ' + totalScore + ' runs off 6 balls.';
                bypassGame();
            }, 1300);
        }

        function bypassGame() {
            document.getElementById('gameView').style.display = 'none';
            document.getElementById('dugoutView').style.display = 'flex';
            confetti({ particleCount: 120, spread: 70, origin: { y: 0.4 }, colors: ['#EC1C24', '#FFC72C', '#ffffff'] });
        }

        function triggerCascadeReveal() {
            const cards = document.querySelectorAll('.flip-card');
            cards.forEach((card, index) => {
                setTimeout(() => {
                    card.classList.add('flipped');
                    setTimeout(() => card.classList.remove('flipped'), 1500);
                }, 600 + (index * 400));
            });
        }

        function toggleFlip(cardElement) { cardElement.classList.toggle('flipped'); }

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

        function launchFireworks() {
            const colors = ['#EC1C24', '#FFC72C', '#7CFF6B', '#ffffff'];
            for (let burst = 0; burst < 6; burst++) {
                setTimeout(() => {
                    const originX = Math.random() * window.innerWidth;
                    const originY = Math.random() * (window.innerHeight * 0.5);
                    for (let i = 0; i < 18; i++) {
                        const dot = document.createElement('div');
                        dot.className = 'firework-dot';
                        const angle = (Math.PI * 2 * i) / 18;
                        const dist = 60 + Math.random() * 60;
                        dot.style.setProperty('--fx', Math.cos(angle) * dist + 'px');
                        dot.style.setProperty('--fy', Math.sin(angle) * dist + 'px');
                        dot.style.left = originX + 'px';
                        dot.style.top = originY + 'px';
                        dot.style.background = colors[Math.floor(Math.random() * colors.length)];
                        document.body.appendChild(dot);
                        setTimeout(() => dot.remove(), 1200);
                    }
                }, burst * 350);
            }
        }
    </script>
</body>
</html>"""

final_layout_rendered = html_layout.replace("__LOGIN_BG_URL__", LOGIN_BACKGROUND_IMAGE)\
                                  .replace("__BEHIND_CURTAIN_URL__", BEHIND_CURTAIN_IMAGE)\
                                  .replace("__PUZZLE_IMG_URL__", PUZZLE_IMAGE)\
                                  .replace("__FINAL_PROFILE_URL__", FINAL_PROFILE_IMAGE)\
                                  .replace("__BONUS_MEMORY_URL__", BONUS_MEMORY_IMAGE)\
                                  .replace("__DUGOUT_TEAM_URL__", DUGOUT_TEAM_IMAGE)\
                                  .replace("__RCB_LOGO_URL__", RCB_LOGO_IMAGE)\
                                  .replace("__SONG_URL__", SONG_URL)

components.html(final_layout_rendered, height=1000, scrolling=False)
