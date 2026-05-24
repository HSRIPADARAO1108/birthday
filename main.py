import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# Initialize session states to track user progression
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "curtain_opened" not in st.session_state:
    st.session_state.curtain_opened = False

# --- PHASE 1: LOGIN PAGE WITH TAPE RECORDER BACKGROUND ---
if not st.session_state.logged_in:
    # Custom CSS injecting an animated tape recorder background and styling the input container
    st.markdown("""
        <style>
        .stApp {
            background: url("https://cdn.dribbble.com/userupload/21316020/file/original-ca7841d288882c8280768de4da51ca3a.gif") no-repeat center center fixed;
            background-size: cover;
        }
        .login-box {
            background-color: rgba(0, 0, 0, 0.75);
            padding: 30px;
            border-radius: 15px;
            border: 2px solid #ff4b4b;
            text-align: center;
            color: white;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
            margin-top: 20%;
        }
        h1, p { color: white !important; }
        </style>
    """, unsafe_allow_html=True)

    # Centered container for login fields
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.title("📼 Retro Audio Vault")
    st.write("Enter the secret tape password to unlock your surprise.")
    
    password = st.text_input("Password", type="password", placeholder="Hint: taperecord", label_visibility="collapsed")
    login_btn = st.button("Play Tape ➔")
    
    if login_btn:
        if password == "taperecord":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Wrong frequency! Try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PHASE 2: THE REVEAL & INTERACTIVE STAGE CURTAIN ---
elif st.session_state.logged_in and not st.session_state.curtain_opened:
    st.title("🎬 A Special Performance Awaits...")
    st.write("Click the button below to pull back the curtains and view your surprise!")

    # Embedded HTML/CSS/JS stage curtain execution
    curtain_html = """
    <style>
        .curtain-container {
            position: relative;
            width: 100%;
            height: 450px;
            overflow: hidden;
            background: url('https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=1000') no-repeat center;
            background-size: cover;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        .curtain-left, .curtain-right {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            background: url('https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyNmVwNHEyNmgyYm12bGZjemswNmh2MWJyOTBtZ3BnY2RpcHQ5NXVnbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hR5V1fYtBDMowv5OIu/giphy.gif') no-repeat;
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
            top: 40%;
            color: white;
            font-family: 'Arial', sans-serif;
            font-size: 28px;
            font-weight: bold;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
            z-index: 1;
        }
    </style>

    <div class="curtain-container" id="curtainStage">
        <div class="curtain-left"></div>
        <div class="curtain-right"></div>
        <div class="reveal-message">✨ The Show is About to Begin! ✨</div>
    </div>

    <script>
        function openCurtain() {
            document.getElementById('curtainStage').classList.add('open');
        }
    </script>
    """
    
    components.html(curtain_html, height=460)
    
    # We use a standard Streamlit button to handle state transition cleanly
    if st.button("🎭 Pull Open Curtains", use_container_width=True):
        st.session_state.curtain_opened = True
        st.rerun()

# --- PHASE 3: BIRTHDAY MESSAGE & REVERSIBLE PICTURE PUZZLE ---
else:
    st.balloons()
    st.title("🎂 Happy Birthday! 🎉")
    st.subheader("Your final tape reward challenge: Solve the Birthday Puzzle")
    st.write("Drag and drop the scrambled grid elements into their correct numerical slots to reveal the secret image!")

    # Interactive Drag-and-Drop Puzzle Widget (HTML5 Canvas + JS)
    puzzle_html = """
    <div style="display: flex; flex-direction: column; align-items: center; background: #1e1e1e; padding: 20px; border-radius: 12px; border: 2px dashed #ff4b4b;">
        <div id="puzzle-board" style="display: grid; grid-template-columns: repeat(3, 100px); gap: 5px; margin-bottom: 15px;">
            <!-- Generated programmatically via JavaScript below -->
        </div>
        <p id="win-status" style="color: #4CAF50; font-weight: bold; font-size: 18px; font-family: sans-serif;"></p>
    </div>

    <script>
        const targetOrder = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        // Deliberately scrambled array state for the puzzle setup
        let currentOrder = ["3", "1", "2", "6", "4", "5", "9", "7", "8"]; 
        const board = document.getElementById('puzzle-board');

        function renderPuzzle() {
            board.innerHTML = '';
            currentOrder.forEach((num, index) => {
                let block = document.createElement('div');
                block.innerText = "🧩 Piece " + num;
                block.style.width = "100px";
                block.style.height = "100px";
                block.style.background = "linear-gradient(135deg, #ff4b4b, #ff7676)";
                block.style.color = "white";
                block.style.display = "flex";
                block.style.align-items = "center";
                block.style.justify-content = "center";
                block.style.fontFamily = "sans-serif";
                block.style.fontWeight = "bold";
                block.style.borderRadius = "8px";
                block.style.cursor = "grab";
                block.setAttribute('draggable', true);
                block.setAttribute('data-id', num);
                block.setAttribute('data-index', index);

                // HTML5 Drag and Drop Event listeners
                block.addEventListener('dragstart', handleDragStart);
                block.addEventListener('dragover', handleDragOver);
                block.addEventListener('drop', handleDrop);
                board.appendChild(block);
            });
        }

        let draggedIndex = null;

        function handleDragStart(e) {
            draggedIndex = this.getAttribute('data-index');
        }

        function handleDragOver(e) {
            e.preventDefault();
        }

        function handleDrop(e) {
            e.preventDefault();
            const targetIndex = this.getAttribute('data-index');
            // Swap array elements inside state
            let temp = currentOrder[draggedIndex];
            currentOrder[draggedIndex] = currentOrder[targetIndex];
            currentOrder[targetOrder.indexOf(targetIndex) !== -1 ? targetIndex : targetIndex] = temp;
            
            renderPuzzle();
            checkWinCondition();
        }

        function checkWinCondition() {
            if (JSON.stringify(currentOrder) === JSON.stringify(targetOrder)) {
                document.getElementById('win-status').innerText = "🎈 Magnificent! You've unlocked the Taperecord Birthday Box! 🎁";
                // Optionally swap backgrounds to show completed graphic asset
                board.style.border = "3px solid #4CAF50";
            }
        }

        renderPuzzle();
    </script>
    """
    components.html(puzzle_html, height=400)

    # Reset option to allow the birthday person to re-run the surprise webpage experience
    if st.button("🔄 Restart Experience"):
        st.session_state.logged_in = False
        st.session_state.curtain_opened = False
        st.rerun()
