import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="For Someone Special ✨", page_icon="💖", layout="centered")

# Initialize session states to track user progression
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "curtain_opened" not in st.session_state:
    st.session_state.curtain_opened = False

# --- PHASE 1: ROMANTIC LOGIN PAGE WITH RETRO TAPE BACKGROUND ---
if not st.session_state.logged_in:
    # Custom CSS injecting an aesthetic retro tape recorder looping background
    st.markdown("""
        <style>
        .stApp {
            background: url("https://cdn.dribbble.com/users/2095460/screenshots/16843477/media/64b5952d4faef49e81b674e7ca3e7e9a.gif") no-repeat center center fixed;
            background-size: cover;
        }
        .login-box {
            background-color: rgba(255, 240, 245, 0.85); /* Soft pinkish transparent background */
            padding: 35px;
            border-radius: 20px;
            border: 2px solid #ff758c;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
            margin-top: 15%;
        }
        h1 { color: #ff4b72 !important; font-family: 'Georgia', serif; }
        p { color: #555555 !important; font-size: 16px; }
        </style>
    """, unsafe_allow_html=True)

    # Centered container for login fields
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.title("📼 A Secret Tape for You...")
    st.write("I recorded something special. Enter the password to play it:")
    
    password = st.text_input("Password", type="password", placeholder="Hint: taperecord", label_visibility="collapsed")
    login_btn = st.button("Press Play ▶️")
    
    if login_btn:
        if password == "taperecord":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ That's not the secret key, try again gorgeous!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PHASE 2: THE REVEAL & INTERACTIVE RED STAGE CURTAIN ---
elif st.session_state.logged_in and not st.session_state.curtain_opened:
    st.title("🎬 Your Birthday Special Screen...")
    st.write("A beautiful world is waiting behind this curtain. Click below to slide them open! 👇")

    # Embedded HTML/CSS/JS stage curtain execution
    curtain_html = """
    <style>
        .curtain-container {
            position: relative;
            width: 100%;
            height: 450px;
            overflow: hidden;
            background: url('https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=1000') no-repeat center; /* Fairy lights under curtain */
            background-size: cover;
            border-radius: 15px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        }
        .curtain-left, .curtain-right {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            background: url('https://i.giphy.com/media/v1.Y2lkPTZjMDliOTUyM2FmNGphYXowZjdvOHVwOHI1ajU2cm40Y2U3eG80N3Q0MGV0ZmtzMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hR5V1fYtBDMowv5OIu/giphy.gif') no-repeat;
            background-size: 200% 100%;
            transition: transform 2.5s ease-in-out;
            z-index: 2;
        }
        .curtain-left { left: 0; background-position: 0 0; }
        .curtain-right { right: 0; background-position: 100% 0; }
        
        /* Class triggered by javascript to smoothly pull curtains open */
        .curtain-container.open .curtain-left { transform: translateX(-100%); }
        .curtain-container.open .curtain-right { transform: translateX(100%); }

        .reveal-message {
            position: absolute;
            width: 100%;
            text-align: center;
            top: 45%;
            color: white;
            font-family: 'Georgia', sans-serif;
            font-size: 30px;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(255, 75, 114, 0.8);
            z-index: 1;
        }
    </style>

    <div class="curtain-container" id="curtainStage">
        <div class="curtain-left"></div>
        <div class="curtain-right"></div>
        <div class="reveal-message">🌹 For the Most Beautiful Girl... 🌹</div>
    </div>
    """
    
    components.html(curtain_html, height=460)
    
    if st.button("💝 Open the Curtains 💝", use_container_width=True):
        st.session_state.curtain_opened = True
        st.rerun()

# --- PHASE 3: BIRTHDAY REVEAL & ROMANTIC PUZZLE GAME ---
else:
    st.balloons()
    st.snow() # Adds a magical aesthetic floating effect
    
    st.title("👑 Happy Birthday, Beautiful! 🎉")
    st.markdown("""
    ### 🎂 Wishing you the happiest, brightest day ever!
    You mean the absolute world to me. To celebrate your special day, I have hidden a final birthday sweet note inside this mini-puzzle.
    
    **💖 Your Task:** Drag and rearrange the blocks into their right numbers ($1$ to $9$) to reveal the final message!
    """)

    # Interactive Drag-and-Drop Puzzle Widget styled in Rose Gold theme
    puzzle_html = """
    <div style="display: flex; flex-direction: column; align-items: center; background: #fff0f5; padding: 25px; border-radius: 20px; border: 3px dashed #ff758c; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        <div id="puzzle-board" style="display: grid; grid-template-columns: repeat(3, 100px); gap: 8px; margin-bottom: 15px;">
            <!-- Generated dynamically -->
        </div>
        <p id="win-status" style="color: #d11a5b; font-weight: bold; font-size: 20px; font-family: 'Georgia', serif; text-align: center;"></p>
    </div>

    <script>
        const targetOrder = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        let currentOrder = ["4", "1", "2", "7", "3", "5", "9", "6", "8"]; // Scrambled initial state
        const board = document.getElementById('puzzle-board');

        function renderPuzzle() {
            board.innerHTML = '';
            currentOrder.forEach((num, index) => {
                let block = document.createElement('div');
                block.innerText = "❤️ Piece " + num;
                block.style.width = "100px";
                block.style.height = "100px";
                block.style.background = "linear-gradient(135deg, #ff758c, #ff7eb3)";
                block.style.color = "white";
                block.style.display = "flex";
                block.style.alignItems = "center";
                block.style.justifyContent = "center";
                block.style.fontFamily = "sans-serif";
                block.style.fontSize = "14px";
                block.style.fontWeight = "bold";
                block.style.borderRadius = "12px";
                block.style.cursor = "grab";
                block.setAttribute('draggable', true);
                block.setAttribute('data-index', index);

                block.addEventListener('dragstart', handleDragStart);
                block.addEventListener('dragover', handleDragOver);
                block.addEventListener('drop', handleDrop);
                board.appendChild(block);
            });
        }

        let draggedIndex = null;
        function handleDragStart(e) { draggedIndex = this.getAttribute('data-index'); }
        function handleDragOver(e) { e.preventDefault(); }

        function handleDrop(e) {
            e.preventDefault();
            const targetIndex = this.getAttribute('data-index');
            let temp = currentOrder[draggedIndex];
            currentOrder[draggedIndex] = currentOrder[targetIndex];
            currentOrder[targetIndex] = temp;
            
            renderPuzzle();
            checkWinCondition();
        }

        function checkWinCondition() {
            if (JSON.stringify(currentOrder) === JSON.stringify(targetOrder)) {
                document.getElementById('win-status').innerHTML = "✨ You Solved It! ✨<br>💌 <i>'Happy Birthday! You make every day brighter just by being in it. May all your dreams come true today and forever!'</i> 🎁💝";
                board.style.border = "3px solid #d11a5b";
            }
        }
        renderPuzzle();
    </script>
    """
    components.html(puzzle_html, height=450)

    # Let her replay if she wants to
    st.write("---")
    if st.button("🔄 Play Again"):
        st.session_state.logged_in = False
        st.session_state.curtain_opened = False
        st.rerun()
