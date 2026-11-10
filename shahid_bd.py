import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="System Freeze Simulator",
    page_icon="📱",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #050505;
    color: white;
}
header, footer, #MainMenu {
    visibility: hidden;
}
h1 {
    text-align: center;
    color: #ff3030;
}
</style>
""", unsafe_allow_html=True)

st.title("📱 Phone Freeze Simulator")
st.caption("A harmless 30-second visual prank")

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #050505;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
}

.panel {
    padding: 25px 15px;
    border: 1px solid #333;
    border-radius: 18px;
    background: #111;
}

button {
    background: #e32636;
    color: white;
    padding: 15px 25px;
    border: none;
    border-radius: 10px;
    font-size: 17px;
    cursor: pointer;
}

#freezeScreen {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: #050505;
    color: white;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 20px;
}

.loader {
    width: 65px;
    height: 65px;
    border: 5px solid #333;
    border-top: 5px solid red;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.error {
    color: #ff3030;
    font-size: 22px;
    font-weight: bold;
    margin: 25px 0;
}

#timer {
    font-size: 48px;
    margin: 20px;
    font-weight: bold;
}

#exit {
    margin-top: 25px;
    background: #333;
}
</style>
</head>

<body>

<div class="panel" id="welcome">
    <h2>System Diagnostic</h2>
    <p>Run a visual device simulation?</p>
    <p>This is a harmless browser animation lasting 30 seconds.</p>
    <button onclick="startSimulation()">
        ALLOW DEMO
    </button>
</div>

<div id="freezeScreen">
    <div class="loader"></div>
    <div class="error">SYSTEM NOT RESPONDING</div>
    <p>Simulated device freeze...</p>
    <div id="timer">30</div>
    <p>Please wait while the demo completes.</p>
    <button id="exit" onclick="endSimulation()">
        EXIT PRANK
    </button>
</div>

<script>
let remaining = 30;
let interval;

function startSimulation() {
    remaining = 30;

    document.getElementById("welcome").style.display = "none";

    const screen = document.getElementById("freezeScreen");
    screen.style.display = "flex";

    document.getElementById("timer").innerText = remaining;

    interval = setInterval(() => {
        remaining--;

        document.getElementById("timer").innerText = remaining;

        if (remaining <= 0) {
            endSimulation();
        }
    }, 1000);
}

function endSimulation() {
    clearInterval(interval);

    document.getElementById("freezeScreen").style.display = "none";
    document.getElementById("welcome").style.display = "block";
}
</script>

</body>
</html>
""", height=600, scrolling=False)
