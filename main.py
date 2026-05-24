import streamlit as st
import streamlit.components.v1 as components

GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"
SONG_FILENAME = "Januma Dinavidu _ Birthday Song in Kannada _ Anuradha Bhat _ Pramod Aravind _ Vijay Krishna __.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

st.set_page_config(
    page_title="Happy Birthday, Gorgeous! 💖",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    [data-testid="stHeader"] {
        display: none !important;
    }
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
    }
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 999999 !important;
    }
    </style>
""", unsafe_allow_html=True)

interactive_birthday_experience = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birthday Wishes</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght=700&family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body, html {
            width: 100%;
            height: 100%;
            overflow: hidden;
            font-family: 'Quicksand', sans-serif;
            background-color: #0d0407;
            color: #ffffff;
        }

        .page-container {
            position: relative;
            width: 100%;
            height: 100%;
            transition: all 0.8s ease-in-out;
        }

        .screen-login {
            position: absolute;
            width: 100%;
            height: 100%;
            background: linear-gradient(rgba(13, 4, 7, 0.45), rgba(13, 4, 7, 0.7)), 
                        url("__LOGIN_BG_URL__") no-repeat center center;
            background-size: cover;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
            transition: opacity 1s ease-in-out;
        }

        .login-card {
            background: rgba(13, 4, 7, 0.65);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 2px solid rgba(255, 133, 162, 0.4);
            padding: 40px;
            border-radius: 24px;
            text-align: center;
            max-width: 420px;
            width: 90%;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
            animation: floatCard 4s ease-in-out infinite;
        }

        @keyframes floatCard {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .login-card h2 {
            font-family: 'Dancing Script', cursive;
            font-size: 38px;
            color: #ff85a2;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(255, 133, 162, 0.4);
        }

        .login-card p {
            font-size: 15px;
            color: #f1f1f1;
            margin-bottom: 25px;
            line-height: 1.4;
        }

        .input-group {
            position: relative;
            margin-bottom: 25px;
        }

        .input-group input {
            width: 100%;
            padding: 14px 20px 14px 45px;
            background: rgba(0, 0, 0, 0.6);
            border: 2px solid rgba(255, 133, 162, 0.3);
            border-radius: 30px;
            color: white;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }

        .input-group input:focus {
            border-color: #ff85a2;
            box-shadow: 0 0 8px rgba(255, 133, 162, 0.3);
        }

        .input-group i {
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #ff85a2;
        }

        .login-btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(45deg, #ff758c, #ff7eb3);
            border: none;
            border-radius: 30px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(255, 117, 140, 0.4);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 117, 140, 0.6);
        }

        .error-msg {
            color: #ff4b4b;
            font-size: 13px;
            margin-top: 10px;
            display: none;
        }

        .screen-stage {
            position: absolute;
            width: 100%;
            height: 100%;
            display: none;
            background-color: #0d0407;
            z-index: 5;
        }

        .stage-backdrop {
            position: absolute;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, #2c0e16 0%, #0d0407 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 1;
        }

        .surprise-photo-container {
            text-align: center;
            max-width: 500px;
            width: 85%;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid #ff758c33;
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            opacity: 0;
            transform: scale(0.9);
            transition: all 1s ease 1s;
        }

        .surprise-photo-container.show {
            opacity: 1;
            transform: scale(1);
        }

        .surprise-photo {
            width: 100%;
            border-radius: 16px;
            border: 3px solid #ff85a2;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }

        .surprise-photo-container h3 {
            font-family: 'Dancing Script', cursive;
            font-size: 34px;
            color: #ff85a2;
            margin-bottom: 15px;
        }

        .next-puzzle-btn {
            padding: 12px 30px;
            background: linear-gradient(45deg, #11caa0, #005088);
            border: none;
            border-radius: 25px;
            color: white;
            font-weight: bold;
            font-size: 15px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(17, 202, 160, 0.3);
        }

        .next-puzzle-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(17, 202, 160, 0.5);
        }

        .curtain-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10;
            overflow: hidden;
            display: flex;
            pointer-events: auto;
        }

        .curtain-half {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            background-color: #b3001e;
            background-image: repeating-linear-gradient(
                to right,
                #800014 0%,
                #a3001a 4%,
                #b3001e 8%,
                #d60024 12%,
                #b3001e 16%,
                #a3001a 20%
            );
            box-shadow: inset 0 0 50px rgba(0,0,0,0.65);
            transition: transform 3.8s cubic-bezier(0.25, 1, 0.3, 1), opacity 3.5s ease;
        }

        .curtain-left {
            left: 0;
            transform-origin: left center;
        }

        .curtain-right {
            right: 0;
            transform-origin: right center;
        }

        .curtain-valance {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 80px;
            background-image: repeating-linear-gradient(
                to right,
                #800014,
                #b3001e 10%,
                #800014 20%
            );
            border-bottom: 4px solid #ffcc00;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            z-index: 12;
            transition: transform 3s ease-in-out;
        }

        .curtains-open .curtain-left {
            transform: scaleX(0.08) translateX(-10%);
        }

        .curtains-open .curtain-right {
            transform: scaleX(0.08) translateX(10%);
        }

        .curtains-open .curtain-valance {
            transform: translateY(-100%);
        }

        .curtain-prompt {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 11;
            text-align: center;
            background: rgba(0,0,0,0.7);
            padding: 20px 40px;
            border-radius: 50px;
            border: 2px solid #ffcc00;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: transform 0.3s, opacity 1.5s ease;
        }

        .curtain-prompt:hover {
            transform: translate(-50%, -52%) scale(1.05);
        }

        .curtain-prompt h3 {
            font-size: 22px;
            color: #ffcc00;
            margin-bottom: 5px;
            letter-spacing: 1px;
            font-weight: 700;
        }

        .curtain-prompt p {
            font-size: 14px;
            color: #fff;
        }

        .curtains-open .curtain-prompt {
            opacity: 0;
            pointer-events: none;
        }

        .screen-puzzle {
            position: absolute;
            width: 100%;
            height: 100%;
            display: none;
            background: linear-gradient(135deg, #0f0c1b 0%, #20132b 50%, #0d0407 100%);
            align-items: center;
            justify-content: center;
            z-index: 4;
            padding: 20px;
        }

        .puzzle-window {
            background: rgba(255, 255, 255, 0.04);
            border: 1.5px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        }

        .puzzle-window h2 {
            font-family: 'Dancing Script', cursive;
            font-size: 34px;
            color: #ff85a2;
            margin-bottom: 5px;
            text-align: center;
        }

        .puzzle-window p {
            font-size: 14px;
            color: #b3b3b3;
            margin-bottom: 25px;
            text-align: center;
        }

        .puzzle-grid {
            display: grid;
            grid-template-columns: repeat(3, 110px);
            grid-template-rows: repeat(3, 110px);
            gap: 6px;
            border-radius: 12px;
            overflow: hidden;
            background: rgba(0, 0, 0, 0.2);
            padding: 6px;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.4);
            margin-bottom: 25px;
        }

        .puzzle-tile {
            width: 110px;
            height: 110px;
            border-radius: 6px;
            cursor: pointer;
            background-image: url("__PUZZLE_IMG_URL__");
            background-size: 330px 330px;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
            position: relative;
            display: flex;
            align-items: flex-end;
            justify-content: flex-end;
            padding: 4px;
        }

        .puzzle-tile::after {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            border: 1.5px solid rgba(255,255,255,0.12);
            border-radius: 6px;
        }

        .tile-number {
            font-size: 11px;
            background: rgba(0,0,0,0.55);
            color: white;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
        }

        .puzzle-tile.selected {
            transform: scale(0.96);
            filter: brightness(1.2);
            box-shadow: 0 0 12px #ff85a2;
        }

        .final-card-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(13, 4, 7, 0.95);
            z-index: 100;
            display: none;
            align-items: center;
            justify-content: center;
        }

        .final-card {
            background: radial-gradient(circle at top left, #fff1f4 0%, #ffe0e6 100%);
            border-radius: 28px;
            padding: 45px 35px;
            max-width: 480px;
            width: 90%;
            text-align: center;
            box-shadow: 0 25px 55px rgba(255, 117, 140, 0.3);
            color: #4a1521;
            transform: scale(0.85);
            opacity: 0;
            transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .final-card.show {
            transform: scale(1);
            opacity: 1;
        }

        .final-card h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 46px;
            color: #d11a5b;
            margin-bottom: 20px;
        }

        .final-card img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 8px 20px rgba(209, 26, 91, 0.2);
            margin-bottom: 25px;
        }

        .final-card p {
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 25px;
            color: #5c353f;
            font-weight: 600;
        }

        .final-card .signature {
            font-family: 'Dancing Script', cursive;
            font-size: 28px;
            color: #d11a5b;
            margin-top: 15px;
        }

        .close-gift-btn {
            padding: 12px 35px;
            background: linear-gradient(45deg, #d11a5b, #ff758c);
            border: none;
            border-radius: 25px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(209, 26, 91, 0.3);
            transition: transform 0.2s;
        }

        .close-gift-btn:hover {
            transform: translateY(-2px);
        }

        .retro-player-card {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            background: rgba(13, 4, 7, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 2px solid rgba(255, 133, 162, 0.4);
            border-radius: 20px;
            padding: 15px;
            width: 270px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .retro-player-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(255, 133, 162, 0.3);
        }

        .player-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .player-title {
            font-size: 12px;
            font-weight: 700;
            color: #ff85a2;
            text-shadow: 0 0 5px rgba(255, 133, 162, 0.3);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 170px;
        }

        .player-status {
            font-size: 11px;
            color: #11caa0;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background-color: #11caa0;
            border-radius: 50%;
            animation: pulseDot 1.5s infinite;
        }

        @keyframes pulseDot {
            0% { transform: scale(0.9); opacity: 0.6; }
            50% { transform: scale(1.25); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.6; }
        }

        .iframe-wrapper {
            width: 240px;
            height: 140px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: #000;
        }

        .player-instruction {
            font-size: 10px;
            color: #b3b3b3;
            text-align: center;
            margin-top: 8px;
            font-weight: 600;
        }

        .decor {
            position: absolute;
            pointer-events: none;
            z-index: 15;
            opacity: 0.8;
            animation: floatUp 8s linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(105vh) rotate(0deg); opacity: 0; }
            10% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>

    <div class="page-container">

        <div class="retro-player-card" id="retroPlayer">
            <div class="player-header">
                <span class="player-title">🎵 Januma Dinavidu</span>
                <span class="player-status" id="playerStatus">
                    <span class="status-dot"></span> Paused
                </span>
            </div>
            
            <div class="iframe-wrapper" style="display: flex; align-items: center; justify-content: center;">
                <audio id="birthday-audio" autoplay loop>
                    <source src="__SONG_URL__" type="audio/mpeg">
                </audio>
                <i class="fa-solid fa-music" style="font-size: 40px; color: #ff85a2;"></i>
            </div>
            
            <p class="player-instruction">👉 Tap anywhere on screen to start audio!</p>
        </div>

        <div class="screen-login" id="loginScreen">
            <div class="login-card">
                <h2>🌹 Private Audio Vault 🌹</h2>
                <p>Welcome, gorgeous! Enter the password on your tape record invitation to begin.</p>
                
                <div class="input-group">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" id="passwordField" placeholder="Password (Hint: varshu)">
                </div>
                
                <button class="login-btn" onclick="checkPassword()">Unlock Birthday surprise ▶️</button>
                <p class="error-msg" id="errorMsg">❌ That's not the secret code, gorgeous!</p>
            </div>
        </div>

        <div class="screen-stage" id="stageScreen">
            <div class="stage-backdrop">
                <div class="surprise-photo-container" id="photoReveal">
                    <h3>🌹 Behind the Stage 🌹</h3>
                    <img src="__BEHIND_CURTAIN_URL__" alt="Special Girl Birthday" class="surprise-photo">
                    <p style="margin-bottom: 20px; font-size: 15px;">Wishing you a beautiful year ahead filled with magic and smiles! ✨</p>
                    <button class="next-puzzle-btn" onclick="goToPuzzle()">Unlock Birthday Challenge 🧩</button>
                </div>
            </div>

            <div class="curtain-overlay" id="curtainOverlay">
                <div class="curtain-valance"></div>
                <div class="curtain-half curtain-left"></div>
                <div class="curtain-half curtain-right"></div>
                
                <div class="curtain-prompt" onclick="openStageCurtain()">
                    <h3>🎭 Click Curtain to Pull Back 🎭</h3>
                    <p>Open up your birthday presentation experience</p>
                </div>
            </div>
        </div>

        <div class="screen-puzzle" id="puzzleScreen">
            <div class="puzzle-window">
                <h2>🎁 Cassette Box Puzzle 🎁</h2>
                <p>Click two segments of the birthday card image to swap them into numerical order (1 to 9) to unlock your card!</p>
                
                <div class="puzzle-grid" id="puzzleGrid">
                </div>
                
                <button class="login-btn" style="background: rgba(255,255,255,0.1); border: 1.5px solid #ff758c; box-shadow: none;" onclick="quickSolve()">Auto-Solve (Instant Card) ✨</button>
            </div>
        </div>

        <div class="final-card-overlay" id="finalOverlay">
            <div class="final-card" id="finalCard">
                <img src="__FINAL_PROFILE_URL__" alt="Gorgeous Girl Profile">
                <h1>Happy Birthday, Beautiful!</h1>
                <p>May every little dream you hold in your heart find its way into reality. You are incredibly rare, charming, and make this world so much brighter just by existing in it. Thank you for being yourself!</p>
                <p class="signature">Forever yours ❤️</p>
                <button class="close-gift-btn" onclick="resetApp()">Close & Replay 🔄</button>
            </div>
        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    
    <script>
        const correctPassword = "varshu";
        
        let puzzleState = [2, 0, 1, 5, 3, 4, 8, 6, 7];
        let selectedTileIndex = null;
        let musicIsPlaying = false;

        function playChime() {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                const ctx = new AudioContext();
                
                const notes = [523.25, 659.25, 783.99, 1046.50];
                notes.forEach((freq, index) => {
                    setTimeout(() => {
                        const osc = ctx.createOscillator();
                        const gain = ctx.createGain();
                        osc.type = 'sine';
                        osc.frequency.value = freq;
                        
                        gain.gain.setValueAtTime(0.1, ctx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
                        
                        osc.connect(gain);
                        gain.connect(ctx.destination);
                        osc.start();
                        osc.stop(ctx.currentTime + 1.2);
                    }, index * 150);
                });
            } catch(e) {
                console.log("Audio not allowed yet");
            }
        }

        window.addEventListener('load', playMusicStream);

        document.addEventListener('click', function() {
            if (!musicIsPlaying) {
                playMusicStream();
            }
        }, { once: true });

        document.addEventListener('touchstart', function() {
            if (!musicIsPlaying) {
                playMusicStream();
            }
        }, { once: true });

        function playMusicStream() {
            const audio = document.getElementById('birthday-audio');
            if (audio) {
                audio.play().then(() => {
                    musicIsPlaying = true;
                    const statusLabel = document.getElementById('playerStatus');
                    statusLabel.innerHTML = '<span class="status-dot"></span> Playing';
                    statusLabel.style.color = '#11caa0';
                }).catch(e => console.log("Autoplay blocked, waiting for user click"));
            }
        }

        function checkPassword() {
            const val = document.getElementById("passwordField").value.trim().toLowerCase();
            const error = document.getElementById("errorMsg");
            
            if (val === correctPassword) {
                error.style.display = "none";
                document.getElementById("loginScreen").style.opacity = "0";
                
                playMusicStream();
                
                setTimeout(() => {
                    document.getElementById("loginScreen").style.display = "none";
                    document.getElementById("stageScreen").style.display = "block";
                }, 1000);
            } else {
                error.style.display = "block";
            }
        }

        function openStageCurtain() {
            playChime();
            const stage = document.getElementById("stageScreen");
            stage.classList.add("curtains-open");
            
            setTimeout(() => {
                document.getElementById("curtainOverlay").style.pointerEvents = "none";
            }, 3000);

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
                buildPuzzleBoard();
            }, 800);
        }

        function buildPuzzleBoard() {
            const grid = document.getElementById("puzzleGrid");
            grid.innerHTML = "";
            
            puzzleState.forEach((pieceId, index) => {
                const tile = document.createElement("div");
                tile.className = "puzzle-tile";
                tile.setAttribute("data-index", index);
                tile.setAttribute("data-piece-id", pieceId);
                
                const row = Math.floor(pieceId / 3);
                const col = pieceId % 3;
                tile.style.backgroundPosition = `-${col * 110}px -${row * 110}px`;
                
                const label = document.createElement("span");
                label.className = "tile-number";
                label.innerText = (pieceId + 1);
                tile.appendChild(label);
                
                tile.onclick = () => handleTileClick(index);
                grid.appendChild(tile);
            });
        }

        function handleTileClick(index) {
            const tiles = document.getElementsByClassName("puzzle-tile");
            
            if (selectedTileIndex === null) {
                selectedTileIndex = index;
                tiles[index].classList.add("selected");
            } else {
                const firstIndex = selectedTileIndex;
                const secondIndex = index;
                
                tiles[firstIndex].classList.remove("selected");
                
                if (firstIndex !== secondIndex) {
                    const temp = puzzleState[firstIndex];
                    puzzleState[firstIndex] = puzzleState[secondIndex];
                    puzzleState[secondIndex] = temp;
                    
                    buildPuzzleBoard();
                    checkWin();
                }
                
                selectedTileIndex = null;
            }
        }

        function quickSolve() {
            puzzleState = [0, 1, 2, 3, 4, 5, 6, 7, 8];
            buildPuzzleBoard();
            setTimeout(checkWin, 200);
        }

        function checkWin() {
            const isSolved = puzzleState.every((val, index) => val === index);
            if (isSolved) {
                triggerConfetti();
                const overlay = document.getElementById("finalOverlay");
                const card = document.getElementById("finalCard");
                
                overlay.style.display = "flex";
                setTimeout(() => {
                    card.classList.add("show");
                }, 100);
            }
        }

        function triggerConfetti() {
            confetti({
                particleCount: 150,
                spread: 80,
                origin: { y: 0.6 }
            });
        }

        function spawnFloatingHearts() {
            const symbols = ["❤️", "💖", "✨", "🌸", "🎈"];
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const icon = document.createElement("div");
                    icon.className = "decor";
                    icon.innerText = symbols[Math.floor(Math.random() * symbols.length)];
                    icon.style.left = Math.random() * 95 + "vw";
                    icon.style.fontSize = Math.random() * 20 + 15 + "px";
                    icon.style.animationDuration = Math.random() * 5 + 5 + "s";
                    document.body.appendChild(icon);
                    
                    setTimeout(() => icon.remove(), 10000);
                }, i * 400);
            }
        }

        function resetApp() {
            window.location.reload();
        }
    </script>
</body>
</html>
"""

final_experience_rendered = interactive_birthday_experience.replace("__LOGIN_BG_URL__", LOGIN_BACKGROUND_IMAGE) \
                                                          .replace("__BEHIND_CURTAIN_URL__", BEHIND_CURTAIN_IMAGE) \
                                                          .replace("__PUZZLE_IMG_URL__", PUZZLE_IMAGE) \
                                                          .replace("__FINAL_PROFILE_URL__", FINAL_PROFILE_IMAGE) \
                                                          .replace("__SONG_URL__", SONG_URL)

components.html(final_experience_rendered, height=720, scrolling=False)
