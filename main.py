import streamlit as st
import streamlit.components.v1 as components

# =========================================================================
# 📸 ENTER YOUR GITHUB INFORMATION HERE!
# Just replace these two values with your actual GitHub details.
# =========================================================================

GITHUB_USERNAME = "HSRIPADARAO1108"  # Replace with your GitHub Username
GITHUB_REPO = "birthday"            # Replace with your GitHub Repository Name
GITHUB_BRANCH = "main"                    # Change to "master" if your default branch is master

# =========================================================================
# This automatically builds the correct raw links for your uploaded images!
# =========================================================================
LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"

st.set_page_config(
    page_title="Happy Birthday, Gorgeous! 💖",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS to force the app component to render in absolute fullscreen
st.markdown("""
    <style>
    /* Hide top header bar, side menu and default margins */
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

# Main web-component package carrying optimized HTML/CSS/JS states
interactive_birthday_experience = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birthday Wishes</title>
    <!-- Fonts and Icons -->
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

        /* Interactive screens transitions container */
        .page-container {
            position: relative;
            width: 100%;
            height: 100%;
            transition: all 0.8s ease-in-out;
        }

        /* Screen 1: Login Page with Tape Record Video/GIF Background */
        .screen-login {
            position: absolute;
            width: 100%;
            height: 100%;
            /* High-fidelity lofi looping cassette tape player background replaced dynamically */
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

        /* Screen 2: Curtains Transition Stage Area */
        .screen-stage {
            position: absolute;
            width: 100%;
            height: 100%;
            display: none;
            background-color: #0d0407;
            z-index: 5;
        }

        /* Stage Backdrop Behind Curtains */
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

        /* PowerPoint Realistic Curtains Effect CSS */
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

        /* Drapery shadow effects to look realistic */
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

        /* The valance structure on top */
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

        /* PPT scrunches the curtains outward on click */
        .curtains-open .curtain-left {
            transform: scaleX(0.08) translateX(-10%);
        }

        .curtains-open .curtain-right {
            transform: scaleX(0.08) translateX(10%);
        }

        .curtains-open .curtain-valance {
            transform: translateY(-100%);
        }

        /* Instruction prompt overlaid on curtain */
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

        /* Screen 3: Happy Birthday Tape Record Puzzle Area */
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

        /* 3x3 Swap Grid layout */
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

        /* Selection styling */
        .puzzle-tile.selected {
            transform: scale(0.96);
            filter: brightness(1.2);
            box-shadow: 0 0 12px #ff85a2;
        }

        /* Final Wish Reveal Overlay Card */
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

        /* Glowing Spinning Vinyl Record Player Audio button styling */
        .music-controller {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            background: rgba(13, 4, 7, 0.8);
            border: 2px solid #ff85a2;
            border-radius: 50%;
            width: 54px;
            height: 54px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(255, 133, 162, 0.6);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .music-controller:hover {
            transform: scale(1.1);
            box-shadow: 0 0 25px rgba(255, 133, 162, 0.9);
        }

        .music-controller i {
            color: #ff85a2;
            font-size: 28px;
        }

        .record-spinning {
            animation: spinRecord 3.5s linear infinite;
        }

        .record-paused {
            animation-play-state: paused !important;
        }

        @keyframes spinRecord {
            100% { transform: rotate(360deg); }
        }

        /* Floating decoration objects */
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

        <!-- Floating Music Controller Widget -->
        <div class="music-controller" id="musicCtrl" onclick="toggleMusic()">
            <i class="fa-solid fa-compact-disc record-spinning record-paused" id="discIcon"></i>
        </div>

        <!-- Hidden YouTube Audio Streaming Iframe Target Container -->
        <div id="yt-player" style="position: absolute; width: 0; height: 0; opacity: 0; pointer-events: none;"></div>

        <!-- SCREEN 1: LOGIN WITH RETRO LOOPING TAPE BACKGROUND -->
        <div class="screen-login" id="loginScreen">
            <div class="login-card">
                <h2>🌹 Private Audio Vault 🌹</h2>
                <p>Welcome, gorgeous! Enter the password on your tape record invitation to begin.</p>
                
                <div class="input-group">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" id="passwordField" placeholder="Password (Hint: taperecord)">
                </div>
                
                <button class="login-btn" onclick="checkPassword()">Unlock Birthday surprise ▶️</button>
                <p class="error-msg" id="errorMsg">❌ That's not the secret code, gorgeous!</p>
            </div>
        </div>

        <!-- SCREEN 2: REALISTIC STAGE WITH PPT CURTAINS -->
        <div class="screen-stage" id="stageScreen">
            <!-- Stage Background containing target reveal image -->
            <div class="stage-backdrop">
                <div class="surprise-photo-container" id="photoReveal">
                    <h3>🌹 Behind the Stage 🌹</h3>
                    <img src="__BEHIND_CURTAIN_URL__" alt="Special Girl Birthday" class="surprise-photo">
                    <p style="margin-bottom: 20px; font-size: 15px;">Wishing you a beautiful year ahead filled with magic and smiles! ✨</p>
                    <button class="next-puzzle-btn" onclick="goToPuzzle()">Unlock Birthday Challenge 🧩</button>
                </div>
            </div>

            <!-- Curtains Layers and Puller Prompt Overlay -->
            <div class="curtain-overlay" id="curtainOverlay">
                <div class="curtain-valance"></div>
                <div class="curtain-half curtain-left"></div>
                <div class="curtain-half curtain-right"></div>
                
                <!-- Curtain Prompt Trigger Box -->
                <div class="curtain-prompt" onclick="openStageCurtain()">
                    <h3>🎭 Click Curtain to Pull Back 🎭</h3>
                    <p>Open up your birthday presentation experience</p>
                </div>
            </div>
        </div>

        <!-- SCREEN 3: BIRTHDAY SLIDING CASSETTE PUZZLE -->
        <div class="screen-puzzle" id="puzzleScreen">
            <div class="puzzle-window">
                <h2>🎁 Cassette Box Puzzle 🎁</h2>
                <p>Click two segments of the birthday card image to swap them into numerical order (1 to 9) to unlock your card!</p>
                
                <div class="puzzle-grid" id="puzzleGrid">
                    <!-- Javascript populates 3x3 tiles dynamic positions -->
                </div>
                
                <button class="login-btn" style="background: rgba(255,255,255,0.1); border: 1.5px solid #ff758c; box-shadow: none;" onclick="quickSolve()">Auto-Solve (Instant Card) ✨</button>
            </div>
        </div>

        <!-- FINAL GIFT CARD DISPLAY OVERLAY -->
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
        // Setup state variables
        const correctPassword = "taperecord";
        
        // Puzzle pieces tracking state
        // Dynamic target index representation for 3x3 layout
        let puzzleState = [2, 0, 1, 5, 3, 4, 8, 6, 7]; // Scrambled indices initial
        let selectedTileIndex = null;

        // Custom chime audio synthesizer using browser web API
        function playChime() {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                const ctx = new AudioContext();
                
                // Magical chime note array frequencies
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

        // YouTube API Hidden Integration Layer
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        var player;
        var musicIsPlaying = false;

        function onYouTubeIframeAPIReady() {
            player = new YT.Player('yt-player', {
                height: '0',
                width: '0',
                videoId: 'WNL9yedU25g',
                playerVars: {
                    'autoplay': 0,
                    'start': 41,        // Starts at exact request point (41s)
                    'controls': 0,
                    'loop': 1,
                    'playlist': 'WNL9yedU25g',
                    'disablekb': 1,
                    'fs': 0,
                    'modestbranding': 1,
                    'rel': 0,
                    'showinfo': 0
                },
                events: {
                    'onReady': onPlayerReady
                }
            });
        }

        function onPlayerReady(event) {
            console.log("Audio stream loaded successfully.");
        }

        function playMusicStream() {
            if (player && typeof player.playVideo === 'function') {
                player.playVideo();
                musicIsPlaying = true;
                document.getElementById('discIcon').classList.remove('record-paused');
            }
        }

        function pauseMusicStream() {
            if (player && typeof player.pauseVideo === 'function') {
                player.pauseVideo();
                musicIsPlaying = false;
                document.getElementById('discIcon').classList.add('record-paused');
            }
        }

        function toggleMusic() {
            if (musicIsPlaying) {
                pauseMusicStream();
            } else {
                playMusicStream();
            }
        }

        // Login Page check input
        function checkPassword() {
            const val = document.getElementById("passwordField").value.trim().toLowerCase();
            const error = document.getElementById("errorMsg");
            
            if (val === correctPassword) {
                error.style.display = "none";
                document.getElementById("loginScreen").style.opacity = "0";
                
                // Trigger customized song streaming safely on user action click
                playMusicStream();
                
                setTimeout(() => {
                    document.getElementById("loginScreen").style.display = "none";
                    document.getElementById("stageScreen").style.display = "block";
                }, 1000);
            } else {
                error.style.display = "block";
            }
        }

        // Action Trigger for Stage PowerPoint Curtain Transition
        function openStageCurtain() {
            playChime();
            const stage = document.getElementById("stageScreen");
            stage.classList.add("curtains-open");
            
            // Remove the interaction barrier to click items behind curtains
            setTimeout(() => {
                document.getElementById("curtainOverlay").style.pointerEvents = "none";
            }, 3000);

            // Display revealed card content container
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

        // Render dynamic puzzle card slicing with coordinate positions
        function buildPuzzleBoard() {
            const grid = document.getElementById("puzzleGrid");
            grid.innerHTML = "";
            
            puzzleState.forEach((pieceId, index) => {
                const tile = document.createElement("div");
                tile.className = "puzzle-tile";
                tile.setAttribute("data-index", index);
                tile.setAttribute("data-piece-id", pieceId);
                
                // Calculate correct background slicing position coordinates
                const row = Math.floor(pieceId / 3);
                const col = pieceId % 3;
                tile.style.backgroundPosition = `-${col * 110}px -${row * 110}px`;
                
                // Add sub-text layout sequence label
                const label = document.createElement("span");
                label.className = "tile-number";
                label.innerText = (pieceId + 1);
                tile.appendChild(label);
                
                tile.onclick = () => handleTileClick(index);
                grid.appendChild(tile);
            });
        }

        // Logic for puzzle pieces click and swap actions
        function handleTileClick(index) {
            const tiles = document.getElementsByClassName("puzzle-tile");
            
            if (selectedTileIndex === null) {
                // First tile selected
                selectedTileIndex = index;
                tiles[index].classList.add("selected");
            } else {
                // Second tile selected - perform array swapping
                const firstIndex = selectedTileIndex;
                const secondIndex = index;
                
                // Clear state selection style
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

        // Auto completion helper for easily exploring outcomes
        function quickSolve() {
            puzzleState = [0, 1, 2, 3, 4, 5, 6, 7, 8];
            buildPuzzleBoard();
            setTimeout(checkWin, 200);
        }

        function checkWin() {
            const isSolved = puzzleState.every((val, index) => val === index);
            if (isSolved) {
                // Launch beautiful full-screen celebration
                triggerConfetti();
                const overlay = document.getElementById("finalOverlay");
                const card = document.getElementById("finalCard");
                
                overlay.style.display = "flex";
                setTimeout(() => {
                    card.classList.add("show");
                }, 100);
            }
        }

        // Confetti script engine trigger
        function triggerConfetti() {
            confetti({
                particleCount: 150,
                spread: 80,
                origin: { y: 0.6 }
            });
        }

        // Spawns beautiful floating hearts upon curtain release
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
                    
                    // Cleanup out of bounds
                    setTimeout(() => icon.remove(), 10000);
                }, i * 400);
            }
        }

        // Hard Reset App States
        function resetApp() {
            window.location.reload();
        }
    </script>
</body>
</html>
"""

# Dynamic template replacement rendering matching correct raw link formats
final_experience_rendered = interactive_birthday_experience.replace("__LOGIN_BG_URL__", LOGIN_BACKGROUND_IMAGE) \
                                                          .replace("__BEHIND_CURTAIN_URL__", BEHIND_CURTAIN_IMAGE) \
                                                          .replace("__PUZZLE_IMG_URL__", PUZZLE_IMAGE) \
                                                          .replace("__FINAL_PROFILE_URL__", FINAL_PROFILE_IMAGE)

# Render full screen responsive viewport within Streamlit iframe
components.html(final_experience_rendered, height=720, scrolling=False)
