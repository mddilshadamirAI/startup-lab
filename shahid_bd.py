import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Device Freeze Simulator",
    page_icon="📱",
    layout="wide"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #050505;
    font-family: Arial, sans-serif;
    color: white;
    overflow: hidden;
}

#start {
    height: 90vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

button {
    padding: 16px 30px;
    background: #d90020;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 17px;
    cursor: pointer;
}

#screen {
    display: none;
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    background: #000;
    z-index: 99999;
    overflow: hidden;
}

#glitch {
    position: absolute;
    inset: 0;
    background:
        repeating-linear-gradient(
            transparent 0px,
            rgba(255,255,255,.04) 2px,
            transparent 4px
        );
    animation: scan 0.12s infinite;
}

#message {
    position: absolute;
    top: 40%;
    width: 100%;
    text-align: center;
    padding: 20px;
    animation: flicker .15s infinite;
}

#message h1 {
    color: red;
    font-size: clamp(25px, 7vw, 42px);
    text-shadow: 3px 0 red, -3px 0 blue;
}

#message p {
    color: #aaa;
}

#noise {
    position: absolute;
    inset: 0;
    pointer-events: none;
    opacity: .18;
    background: repeating-linear-gradient(
        0deg,
        transparent 0px,
        rgba(255,0,0,.2) 1px,
        transparent 3px
    );
}

#exit {
    position: absolute;
    bottom: 25px;
    left: 50%;
    transform: translateX(-50%);
    background: #222;
    border: 1px solid #777;
    font-size: 13px;
    padding: 10px 20px;
    z-index: 10;
}

#recovery {
    display: none;
    position: fixed;
    inset: 0;
    background: #050505;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    z-index: 100000;
}

@keyframes flicker {
    0% { opacity: 1; transform: translateX(0); }
    25% { opacity: .7; transform: translateX(3px); }
    50% { opacity: .9; transform: translateX(-3px); }
    75% { opacity: .5; transform: translateX(2px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes scan {
    0% { transform: translateY(-5px); }
    100% { transform: translateY(5px); }
}

.glitching {
    animation: flicker .12s infinite;
}
</style>
</head>

<body>

<div id="start">
    <h1>DEVICE DIAGNOSTICS</h1>
    <p>Run a 20-second visual freeze simulation?</p>
    <button onclick="startFreeze()">ALLOW DEMO</button>
</div>

<div id="screen">
    <div id="glitch"></div>
    <div id="noise"></div>

    <div id="message">
        <h1>DEVICE NOT RESPONDING</h1>
        <p>System interface temporarily unavailable</p>
        <p>Simulated hardware communication error</p>
        <p>Attempting automatic recovery...</p>
    </div>

    <button id="exit" onclick="recover()">
        EXIT SIMULATION
    </button>
</div>

<div id="recovery">
    <h1 style="color:#00df80">SYSTEM RECOVERED</h1>
    <p>Your device simulation has ended.</p>
    <button onclick="location.reload()">FINISH</button>
</div>

<script>
let freezeTimer;

function startFreeze() {
    document.getElementById("start").style.display = "none";
    document.getElementById("screen").style.display = "block";

    document.getElementById("message").classList.add("glitching");

    // Automatic recovery after 20 seconds
    freezeTimer = setTimeout(recover, 20000);
}

function recover() {
    clearTimeout(freezeTimer);

    document.getElementById("screen").style.display = "none";
    document.getElementById("recovery").style.display = "flex";
}
</script>

</body>
</html>
""", height=750, scrolling=False)
