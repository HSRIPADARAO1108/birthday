import streamlit as st
import streamlit.components.v1 as components

GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"
SONG_FILENAME = "januma-dinavidu-birthday-song-in-kannada-anuradha-bhat-pramod-aravind-vi_lk1Ob9t4.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

st.set_page_config(
    page_title="Happy Birthday, Gorgeous! 💖",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; }
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
        width: 100vw !important; height: 100vh !important;
        border: none !important; margin: 0 !important;
        padding: 0 !important; z-index: 999999 !important;
    }
    </style>
""", unsafe_allow_html=True)

interactive_birthday_experience = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Birthday Wishes</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        body, html {
            width: 100%; height: 100%;
            overflow: hidden;
            font-family: 'Quicksand', sans-serif;
            background-color: #0d0407;
            color: #ffffff;
            -webkit-tap-highlight-color: transparent;
            touch-action: manipulation;
        }

        .page-container { position: relative; width: 100%; height: 100%; }

        /* WATERMARK */
        .watermark {
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 99999;
            font-size: clamp(9px, 2vw, 12px);
            color: rgba(255, 133, 162, 0.55);
            font-family: 'Quicksand', sans-serif;
            font-weight: 700;
            letter-spacing: 0.5px;
            white-space: nowrap;
            pointer-events: none;
            text-shadow: 0 0 8px rgba(255,133,162,0.3);
        }

        /* SCREEN 1: LOGIN */
        .screen-login {
            position: absolute; width: 100%; height: 100%;
            background: linear-gradient(rgba(13,4,7,0.45), rgba(13,4,7,0.7)),
                        url("__LOGIN_BG_URL__") no-repeat center center;
            background-size: cover;
            display: flex; align-items: center; justify-content: center;
            z-index: 10;
            transition: opacity 1s ease-in-out;
            padding: 16px;
        }

        .login-card {
            background: rgba(13,4,7,0.65);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 2px solid rgba(255,133,162,0.4);
            padding: clamp(24px, 5vw, 40px);
            border-radius: 24px;
            text-align: center;
            max-width: 420px;
            width: 100%;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            animation: floatCard 4s ease-in-out infinite;
        }

        @keyframes floatCard {
            0%,100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .login-card h2 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(26px, 6vw, 38px);
            color: #ff85a2;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(255,133,162,0.4);
        }

        .login-card p {
            font-size: clamp(13px, 3vw, 15px);
            color: #f1f1f1;
            margin-bottom: 22px;
            line-height: 1.5;
        }

        .input-group { position: relative; margin-bottom: 20px; }

        .input-group input {
            width: 100%;
            padding: 13px 20px 13px 44px;
            background: rgba(0,0,0,0.6);
            border: 2px solid rgba(255,133,162,0.3);
            border-radius: 30px;
            color: white;
            font-size: clamp(14px, 3.5vw, 16px);
            outline: none;
            transition: border-color 0.3s;
            font-family: 'Quicksand', sans-serif;
        }

        .input-group input:focus { border-color: #ff85a2; box-shadow: 0 0 8px rgba(255,133,162,0.3); }

        .input-group i {
            position: absolute; left: 16px; top: 50%;
            transform: translateY(-50%); color: #ff85a2;
            font-size: 15px;
        }

        .login-btn {
            width: 100%;
            padding: 13px;
            background: linear-gradient(45deg, #ff758c, #ff7eb3);
            border: none; border-radius: 30px;
            color: white;
            font-size: clamp(14px, 3.5vw, 16px);
            font-weight: bold; cursor: pointer;
            box-shadow: 0 6px 20px rgba(255,117,140,0.4);
            transition: transform 0.2s, box-shadow 0.2s;
            font-family: 'Quicksand', sans-serif;
            touch-action: manipulation;
        }

        .login-btn:active { transform: scale(0.97); }
        .error-msg { color: #ff4b4b; font-size: 13px; margin-top: 10px; display: none; }

        /* SCREEN 2: STAGE */
        .screen-stage {
            position: absolute; width: 100%; height: 100%;
            display: none; background-color: #0d0407; z-index: 5;
        }

        .stage-backdrop {
            position: absolute; width: 100%; height: 100%;
            background: radial-gradient(circle, #2c0e16 0%, #0d0407 100%);
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            z-index: 1; padding: 16px; overflow-y: auto;
        }

        .surprise-photo-container {
            text-align: center;
            max-width: 480px; width: 100%;
            padding: clamp(14px, 4vw, 22px);
            background: rgba(255,255,255,0.05);
            border: 2px solid #ff758c33;
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            opacity: 0; transform: scale(0.9);
            transition: all 1s ease 1s;
        }

        .surprise-photo-container.show { opacity: 1; transform: scale(1); }

        .surprise-photo {
            width: 100%; border-radius: 16px;
            border: 3px solid #ff85a2;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            margin-bottom: 16px;
            max-height: 45vh; object-fit: cover;
        }

        .surprise-photo-container h3 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(22px, 5vw, 34px);
            color: #ff85a2; margin-bottom: 12px;
        }

        .next-puzzle-btn {
            padding: 12px 28px;
            background: linear-gradient(45deg, #11caa0, #005088);
            border: none; border-radius: 25px;
            color: white; font-weight: bold;
            font-size: clamp(13px, 3.5vw, 15px);
            cursor: pointer; transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(17,202,160,0.3);
            font-family: 'Quicksand', sans-serif;
            touch-action: manipulation;
        }

        .next-puzzle-btn:active { transform: scale(0.97); }

        /* CURTAINS */
        .curtain-overlay {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 10; overflow: hidden;
            display: flex; pointer-events: auto;
        }

        .curtain-half {
            position: absolute; top: 0; width: 50%; height: 100%;
            background-color: #b3001e;
            background-image: repeating-linear-gradient(
                to right, #800014 0%, #a3001a 4%, #b3001e 8%,
                #d60024 12%, #b3001e 16%, #a3001a 20%
            );
            box-shadow: inset 0 0 50px rgba(0,0,0,0.65);
            transition: transform 3.8s cubic-bezier(0.25,1,0.3,1), opacity 3.5s ease;
        }

        .curtain-left { left: 0; transform-origin: left center; }
        .curtain-right { right: 0; transform-origin: right center; }

        .curtain-valance {
            position: absolute; top: 0; left: 0;
            width: 100%; height: clamp(50px, 10vw, 80px);
            background-image: repeating-linear-gradient(
                to right, #800014, #b3001e 10%, #800014 20%
            );
            border-bottom: 4px solid #ffcc00;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            z-index: 12; transition: transform 3s ease-in-out;
        }

        .curtains-open .curtain-left  { transform: scaleX(0.08) translateX(-10%); }
        .curtains-open .curtain-right { transform: scaleX(0.08) translateX(10%); }
        .curtains-open .curtain-valance { transform: translateY(-100%); }

        .curtain-prompt {
            position: absolute; top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            z-index: 11; text-align: center;
            background: rgba(0,0,0,0.7);
            padding: clamp(14px, 3vw, 20px) clamp(20px, 5vw, 40px);
            border-radius: 50px;
            border: 2px solid #ffcc00;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: transform 0.3s, opacity 1.5s ease;
            width: 85%; max-width: 360px;
        }

        .curtain-prompt:active { transform: translate(-50%, -50%) scale(0.97); }

        .curtain-prompt h3 {
            font-size: clamp(15px, 4vw, 22px);
            color: #ffcc00; margin-bottom: 5px;
            letter-spacing: 1px; font-weight: 700;
        }

        .curtain-prompt p { font-size: clamp(12px, 3vw, 14px); color: #fff; }
        .curtains-open .curtain-prompt { opacity: 0; pointer-events: none; }

        /* SCREEN 3: PUZZLE */
        .screen-puzzle {
            position: absolute; width: 100%; height: 100%;
            display: none;
            background: linear-gradient(135deg, #0f0c1b 0%, #20132b 50%, #0d0407 100%);
            align-items: center; justify-content: center;
            z-index: 4; padding: 16px; overflow-y: auto;
        }

        .puzzle-window {
            background: rgba(255,255,255,0.04);
            border: 1.5px solid rgba(255,255,255,0.1);
            border-radius: 24px;
            padding: clamp(18px, 4vw, 30px);
            display: flex; flex-direction: column;
            align-items: center;
            max-width: 480px; width: 100%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.4);
        }

        .puzzle-window h2 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(24px, 6vw, 34px);
            color: #ff85a2; margin-bottom: 5px; text-align: center;
        }

        .puzzle-window > p {
            font-size: clamp(12px, 3vw, 14px);
            color: #b3b3b3; margin-bottom: 20px; text-align: center;
        }

        .puzzle-grid {
            display: grid;
            grid-template-columns: repeat(3, var(--tile-size, 100px));
            grid-template-rows:    repeat(3, var(--tile-size, 100px));
            gap: 5px;
            border-radius: 12px; overflow: hidden;
            background: rgba(0,0,0,0.2);
            padding: 5px;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }

        .puzzle-tile {
            width:  var(--tile-size, 100px);
            height: var(--tile-size, 100px);
            border-radius: 6px; cursor: pointer;
            background-image: url("__PUZZLE_IMG_URL__");
            background-size: calc(var(--tile-size, 100px) * 3) calc(var(--tile-size, 100px) * 3);
            transition: all 0.2s ease-in-out;
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
            position: relative; display: flex;
            align-items: flex-end; justify-content: flex-end;
            padding: 3px; touch-action: manipulation;
        }

        .puzzle-tile::after {
            content: ''; position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            border: 1.5px solid rgba(255,255,255,0.12);
            border-radius: 6px;
        }

        .tile-number {
            font-size: 10px; background: rgba(0,0,0,0.55);
            color: white; padding: 2px 5px;
            border-radius: 4px; font-weight: bold;
        }

        .puzzle-tile.selected {
            transform: scale(0.96); filter: brightness(1.2);
            box-shadow: 0 0 12px #ff85a2;
        }

        .solve-btn {
            width: 100%; padding: 13px;
            background: rgba(255,255,255,0.1);
            border: 1.5px solid #ff758c;
            border-radius: 30px; color: white;
            font-size: clamp(13px, 3.5vw, 15px);
            font-weight: bold; cursor: pointer;
            transition: transform 0.2s;
            font-family: 'Quicksand', sans-serif;
            touch-action: manipulation;
        }

        .solve-btn:active { transform: scale(0.97); }

        /* FINAL CARD */
        .final-card-overlay {
            position: fixed; top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(13,4,7,0.95);
            z-index: 100; display: none;
            align-items: center; justify-content: center;
            padding: 16px; overflow-y: auto;
        }

        .final-card {
            background: linear-gradient(160deg, #fff1f4 0%, #ffd6e0 60%, #ffb3c6 100%);
            border-radius: 32px;
            padding: clamp(24px, 5vw, 40px) clamp(20px, 5vw, 35px);
            max-width: 460px; width: 100%;
            text-align: center;
            box-shadow: 0 30px 70px rgba(255,117,140,0.4),
                        0 0 0 2px rgba(255,133,162,0.3);
            color: #4a1521;
            transform: scale(0.85); opacity: 0;
            transition: all 0.6s cubic-bezier(0.175,0.885,0.32,1.275);
            margin: auto;
        }

        .final-card.show { transform: scale(1); opacity: 1; }

        /* BIG profile photo */
        .profile-photo-wrap {
            width: clamp(140px, 38vw, 190px);
            height: clamp(140px, 38vw, 190px);
            border-radius: 50%;
            margin: 0 auto 18px;
            padding: 4px;
            background: linear-gradient(135deg, #ff758c, #ff85a2, #ffb3c6);
            box-shadow: 0 10px 30px rgba(209,26,91,0.35);
        }

        .profile-photo-wrap img {
            width: 100%; height: 100%;
            object-fit: cover; border-radius: 50%;
            border: 4px solid #fff;
            display: block;
        }

        .final-card h1 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(28px, 7.5vw, 44px);
            color: #d11a5b;
            margin-bottom: 6px;
            line-height: 1.2;
            text-shadow: 0 2px 8px rgba(209,26,91,0.15);
        }

        .name-tag {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(26px, 7vw, 40px);
            color: #b5004e;
            margin-bottom: 18px;
            display: block;
            text-shadow: 0 2px 6px rgba(181,0,78,0.2);
        }

        .divider {
            width: 60px; height: 3px;
            background: linear-gradient(90deg, #ff758c, #ffb3c6);
            border-radius: 2px;
            margin: 0 auto 18px;
        }

        .final-card p.wish-text {
            font-size: clamp(13px, 3.5vw, 15px);
            line-height: 1.7; margin-bottom: 18px;
            color: #5c353f; font-weight: 600;
        }

        .final-card .signature {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(22px, 5vw, 28px);
            color: #d11a5b; margin-top: 8px;
            margin-bottom: 22px;
            display: block;
        }

        .close-gift-btn {
            padding: 13px 36px;
            background: linear-gradient(45deg, #d11a5b, #ff758c);
            border: none; border-radius: 30px;
            color: white; font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(209,26,91,0.4);
            transition: transform 0.2s, box-shadow 0.2s;
            font-family: 'Quicksand', sans-serif;
            font-size: clamp(13px, 3.5vw, 15px);
            touch-action: manipulation;
        }

        .close-gift-btn:active { transform: scale(0.97); }

        /* MUSIC PLAYER */
        .retro-player-card {
            position: fixed;
            top: 12px; right: 12px;
            z-index: 10000;
            background: rgba(13,4,7,0.88);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 2px solid rgba(255,133,162,0.4);
            border-radius: 16px;
            padding: 10px 14px;
            width: clamp(160px, 45vw, 240px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .player-header {
            display: flex; align-items: center;
            justify-content: space-between; margin-bottom: 6px;
        }

        .player-title {
            font-size: clamp(10px, 2.5vw, 12px);
            font-weight: 700; color: #ff85a2;
            white-space: nowrap; overflow: hidden;
            text-overflow: ellipsis; max-width: 75%;
        }

        .player-status {
            font-size: 10px; color: #11caa0;
            display: flex; align-items: center; gap: 4px;
        }

        .status-dot {
            width: 7px; height: 7px;
            background-color: #11caa0;
            border-radius: 50%;
            animation: pulseDot 1.5s infinite;
            flex-shrink: 0;
        }

        @keyframes pulseDot {
            0%   { transform: scale(0.9); opacity: 0.6; }
            50%  { transform: scale(1.25); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.6; }
        }

        .music-icon-wrap {
            display: flex; align-items: center;
            justify-content: center; height: 36px;
        }

        .player-instruction {
            font-size: clamp(8px, 2vw, 10px);
            color: #b3b3b3; text-align: center;
            margin-top: 6px; font-weight: 600;
        }

        /* FLOATING DECOR */
        .decor {
            position: absolute; pointer-events: none;
            z-index: 15; opacity: 0.8;
            animation: floatUp 8s linear infinite;
        }

        @keyframes floatUp {
            0%   { transform: translateY(105vh) rotate(0deg); opacity: 0; }
            10%  { opacity: 0.8; }
            90%  { opacity: 0.8; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }

        @media (max-width: 480px) {
            .login-card { border-radius: 18px; }
            .retro-player-card { top: 8px; right: 8px; }
        }

        @media (max-height: 600px) {
            .login-card { padding: 18px 20px; }
            .login-card h2 { font-size: 24px; margin-bottom: 6px; }
            .login-card p  { margin-bottom: 12px; }
            .input-group   { margin-bottom: 12px; }
            .profile-photo-wrap { width: 110px; height: 110px; }
        }
    </style>
</head>
<body>

<div class="page-container">

    <!-- Watermark -->
    <div class="watermark">✨ Created by Sripada Rao H ✨</div>

    <!-- Music Player -->
    <div class="retro-player-card" id="retroPlayer">
        <div class="player-header">
            <span class="player-title">🎵 Januma Dinavidu</span>
            <span class="player-status" id="playerStatus">
                <span class="status-dot"></span> Paused
            </span>
        </div>
        <audio id="birthday-audio" autoplay loop>
            <source src="__SONG_URL__" type="audio/mpeg">
        </audio>
        <div class="music-icon-wrap">
            <i class="fa-solid fa-music" style="font-size:28px;color:#ff85a2;"></i>
        </div>
        <p class="player-instruction">👉 Tap to start audio!</p>
    </div>

    <!-- SCREEN 1: LOGIN -->
    <div class="screen-login" id="loginScreen">
        <div class="login-card">
            <h2>🌹 Private Audio Vault 🌹</h2>
            <p>Welcome, gorgeous! Enter the password on your tape record invitation to begin.</p>
            <div class="input-group">
                <i class="fa-solid fa-lock"></i>
                <input type="password" id="passwordField" placeholder="Password (Hint: varshu)"
                       autocomplete="off" autocorrect="off" autocapitalize="none">
            </div>
            <button class="login-btn" onclick="checkPassword()">Unlock Birthday Surprise ▶️</button>
            <p class="error-msg" id="errorMsg">❌ That's not the secret code, gorgeous!</p>
        </div>
    </div>

    <!-- SCREEN 2: STAGE + CURTAINS -->
    <div class="screen-stage" id="stageScreen">
        <div class="stage-backdrop">
            <div class="surprise-photo-container" id="photoReveal">
                <h3>🌹 Behind the Stage 🌹</h3>
                <img src="__BEHIND_CURTAIN_URL__" alt="Special Girl Birthday" class="surprise-photo">
                <p style="margin-bottom:16px;font-size:clamp(13px,3.5vw,15px);">Wishing you a beautiful year ahead filled with magic and smiles! ✨</p>
                <button class="next-puzzle-btn" onclick="goToPuzzle()">Unlock Birthday Challenge 🧩</button>
            </div>
        </div>
        <div class="curtain-overlay" id="curtainOverlay">
            <div class="curtain-valance"></div>
            <div class="curtain-half curtain-left"></div>
            <div class="curtain-half curtain-right"></div>
            <div class="curtain-prompt" onclick="openStageCurtain()">
                <h3>🎭 Tap to Pull Curtain 🎭</h3>
                <p>Open your birthday presentation experience</p>
            </div>
        </div>
    </div>

    <!-- SCREEN 3: PUZZLE -->
    <div class="screen-puzzle" id="puzzleScreen">
        <div class="puzzle-window">
            <h2>🎁 Cassette Box Puzzle 🎁</h2>
            <p>Tap two tiles to swap them into order (1–9) and unlock your card!</p>
            <div class="puzzle-grid" id="puzzleGrid"></div>
            <button class="solve-btn" onclick="quickSolve()">Auto-Solve (Instant Card) ✨</button>
        </div>
    </div>

    <!-- FINAL CARD -->
    <div class="final-card-overlay" id="finalOverlay">
        <div class="final-card" id="finalCard">

            <!-- BIG profile photo with gradient ring -->
            <div class="profile-photo-wrap">
                <img src="__FINAL_PROFILE_URL__" alt="Varshini">
            </div>

            <h1>Happy Birthday,</h1>
            <span class="name-tag">Beautiful Girl Varshini! 🌸</span>

            <div class="divider"></div>

            <p class="wish-text">
                May every little dream you hold in your heart find its way into reality.
                You are incredibly rare, charming, and make this world so much brighter
                just by existing in it. Thank you for being yourself, Varshini! 💖
            </p>

            <span class="signature">Forever yours ❤️</span>

            <button class="close-gift-btn" onclick="resetApp()">Close &amp; Replay 🔄</button>
        </div>
    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<script>
    const correctPassword = "varshu";
    let puzzleState = [2,0,1,5,3,4,8,6,7];
    let selectedTileIndex = null;
    let musicIsPlaying = false;

    /* Responsive tile size */
    function setTileSize() {
        const maxGrid = Math.min(window.innerWidth - 80, window.innerHeight - 280, 360);
        const tile = Math.floor((maxGrid - 16) / 3);
        document.documentElement.style.setProperty('--tile-size', tile + 'px');
    }
    setTileSize();
    window.addEventListener('resize', () => { setTileSize(); buildPuzzleBoard(); });

    /* Audio */
    function playChime() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            const ctx = new AudioContext();
            [523.25,659.25,783.99,1046.50].forEach((freq, i) => {
                setTimeout(() => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.value = freq;
                    gain.gain.setValueAtTime(0.1, ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
                    osc.connect(gain); gain.connect(ctx.destination);
                    osc.start(); osc.stop(ctx.currentTime + 1.2);
                }, i * 150);
            });
        } catch(e) {}
    }

    function playMusicStream() {
        const audio = document.getElementById('birthday-audio');
        if (!audio) return;
        audio.play().then(() => {
            musicIsPlaying = true;
            const s = document.getElementById('playerStatus');
            s.innerHTML = '<span class="status-dot"></span> Playing';
            s.style.color = '#11caa0';
        }).catch(() => {});
    }

    window.addEventListener('load', playMusicStream);
    document.addEventListener('click',      () => { if (!musicIsPlaying) playMusicStream(); }, { once: true });
    document.addEventListener('touchstart', () => { if (!musicIsPlaying) playMusicStream(); }, { once: true, passive: true });

    /* Login */
    function checkPassword() {
        const val = document.getElementById("passwordField").value.trim().toLowerCase();
        const err = document.getElementById("errorMsg");
        if (val === correctPassword) {
            err.style.display = "none";
            document.getElementById("loginScreen").style.opacity = "0";
            playMusicStream();
            setTimeout(() => {
                document.getElementById("loginScreen").style.display = "none";
                document.getElementById("stageScreen").style.display = "block";
            }, 1000);
        } else {
            err.style.display = "block";
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        const field = document.getElementById('passwordField');
        if (field) field.addEventListener('keydown', e => { if (e.key === 'Enter') checkPassword(); });
    });

    /* Curtain */
    function openStageCurtain() {
        playChime();
        document.getElementById("stageScreen").classList.add("curtains-open");
        setTimeout(() => { document.getElementById("curtainOverlay").style.pointerEvents = "none"; }, 3000);
        setTimeout(() => {
            document.getElementById("photoReveal").classList.add("show");
            spawnFloatingHearts();
        }, 1000);
    }

    function goToPuzzle() {
        document.getElementById("stageScreen").style.opacity = "0";
        setTimeout(() => {
            document.getElementById("stageScreen").style.display = "none";
            document.getElementById("puzzleScreen").style.display = "flex";
            setTileSize();
            buildPuzzleBoard();
        }, 800);
    }

    /* Puzzle */
    function buildPuzzleBoard() {
        const grid = document.getElementById("puzzleGrid");
        if (!grid) return;
        grid.innerHTML = "";
        const tileSize = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--tile-size')) || 100;

        puzzleState.forEach((pieceId, index) => {
            const tile = document.createElement("div");
            tile.className = "puzzle-tile";
            const row = Math.floor(pieceId / 3);
            const col = pieceId % 3;
            tile.style.backgroundPosition = `-${col * tileSize}px -${row * tileSize}px`;

            const label = document.createElement("span");
            label.className = "tile-number";
            label.innerText = pieceId + 1;
            tile.appendChild(label);

            tile.addEventListener('click', () => handleTileClick(index));
            tile.addEventListener('touchstart', (e) => { e.preventDefault(); handleTileClick(index); }, { passive: false });
            grid.appendChild(tile);
        });
    }

    function handleTileClick(index) {
        const tiles = document.getElementsByClassName("puzzle-tile");
        if (selectedTileIndex === null) {
            selectedTileIndex = index;
            tiles[index].classList.add("selected");
        } else {
            const first = selectedTileIndex, second = index;
            tiles[first].classList.remove("selected");
            if (first !== second) {
                [puzzleState[first], puzzleState[second]] = [puzzleState[second], puzzleState[first]];
                buildPuzzleBoard();
                checkWin();
            }
            selectedTileIndex = null;
        }
    }

    function quickSolve() {
        puzzleState = [0,1,2,3,4,5,6,7,8];
        buildPuzzleBoard();
        setTimeout(checkWin, 200);
    }

    function checkWin() {
        if (puzzleState.every((v,i) => v === i)) {
            triggerConfetti();
            document.getElementById("finalOverlay").style.display = "flex";
            setTimeout(() => document.getElementById("finalCard").classList.add("show"), 100);
        }
    }

    function triggerConfetti() {
        confetti({ particleCount: 200, spread: 90, origin: { y: 0.5 } });
        setTimeout(() => confetti({ particleCount: 100, spread: 70, origin: { y: 0.3 } }), 600);
    }

    function spawnFloatingHearts() {
        const symbols = ["❤️","💖","✨","🌸","🎈","🌹","💕"];
        for (let i = 0; i < 22; i++) {
            setTimeout(() => {
                const icon = document.createElement("div");
                icon.className = "decor";
                icon.innerText = symbols[Math.floor(Math.random() * symbols.length)];
                icon.style.left = Math.random() * 90 + "vw";
                icon.style.fontSize = Math.random() * 18 + 14 + "px";
                icon.style.animationDuration = Math.random() * 5 + 5 + "s";
                document.body.appendChild(icon);
                setTimeout(() => icon.remove(), 10000);
            }, i * 350);
        }
    }

    function resetApp() { window.location.reload(); }
</script>
</body>
</html>
"""

final_experience_rendered = (
    interactive_birthday_experience
    .replace("__LOGIN_BG_URL__",       LOGIN_BACKGROUND_IMAGE)
    .replace("__BEHIND_CURTAIN_URL__", BEHIND_CURTAIN_IMAGE)
    .replace("__PUZZLE_IMG_URL__",     PUZZLE_IMAGE)
    .replace("__FINAL_PROFILE_URL__",  FINAL_PROFILE_IMAGE)
    .replace("__SONG_URL__",           SONG_URL)
)

components.html(final_experience_rendered, height=720, scrolling=False)
