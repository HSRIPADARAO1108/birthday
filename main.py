```python
import streamlit as st
import streamlit.components.v1 as components

# =========================================================================
# 📸 ENTER YOUR GITHUB INFORMATION HERE!
# =========================================================================

GITHUB_USERNAME = "HSRIPADARAO1108"
GITHUB_REPO = "birthday"
GITHUB_BRANCH = "main"

# =========================================================================
# IMAGE + AUDIO LINKS
# =========================================================================

LOGIN_BACKGROUND_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/LOGIN_BACKGROUND_IMAGE.jpeg"
BEHIND_CURTAIN_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/BEHIND_CURTAIN_IMAGE.jpeg"
PUZZLE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/PUZZLE_IMAGE.jpeg"
FINAL_PROFILE_IMAGE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/FINAL_PROFILE_IMAGE.jpeg"

# AUDIO FILE
SONG_FILENAME = "Januma Dinavidu _ Birthday Song in Kannada _ Anuradha Bhat _ Pramod Aravind _ Vijay Krishna __.mp3"
SONG_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/{SONG_FILENAME.replace(' ', '%20')}"

# =========================================================================
# STREAMLIT SETTINGS
# =========================================================================

st.set_page_config(
    page_title="Happy Birthday 💖",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================================
# FULLSCREEN CSS
# =========================================================================

st.markdown("""
<style>
[data-testid="stHeader"] {
    display: none !important;
}

.main .block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

iframe {
    position: fixed !important;
    top: 0;
    left: 0;
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================================
# MAIN HTML
# =========================================================================

html_code = """
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Birthday Surprise</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body,html{
    width:100%;
    height:100%;
    overflow:hidden;
    font-family:'Quicksand',sans-serif;
    background:#0d0407;
}

/* ===================================================== */
/* LOGIN SCREEN */
/* ===================================================== */

.screen-login{
    width:100%;
    height:100vh;

    background:
    linear-gradient(rgba(0,0,0,0.5),rgba(0,0,0,0.7)),
    url("__LOGIN_BG_URL__");

    background-size:cover;
    background-position:center;

    display:flex;
    align-items:center;
    justify-content:center;
}

.login-card{
    width:90%;
    max-width:420px;

    padding:40px;

    border-radius:25px;

    background:rgba(0,0,0,0.5);

    backdrop-filter:blur(12px);

    border:2px solid rgba(255,255,255,0.2);

    text-align:center;

    box-shadow:0 10px 30px rgba(0,0,0,0.5);
}

.login-card h1{
    color:#ff85a2;
    font-size:42px;
    margin-bottom:15px;
    font-family:'Dancing Script',cursive;
}

.login-card p{
    color:white;
    margin-bottom:25px;
    line-height:1.6;
}

.input-group{
    position:relative;
    margin-bottom:20px;
}

.input-group input{
    width:100%;
    padding:14px 18px 14px 45px;

    border:none;
    outline:none;

    border-radius:30px;

    background:rgba(255,255,255,0.1);

    color:white;
    font-size:16px;
}

.input-group i{
    position:absolute;
    left:18px;
    top:50%;
    transform:translateY(-50%);
    color:#ff85a2;
}

.login-btn{
    width:100%;
    padding:14px;

    border:none;
    border-radius:30px;

    cursor:pointer;

    background:linear-gradient(45deg,#ff758c,#ff7eb3);

    color:white;
    font-size:16px;
    font-weight:bold;

    transition:0.3s;
}

.login-btn:hover{
    transform:scale(1.03);
}

.error-msg{
    color:red;
    margin-top:10px;
    display:none;
}

/* ===================================================== */
/* STAGE SCREEN */
/* ===================================================== */

.screen-stage{
    display:none;
    width:100%;
    height:100vh;
    position:relative;
    overflow:hidden;
    background:#0d0407;
}

.stage-backdrop{
    width:100%;
    height:100%;
    display:flex;
    justify-content:center;
    align-items:center;
}

.photo-box{
    width:90%;
    max-width:500px;

    padding:20px;

    background:rgba(255,255,255,0.05);

    border-radius:25px;

    text-align:center;

    border:2px solid rgba(255,255,255,0.1);
}

.photo-box img{
    width:100%;
    border-radius:20px;
    margin-bottom:20px;
}

.photo-box h2{
    color:#ff85a2;
    margin-bottom:15px;
    font-size:38px;
    font-family:'Dancing Script',cursive;
}

.next-btn{
    padding:12px 30px;

    border:none;
    border-radius:30px;

    cursor:pointer;

    background:linear-gradient(45deg,#11caa0,#005088);

    color:white;
    font-weight:bold;
}

/* ===================================================== */
/* CURTAINS */
/* ===================================================== */

.curtain-overlay{
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    display:flex;
    z-index:10;
}

.curtain{
    width:50%;
    height:100%;
    background:
    repeating-linear-gradient(
    to right,
    #7a0014,
    #b3001e 10%,
    #7a0014 20%
    );

    transition:3s ease;
}

.left{
    transform-origin:left;
}

.right{
    transform-origin:right;
}

.curtains-open .left{
    transform:translateX(-100%);
}

.curtains-open .right{
    transform:translateX(100%);
}

.curtain-text{
    position:absolute;

    top:50%;
    left:50%;

    transform:translate(-50%,-50%);

    color:white;

    background:rgba(0,0,0,0.7);

    padding:20px 40px;

    border-radius:50px;

    cursor:pointer;

    text-align:center;

    border:2px solid gold;

    z-index:11;
}

.curtains-open .curtain-text{
    display:none;
}

/* ===================================================== */
/* PUZZLE SCREEN */
/* ===================================================== */

.screen-puzzle{
    display:none;

    width:100%;
    height:100vh;

    justify-content:center;
    align-items:center;

    background:linear-gradient(135deg,#0f0c1b,#20132b,#0d0407);
}

.puzzle-box{
    text-align:center;
}

.puzzle-box h2{
    color:#ff85a2;
    font-size:40px;
    margin-bottom:10px;
    font-family:'Dancing Script',cursive;
}

.puzzle-grid{
    display:grid;
    grid-template-columns:repeat(3,110px);
    gap:5px;
    margin-top:20px;
}

.tile{
    width:110px;
    height:110px;

    background-image:url("__PUZZLE_IMG_URL__");
    background-size:330px 330px;

    border-radius:8px;

    cursor:pointer;
}

/* ===================================================== */
/* FINAL CARD */
/* ===================================================== */

.final-overlay{
    position:fixed;
    top:0;
    left:0;

    width:100%;
    height:100vh;

    background:rgba(0,0,0,0.92);

    display:none;

    justify-content:center;
    align-items:center;

    z-index:100;
}

.final-card{
    width:90%;
    max-width:500px;

    background:white;

    padding:40px;

    border-radius:30px;

    text-align:center;
}

.final-card img{
    width:130px;
    height:130px;

    object-fit:cover;

    border-radius:50%;

    margin-bottom:20px;
}

.final-card h1{
    color:#d11a5b;
    font-size:45px;
    margin-bottom:20px;
    font-family:'Dancing Script',cursive;
}

.final-card p{
    line-height:1.8;
    color:#333;
    margin-bottom:20px;
}

.creator{
    margin-top:20px;
    color:#d11a5b;
    font-weight:bold;
    font-size:15px;
}

/* ===================================================== */
/* MUSIC PLAYER */
/* ===================================================== */

audio{
    display:none;
}

</style>
</head>

<body>

<!-- AUDIO -->
<audio id="bgMusic" autoplay loop playsinline>
    <source src="__SONG_URL__" type="audio/mpeg">
</audio>

<!-- LOGIN SCREEN -->

<div class="screen-login" id="loginScreen">

    <div class="login-card">

        <h1>🌸 Birthday Vault 🌸</h1>

        <p>
        Enter the secret password and unlock your birthday surprise ❤️
        </p>

        <div class="input-group">
            <i class="fa-solid fa-lock"></i>

            <input type="password"
            id="passwordField"
            placeholder="Enter password">
        </div>

        <button class="login-btn"
        onclick="checkPassword()">

        Unlock Surprise 🎁

        </button>

        <p class="error-msg" id="errorMsg">
        Wrong password ❌
        </p>

    </div>

</div>

<!-- STAGE SCREEN -->

<div class="screen-stage" id="stageScreen">

    <div class="stage-backdrop">

        <div class="photo-box">

            <h2>🌹 Special Birthday 🌹</h2>

            <img src="__BEHIND_CURTAIN_URL__">

            <button class="next-btn"
            onclick="goToPuzzle()">

            Open Puzzle 🧩

            </button>

        </div>

    </div>

    <div class="curtain-overlay" id="curtainOverlay">

        <div class="curtain left"></div>

        <div class="curtain right"></div>

        <div class="curtain-text"
        onclick="openCurtains()">

        <h2>🎭 Click To Open Curtain 🎭</h2>

        </div>

    </div>

</div>

<!-- PUZZLE SCREEN -->

<div class="screen-puzzle" id="puzzleScreen">

    <div class="puzzle-box">

        <h2>Birthday Puzzle 🎁</h2>

        <div class="puzzle-grid" id="grid"></div>

        <br>

        <button class="login-btn"
        onclick="autoSolve()">

        Auto Solve ✨

        </button>

    </div>

</div>

<!-- FINAL SCREEN -->

<div class="final-overlay" id="finalOverlay">

    <div class="final-card">

        <img src="__FINAL_PROFILE_URL__">

        <h1>Happy Birthday ❤️</h1>

        <p>
        May your life always stay beautiful,
        peaceful and filled with happiness.
        Keep smiling always ✨
        </p>

        <div class="creator">
            Created By Sripada Rao H ❤️
        </div>

        <br>

        <button class="next-btn"
        onclick="location.reload()">

        Replay 🔄

        </button>

    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<script>

// =====================================================
// FORCE AUDIO AUTOPLAY
// =====================================================

const audio = document.getElementById("bgMusic");

window.onload = () => {

    const playPromise = audio.play();

    if(playPromise !== undefined){

        playPromise
        .then(() => {
            console.log("Audio playing");
        })
        .catch(() => {

            // MOBILE BROWSER BLOCK FIX
            document.body.addEventListener('click', () => {
                audio.play();
            }, { once:true });

        });

    }

};

// =====================================================
// PASSWORD
// =====================================================

const correctPassword = "taperecord";

function checkPassword(){

    const val = document.getElementById("passwordField").value;

    if(val.toLowerCase() === correctPassword){

        document.getElementById("loginScreen").style.display = "none";

        document.getElementById("stageScreen").style.display = "block";

    }
    else{
        document.getElementById("errorMsg").style.display = "block";
    }
}

// =====================================================
// CURTAINS
// =====================================================

function openCurtains(){

    document.getElementById("stageScreen")
    .classList.add("curtains-open");

}

// =====================================================
// GO TO PUZZLE
// =====================================================

function goToPuzzle(){

    document.getElementById("stageScreen").style.display = "none";

    document.getElementById("puzzleScreen").style.display = "flex";

    buildPuzzle();
}

// =====================================================
// PUZZLE
// =====================================================

let puzzleState = [2,0,1,5,3,4,8,6,7];

let selected = null;

function buildPuzzle(){

    const grid = document.getElementById("grid");

    grid.innerHTML = "";

    puzzleState.forEach((piece,index)=>{

        const tile = document.createElement("div");

        tile.className = "tile";

        const row = Math.floor(piece/3);
        const col = piece%3;

        tile.style.backgroundPosition =
        `-${col*110}px -${row*110}px`;

        tile.onclick = () => selectTile(index);

        grid.appendChild(tile);

    });

}

function selectTile(index){

    if(selected === null){

        selected = index;

    }else{

        [puzzleState[selected], puzzleState[index]] =
        [puzzleState[index], puzzleState[selected]];

        selected = null;

        buildPuzzle();

        checkWin();
    }
}

function autoSolve(){

    puzzleState = [0,1,2,3,4,5,6,7,8];

    buildPuzzle();

    checkWin();
}

function checkWin(){

    const solved =
    puzzleState.every((v,i)=>v===i);

    if(solved){

        confetti({
            particleCount:200,
            spread:100
        });

        document.getElementById("finalOverlay")
        .style.display = "flex";
    }
}

</script>

</body>
</html>
"""

# =========================================================================
# REPLACE URLS
# =========================================================================

final_html = html_code.replace(
    "__LOGIN_BG_URL__",
    LOGIN_BACKGROUND_IMAGE
).replace(
    "__BEHIND_CURTAIN_URL__",
    BEHIND_CURTAIN_IMAGE
).replace(
    "__PUZZLE_IMG_URL__",
    PUZZLE_IMAGE
).replace(
    "__FINAL_PROFILE_URL__",
    FINAL_PROFILE_IMAGE
).replace(
    "__SONG_URL__",
    SONG_URL
)

# =========================================================================
# RENDER
# =========================================================================

components.html(final_html, height=1000, scrolling=False)
```
