import streamlit as st
import streamlit.components.v1 as components
import json
import time

# ---------------------------------------------------------
# Page Configuration & Metadata
# ---------------------------------------------------------
st.set_page_config(
    page_title="HAPPY BIRTHDAY MD SHAHID ðŸŽ® LEVEL UP!",
    page_icon="ðŸŽ‚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling (Cyberpunk / Gamer Dark Theme)
# ---------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Press+Start+2P&family=Rajdhani:wght@500;700&display=swap');

    /* Global Theme Overrides */
    .stApp {
        background-color: #08090f;
        background-image: 
            radial-gradient(circle at 15% 20%, rgba(0, 243, 255, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 85% 80%, rgba(255, 0, 127, 0.08) 0%, transparent 40%),
            linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
        color: #e0e6ed;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Neon Title Banner */
    .cyber-banner {
        text-align: center;
        padding: 25px 20px;
        background: rgba(13, 17, 23, 0.85);
        border: 2px solid #00f3ff;
        border-radius: 16px;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.3), inset 0 0 15px rgba(0, 243, 255, 0.15);
        margin-bottom: 25px;
        backdrop-filter: blur(8px);
        position: relative;
        overflow: hidden;
    }

    .cyber-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: 3px;
        color: #ffffff;
        text-shadow: 
            0 0 7px #fff,
            0 0 10px #00f3ff,
            0 0 21px #00f3ff,
            0 0 42px #00f3ff,
            0 0 82px #ff007f;
        margin: 0;
    }

    .cyber-subtitle {
        font-family: 'Press Start 2P', cursive;
        font-size: 1rem;
        color: #ff007f;
        text-shadow: 0 0 8px rgba(255, 0, 127, 0.8);
        margin-top: 15px;
    }

    /* Section Cards */
    .cyber-card {
        background: rgba(16, 22, 34, 0.8);
        border: 1px solid #1f293d;
        border-left: 4px solid #00f3ff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }

    /* Gamer Leaderboard & Quest Log Styling */
    .quest-box {
        background: #0d111a;
        border: 1px dashed #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }

    /* Custom Streamlit Buttons Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #00f3ff 0%, #0066ff 100%);
        color: #000000 !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 1.1rem;
        border: none;
        border-radius: 10px;
        padding: 14px 20px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 0 30px rgba(0, 243, 255, 0.8), 0 0 15px rgba(255, 0, 127, 0.6);
        color: #ffffff !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid #1f293d;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "candles_lit" not in st.session_state:
    st.session_state.candles_lit = False

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = [
        {"player": "Faizan", "score": 99990, "wish": "Happy Birthday Shahid! Keep grinding and crushing every level! ðŸŽ®ðŸ”¥"},
        {"player": "Tabish", "score": 98500, "wish": "Wishing you an epic year ahead filled with health, wins, and zero lag! ðŸš€"},
        {"player": "Dilshad", "score": 97000, "wish": "Happy Birthday brother! Leveling up in life with top stats! ðŸ’ªðŸ†"}
    ]

# ---------------------------------------------------------
# Sidebar Controls & Stats
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='font-family: Orbitron; color: #00f3ff;'>ðŸŽ® PLAYER CONFIG</h2>", unsafe_allow_html=True)
    
    age = st.number_input("Select Player Level (Age)", min_value=1, max_value=100, value=20, step=1)
    
    st.markdown("---")
    st.markdown("<h3 style='font-family: Orbitron; color: #ff007f;'>âš¡ PLAYER ATTRIBUTES</h3>", unsafe_allow_html=True)
    st.write("**Name:** Md Shahid")
    st.write("**Class:** Elite Gamer & Brother")
    st.write("**Latency:** 0 ms (Ultra Speed)")
    st.write("**Special Skill:** Instant Clutch & High IQ")
    st.write("**Status:** ðŸ† MAXIMUM HYPER-DRIVE")
    
    st.markdown("---")
    st.markdown("<h3 style='font-family: Orbitron; color: #7ee787;'>ðŸ•¹ï¸ QUICK CONTROLS</h3>", unsafe_allow_html=True)
    
    if st.button("ðŸ”¥ Toggle Candle Flames"):
        st.session_state.candles_lit = not st.session_state.candles_lit
        st.rerun()
        
    if st.button("ðŸŽˆ Launch Confetti & Balloons"):
        st.balloons()
        st.snow()

# ---------------------------------------------------------
# Header Banner
# ---------------------------------------------------------
st.markdown(f"""
    <div class="cyber-banner">
        <div class="cyber-title">HAPPY BIRTHDAY MD SHAHID</div>
        <div class="cyber-subtitle">ðŸ† LEVEL {age} UNLOCKED! ðŸ†</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Interactive 3D Three.js Canvas Component
# ---------------------------------------------------------
def render_3d_cake_canvas(is_lit):
    lit_flag = "true" if is_lit else "false"
    
    threejs_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                overflow: hidden;
                background-color: transparent;
                font-family: 'Courier New', monospace;
            }}
            #canvas-container {{
                width: 100vw;
                height: 500px;
                position: relative;
            }}
            #controls-overlay {{
                position: absolute;
                bottom: 15px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 15px;
                z-index: 10;
            }}
            .cyber-btn {{
                background: linear-gradient(135deg, #00f3ff, #ff007f);
                color: #000;
                font-weight: bold;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 0 0 15px rgba(0,243,255,0.5);
                font-size: 14px;
                text-transform: uppercase;
                transition: all 0.2s ease;
            }}
            .cyber-btn:hover {{
                transform: scale(1.05);
                box-shadow: 0 0 25px rgba(255,0,127,0.8);
                color: #fff;
            }}
        </style>
        <!-- Three.js CDN -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="canvas-container">
            <div id="controls-overlay">
                <button class="cyber-btn" onclick="toggleLighting()">ðŸ”¥ { "Extinguish Flames" if is_lit else "Light Up Candles" }</button>
                <button class="cyber-btn" onclick="triggerPartyEffect()">ðŸŽ† Cyber Blast</button>
            </div>
        </div>

        <script>
            let scene, camera, renderer, flames = [], floatingObjects = [], particles;
            let candlesLit = {lit_flag};

            function init() {{
                const container = document.getElementById('canvas-container');
                scene = new THREE.Scene();
                
                camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
                camera.position.set(0, 4, 9);
                camera.lookAt(0, 1.2, 0);

                renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(container.clientWidth, container.clientHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                renderer.shadowMap.enabled = true;
                container.appendChild(renderer.domElement);

                // Lighting Setup
                const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
                scene.add(ambientLight);

                const cyanDirLight = new THREE.DirectionalLight(0x00f3ff, 1.2);
                cyanDirLight.position.set(5, 8, 5);
                scene.add(cyanDirLight);

                const magentaDirLight = new THREE.DirectionalLight(0xff007f, 1.0);
                magentaDirLight.position.set(-5, 5, -5);
                scene.add(magentaDirLight);

                // Build 3D Gaming Cake
                createGamerCake();

                // Build Floating Items
                createFloatingElements();

                // Build Background Particle System
                createParticleSystem();

                // Event Listeners
                window.addEventListener('resize', onWindowResize);
                animate();
            }}

            function createGamerCake() {{
                const cakeGroup = new THREE.Group();

                // Cake Base Platform (Pedestal)
                const pedGeo = new THREE.CylinderGeometry(2.8, 3.2, 0.3, 32);
                const pedMat = new THREE.MeshStandardMaterial({{ color: 0x111827, roughness: 0.2, metalness: 0.8 }});
                const pedestal = new THREE.Mesh(pedGeo, pedMat);
                pedestal.position.y = -0.15;
                cakeGroup.add(pedestal);

                // Tier 1 (Bottom Layer - Dark Cyber Base)
                const t1Geo = new THREE.CylinderGeometry(2.3, 2.3, 1.0, 32);
                const t1Mat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.3 }});
                const tier1 = new THREE.Mesh(t1Geo, t1Mat);
                tier1.position.y = 0.5;
                cakeGroup.add(tier1);

                // Neon Trim Tier 1
                const trim1Geo = new THREE.TorusGeometry(2.32, 0.04, 16, 100);
                const trim1Mat = new THREE.MeshBasicMaterial({{ color: 0x00f3ff }});
                const trim1 = new THREE.Mesh(trim1Geo, trim1Mat);
                trim1.rotation.x = Math.PI / 2;
                trim1.position.y = 0.5;
                cakeGroup.add(trim1);

                // Tier 2 (Middle Layer - Magenta/Purple accent)
                const t2Geo = new THREE.CylinderGeometry(1.6, 1.6, 0.8, 32);
                const t2Mat = new THREE.MeshStandardMaterial({{ color: 0x1e1b4b, roughness: 0.3 }});
                const tier2 = new THREE.Mesh(t2Geo, t2Mat);
                tier2.position.y = 1.4;
                cakeGroup.add(tier2);

                // Neon Trim Tier 2
                const trim2Geo = new THREE.TorusGeometry(1.62, 0.04, 16, 100);
                const trim2Mat = new THREE.MeshBasicMaterial({{ color: 0xff007f }});
                const trim2 = new THREE.Mesh(trim2Geo, trim2Mat);
                trim2.rotation.x = Math.PI / 2;
                trim2.position.y = 1.4;
                cakeGroup.add(trim2);

                // Top Tier 3 (Cyan Layer)
                const t3Geo = new THREE.CylinderGeometry(1.0, 1.0, 0.6, 32);
                const t3Mat = new THREE.MeshStandardMaterial({{ color: 0x0284c7, roughness: 0.2 }});
                const tier3 = new THREE.Mesh(t3Geo, t3Mat);
                tier3.position.y = 2.1;
                cakeGroup.add(tier3);

                // Add 3D Candles & Flames
                const candlePositions = [
                    {{ x: 0, z: 0 }},
                    {{ x: 0.4, z: 0.4 }},
                    {{ x: -0.4, z: 0.4 }},
                    {{ x: 0.4, z: -0.4 }},
                    {{ x: -0.4, z: -0.4 }}
                ];

                candlePositions.forEach(pos => {{
                    // Candle stick
                    const cGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.4, 16);
                    const cMat = new THREE.MeshStandardMaterial({{ color: 0xffffff, emissive: 0x00f3ff, emissiveIntensity: 0.3 }});
                    const candle = new THREE.Mesh(cGeo, cMat);
                    candle.position.set(pos.x, 2.6, pos.z);
                    cakeGroup.add(candle);

                    // Flame
                    const fGeo = new THREE.ConeGeometry(0.07, 0.2, 16);
                    const fMat = new THREE.MeshBasicMaterial({{ color: 0xffaa00 }});
                    const flame = new THREE.Mesh(fGeo, fMat);
                    flame.position.set(pos.x, 2.9, pos.z);
                    flame.visible = candlesLit;
                    cakeGroup.add(flame);
                    flames.push(flame);

                    // Flame Point Light
                    const pLight = new THREE.PointLight(0xffaa00, candlesLit ? 1.5 : 0, 2);
                    pLight.position.set(pos.x, 2.95, pos.z);
                    cakeGroup.add(pLight);
                    flame.userData.light = pLight;
                }});

                scene.add(cakeGroup);
            }}

            function createFloatingElements() {{
                const geometries = [
                    new THREE.BoxGeometry(0.3, 0.3, 0.3),
                    new THREE.OctahedronGeometry(0.25),
                    new THREE.TetrahedronGeometry(0.25)
                ];

                const materials = [
                    new THREE.MeshStandardMaterial({{ color: 0x00f3ff, wireframe: true }}),
                    new THREE.MeshStandardMaterial({{ color: 0xff007f, wireframe: true }}),
                    new THREE.MeshStandardMaterial({{ color: 0x7ee787, wireframe: true }})
                ];

                for (let i = 0; i < 15; i++) {{
                    const geo = geometries[Math.floor(Math.random() * geometries.length)];
                    const mat = materials[Math.floor(Math.random() * materials.length)];
                    const mesh = new THREE.Mesh(geo, mat);

                    mesh.position.set(
                        (Math.random() - 0.5) * 10,
                        Math.random() * 5 + 0.5,
                        (Math.random() - 0.5) * 8
                    );
                    
                    mesh.userData = {{
                        rotSpeedX: (Math.random() - 0.5) * 0.03,
                        rotSpeedY: (Math.random() - 0.5) * 0.03,
                        floatSpeed: Math.random() * 0.015 + 0.005,
                        initialY: mesh.position.y
                    }};

                    floatingObjects.push(mesh);
                    scene.add(mesh);
                }}
            }}

            function createParticleSystem() {{
                const pGeo = new THREE.BufferGeometry();
                const count = 300;
                const positions = new Float32Array(count * 3);

                for (let i = 0; i < count * 3; i++) {{
                    positions[i] = (Math.random() - 0.5) * 18;
                }}

                pGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                const pMat = new THREE.PointsMaterial({{
                    size: 0.05,
                    color: 0x00f3ff,
                    transparent: true,
                    opacity: 0.6
                }});

                particles = new THREE.Points(pGeo, pMat);
                scene.add(particles);
            }}

            function toggleLighting() {{
                candlesLit = !candlesLit;
                flames.forEach(flame => {{
                    flame.visible = candlesLit;
                    if (flame.userData.light) {{
                        flame.userData.light.intensity = candlesLit ? 1.5 : 0;
                    }}
                }});
            }}

            function triggerPartyEffect() {{
                particles.material.color.setHex(Math.random() > 0.5 ? 0xff007f : 0x7ee787);
                floatingObjects.forEach(obj => {{
                    obj.position.y += 0.8;
                }});
            }}

            function onWindowResize() {{
                const container = document.getElementById('canvas-container');
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }}

            function animate() {{
                requestAnimationFrame(animate);

                // Rotate Scene slightly for orbit look
                scene.rotation.y += 0.004;

                // Animate Flames
                if (candlesLit) {{
                    flames.forEach(flame => {{
                        flame.scale.x = 0.9 + Math.sin(Date.now() * 0.01) * 0.2;
                        flame.scale.z = 0.9 + Math.cos(Date.now() * 0.015) * 0.2;
                    }});
                }}

                // Animate Floating Objects
                floatingObjects.forEach(obj => {{
                    obj.rotation.x += obj.userData.rotSpeedX;
                    obj.rotation.y += obj.userData.rotSpeedY;
                    obj.position.y = obj.userData.initialY + Math.sin(Date.now() * obj.userData.floatSpeed) * 0.3;
                }});

                renderer.render(scene, camera);
            }}

            window.onload = init;
        </script>
    </body>
    </html>
    """
    components.html(threejs_code, height=520)

# Render 3D Scene
st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: Orbitron; color: #00f3ff; margin-bottom: 0;'>ðŸŽ‚ 3D INTERACTIVE GAMING CAKE & ARENA</h3>", unsafe_allow_html=True)
render_3d_cake_canvas(st.session_state.candles_lit)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Interactive Buttons & Actions Section
# ---------------------------------------------------------
st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: Orbitron; color: #ff007f;'>âš¡ CELEBRATION BOOSTERS</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    btn_text = "ðŸ”¥ Extinguish Candle Flames" if st.session_state.candles_lit else "ðŸ”¥ Light Up Candles"
    if st.button(btn_text, key="main_candle_btn"):
        st.session_state.candles_lit = not st.session_state.candles_lit
        st.rerun()

with col2:
    if st.button("ðŸŽ‰ Launch Balloons & Cyber Confetti", key="main_confetti_btn"):
        st.balloons()
        st.snow()
        st.toast("ðŸš€ ACHIEVEMENT UNLOCKED: Party Mode Activated!", icon="ðŸ†")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Leaderboard & Custom Birthday Wishes
# ---------------------------------------------------------
st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: Orbitron; color: #7ee787;'>ðŸ† HALL OF FAME: BIRTHDAY LEADERBOARD</h3>", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("#### ðŸ“ Submit Your Wish & Score")
    with st.form(key="wish_form"):
        player_name = st.text_input("Gamer Tag / Your Name", placeholder="e.g. PixelKnight")
        player_score = st.number_input("High Score Contribution", min_value=100, max_value=999999, value=95000, step=500)
        custom_wish = st.text_area("Birthday Message / Quest Log", placeholder="Write your birthday wish for Md Shahid...")
        submit_btn = st.form_submit_button("ðŸš€ Submit to Leaderboard")

        if submit_btn:
            if player_name.strip() != "" and custom_wish.strip() != "":
                st.session_state.leaderboard.append({
                    "player": player_name,
                    "score": player_score,
                    "wish": custom_wish
                })
                # Sort by score descending
                st.session_state.leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x["score"], reverse=True)
                st.success("ðŸŽ¯ Score & Wish Posted to Leaderboard!")
                st.balloons()
                st.rerun()
            else:
                st.error("Please provide both a Gamer Tag and a Wish!")

with col_right:
    st.markdown("#### ðŸ¥‡ Current Top High Scores & Wishes")
    for idx, entry in enumerate(st.session_state.leaderboard):
        rank_icon = "ðŸ¥‡" if idx == 0 else ("ðŸ¥ˆ" if idx == 1 else ("ðŸ¥‰" if idx == 2 else "ðŸŽ®"))
        st.markdown(f"""
            <div class="quest-box">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-family: Orbitron; font-weight: bold; color: #00f3ff;">
                        {rank_icon} Rank #{idx+1}: {entry['player']}
                    </span>
                    <span style="font-family: 'Press Start 2P', cursive; font-size: 0.8rem; color: #ff007f;">
                        {entry['score']:,} PTS
                    </span>
                </div>
                <div style="margin-top: 8px; font-style: italic; color: #c9d1d9;">
                    "{entry['wish']}"
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #484f58; font-family: 'Orbitron', sans-serif; font-size: 0.9rem;">
        Engineered with â¤ï¸ for Md Shahid â€¢ Level Up Edition â€¢ Powered by Streamlit & Three.js
    </div>
""", unsafe_allow_html=True)