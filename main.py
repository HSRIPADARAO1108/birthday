import streamlit as fancy_st
import urllib.parse

# Set up page styling and title
fancy_st.set_page_config(page_title="Interactive Birthday Wish 🎉", page_icon="🎂", layout="centered")

# Custom CSS to make it look festive and clean
fancy_st.markdown("""
    <style>
    .birthday-header {
        text-align: center;
        color: #ff4b4b;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .cake-emoji {
        font-size: 100px;
        text-align: center;
        display: block;
        margin: 20px auto;
    }
    .wishes-box {
        background-color: #fff0f0;
        padding: 30px;
        border-radius: 15px;
        border: 2px dashed #ff4b4b;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Check if URL parameters exist (meaning a friend opened a shared link)
query_params = fancy_st.query_params

if "name" in query_params:
    # --- RECIPIENT MODE ---
    # Extract data from the URL safely
    friend_name = query_params.get("name")
    friend_age = query_params.get("age", "")
    secret_message = query_params.get("msg", "Happy Birthday!")
    
    fancy_st.markdown(f"<h1 class='birthday-header'>For You, {friend_name}! ✨</h1>", unsafe_allow_html=True)
    
    # Session state tracking to check if candles are blown
    if "blown" not in fancy_st.session_state:
        fancy_st.session_state.blown = False

    if not fancy_st.session_state.blown:
        # Display cake with lit candle emoji
        fancy_st.markdown("<span class='cake-emoji'>🎂🎂🎂<br>🎂🕯️🎂</span>", unsafe_allow_html=True)
        fancy_st.write("")
        fancy_st.info(f"Hey {friend_name}! You have a secret birthday wish waiting for your {friend_age if friend_age else ''} birthday! Make a wish and blow out the candle below.")
        
        # Interactive action button to "blow" the candle
        if fancy_st.button("💨 Click to Blow Out the Candle! 💨", use_container_width=True):
            fancy_st.session_state.blown = True
            fancy_st.rerun()
            
    else:
        # Show celebration animations!
        fancy_st.balloons()
        fancy_st.snow() # Creates a magical confetti/sparkle overlay effect
        
        # Display cake with blown out candle
        fancy_st.markdown("<span class='cake-emoji'>🎂🎂🎂<br>🎂✨🎂</span>", unsafe_allow_html=True)
        
        # Reveal the secret message in a styled card container
        fancy_st.markdown(f"""
            <div class='wishes-box'>
                <h2 style='color: #ff4b4b; margin-bottom: 10px;'>🎉 HAPPY BIRTHDAY 🎉</h2>
                <p style='font-size: 24px; font-weight: bold; color: #333;'>{secret_message}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Option to create their own link
        if fancy_st.button("Create a wish for someone else 👈"):
            fancy_st.query_params.clear()
            fancy_st.session_state.blown = False
            fancy_st.rerun()

else:
    # --- CREATOR MODE ---
    fancy_st.markdown("<h1 class='birthday-header'>🎂 Birthday Wish Link Generator 🎁</h1>", unsafe_allow_html=True)
    fancy_st.write("Create a unique interactive experience for your friends. Fill out the details below to generate their card link!")
    
    with fancy_st.form("wish_generator"):
        name = fancy_st.text_input("Friend's Name", placeholder="e.g. Rahul")
        age = fancy_st.text_input("Age (Optional)", placeholder="e.g. 25")
        message = fancy_st.text_area("Your Secret Birthday Message", placeholder="Happy Birthday buddy! Hope you have an awesome year ahead!")
        
        submit_btn = fancy_st.form_submit_button("Generate Magical Link ✨")
        
    if submit_btn:
        if name and message:
            # Safely encode strings to be URL-friendly
            encoded_name = urllib.parse.quote(name)
            encoded_age = urllib.parse.quote(age)
            encoded_msg = urllib.parse.quote(message)
            
            # Construct base host URL dynamically or use a fallback local link structure
            base_url = "http://localhost:8501/" # Change this to your deployed Streamlit Cloud URL later!
            
            # Formulate the custom shareable link
            share_url = f"{base_url}?name={encoded_name}&age={encoded_age}&msg={encoded_msg}"
            
            fancy_st.success("🎉 Link successfully created! Copy it below and send it to your friend.")
            fancy_st.code(share_url, language="text")
            fancy_st.caption("Pro-tip: If you deploy this app on Streamlit Community Cloud, swap 'localhost:8501' with your public app web address!")
        else:
            fancy_st.error("Please fill out at least the Name and Secret Message fields to generate a link.")
