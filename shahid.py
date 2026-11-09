import streamlit as st
import time

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Level Up: Shahid's Birthday!",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# Custom Styling (Gaming & Cyber Theme)
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Dark Cyber Background */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neon Glow Title */
    .glowing-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        color: #58a6ff;
        text-shadow: 0 0 10px #58a6ff, 0 0 20px #1f6feb, 0 0 30px #1f6feb;
        margin-bottom: 5px;
    }
    
    .sub-glow {
        font-size: 1.2rem;
        text-align: center;
        color: #7ee787;
        margin-bottom: 25px;
    }
    
    /* Card Component */
    .stat-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    
    .stat-header {
        color: #ffa657;
        font-size: 1.1rem;
        font-weight: bold;
    }

    .stat-value {
        color: #ffffff;
        font-size: 1.4rem;
    }

    /* Custom Button */
    .stButton>button {
        background: linear-gradient(135deg, #238636, #2ea043);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 10px 24px;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(46, 160, 67, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "candles_blown" not in st.session_state:
    st.session_state.candles_blown = False

# ---------------------------------------------------------
# Header & Celebration Trigger
# ---------------------------------------------------------
st.markdown("<h1 class='glowing-title'>LEVEL UP: MD SHAHID</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-glow'>[ SYSTEM MSG: Player 1 has successfully aged up! ]</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Interactive Cake Section
# ---------------------------------------------------------
st.markdown("---")
st.subheader("🎂 The Virtual Birthday Cake")

col1, col2 = st.columns([1, 1])

with col1:
    if not st.session_state.candles_blown:
        st.markdown("""
        <div style="text-align: center; font-size: 5rem; line-height: 1.2;">
            🔥 🔥 🔥<br>
            🎂🎂🎂
        </div>
        """, unsafe_allow_html=True)
        st.info("The candles are lit! Make a wish and blow them out.")
    else:
        st.markdown("""
        <div style="text-align: center; font-size: 5rem; line-height: 1.2;">
            💨 💨 💨<br>
            🎂🎂🎂
        </div>
        """, unsafe_allow_html=True)
        st.success("Wish locked in! Next year's quest unlocked! 🎉")

with col2:
    st.write("")
    st.write("")
    if not st.session_state.candles_blown:
        if st.button("💨 Blow Out Candles!"):
            st.session_state.candles_blown = True
            st.balloons()
            st.snow()
            st.rerun()
    else:
        if st.button("🔄 Relight Candles"):
            st.session_state.candles_blown = False
            st.rerun()

# Trigger confetti automatically if candles are blown
if st.session_state.candles_blown:
    st.balloons()

# ---------------------------------------------------------
# Player Stats Dashboard
# ---------------------------------------------------------
st.markdown("---")
st.subheader("📊 Player Attributes & Stats")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class='stat-card'>
        <div class='stat-header'>🎮 Role / Class</div>
        <div class='stat-value'>Master Gamer & Brother</div>
    </div>
    <div class='stat-card'>
        <div class='stat-header'>⚡ Ping / Latency</div>
        <div class='stat-value'>0 ms (Ultra Speed)</div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class='stat-card'>
        <div class='stat-header'>🛡️ Special Ability</div>
        <div class='stat-value'>Leap of Faith / High Clutch</div>
    </div>
    <div class='stat-card'>
        <div class='stat-header'>🏆 Loyalty Rank</div>
        <div class='stat-value'>MAX Level (Unbreakable)</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Terminal Log & Developer Note
# ---------------------------------------------------------
st.markdown("---")
st.subheader("💻 Console Logs & Wish")

with st.expander("▶ Click to run brother_wishes.py", expanded=True):
    code_placeholder = st.empty()
    terminal_logs = [
        "> Initializing birthday protocol...",
        "> Loading brotherly appreciation modules...",
        "> Status: 100% Synced.",
        "> Executing message output:"
    ]
    
    log_text = ""
    for log in terminal_logs:
        log_text += log + "\n"
        code_placeholder.code(log_text, language="bash")
        time.sleep(0.3)

    st.markdown("""
    > **Happy Birthday, Shahid!** 🎂🎮
    > 
    > Having you as both a brother and a friend is an absolute cheat code in life. 
    > May this new year bring you zero bugs, maximum frame rates, infinite wins, 
    > and clear paths to every big goal you set out to achieve! 
    > 
    > *Believe in yourself and keep taking those leaps.* 🚀
    """)

# ---------------------------------------------------------
# Secret Unlockable / Gallery Section
# ---------------------------------------------------------
st.markdown("---")
st.subheader("🔓 Secret VIP Locker")

pin_code = st.text_input("Enter Secret PIN to unlock birthday surprise (Hint: Shahid's Month Number '11' or '9'):", type="password")

if pin_code in ["9", "11", "09"]:
    st.success("Access Granted! VIP Archives Unlocked.")
    st.markdown("""
    🎉 **You unlocked the Brotherhood Trophy!**  
    *Free Pass for 1x Free Meal / Gaming Session with zero refusals!*
    """)
    st.balloons()
elif pin_code != "":
    st.error("Access Denied: Incorrect Passcode. Try 9 or 11!")

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.markdown("<div style='text-align: center; color: #484f58;'>Engineered with ❤️ for Md Shahid • 9th November</div>", unsafe_allow_html=True)
