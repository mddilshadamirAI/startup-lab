import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# Page Config & Gamer Dark Theme CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Md Shahid | Level Up Birthday 🎮",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;900&family=Rajdhani:wght@600;700&display=swap');

    .stApp {
        background-color: #08090f;
        background-image: 
            radial-gradient(circle at 50% 30%, rgba(0, 243, 255, 0.12) 0%, transparent 60%),
            radial-gradient(circle at 80% 80%, rgba(255, 0, 127, 0.1) 0%, transparent 50%),
            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px;
        color: #e0e6ed;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Cyber Neon Header Banner */
    .banner {
        text-align: center;
        padding: 20px;
        background: rgba(13, 17, 23, 0.9);
        border: 2px solid #00f3ff;
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.3), inset 0 0 15px rgba(0, 243, 255, 0.15);
        margin-bottom: 25px;
    }

    .title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.3rem;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 10px #00f3ff, 0 0 25px #00f3ff, 0 0 40px #ff007f;
        margin: 0;
    }

    .subtitle {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.1rem;
        color: #ff007f;
        text-shadow: 0 0 8px rgba(255, 0, 127, 0.8);
        margin-top: 10px;
        letter-spacing: 2px;
    }

    /* Wish Card */
    .wish-card {
        background: rgba(16, 22, 34, 0.85);
        border-left: 4px solid #00f3ff;
        border-right: 4px solid #ff007f;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        margin-top: 15px;
        font-size: 1.25rem;
        line-height: 1.7;
    }

    /* Streamlit Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #00f3ff 0%, #ff007f 100%);
        color: #000000 !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 1rem;
        border: none;
        border-radius: 10px;
        padding: 12px 15px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.8), 0 0 15px rgba(255, 0, 127, 0.8);
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# State Management
# ---------------------------------------------------------
if "candles_lit" not in st.session_state:
    st.session_state.candles_lit = False

# ---------------------------------------------------------
# Header Banner
# ---------------------------------------------------------
st.markdown("""
    <div class="banner">
        <div class="title">🎮 HAPPY BIRTHDAY MD SHAHID 🎮</div>
        <div class="subtitle">🏆 LEVEL UP: NEW AGE UNLOCKED 🏆</div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Shahid's Photo & 3D Cake Section (Side-by-Side or Stacked)
# ---------------------------------------------------------
col_img, col_cake = st.columns([1, 1.3])

with col_img:
    st.markdown("<h4 style='font-family: Orbitron; color: #00f3ff; text-align: center;'>👤 PLAYER 1 PROFILE</h4>", unsafe_allow_html=True)
    try:
        # Replace 'shahid.jpg' with your actual image filename/path
        st.image("shahid.jpg", caption="Md Shahid • Elite Gamer & Brother", use_container_width=True)
    except Exception:
        st.info("💡 Tip: Place 'shahid.jpg' in the same folder as app.py to display his photo here!")

with col_cake:
    st.markdown("<h4 style='font-family: Orbitron; color: #ff007f; text-align: center;'>🎂 3D BIRTHDAY CAKE</h4>", unsafe_allow_html=True)
    
    # 3D Interactive Three.js Cake Component
    def render_3d_cake(is_lit):
        lit_flag = "true" if is_lit else "false"
        
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ margin: 0; overflow: hidden; background: transparent; }}
                #canvas-container {{ width: 100%; height: 320px; position: relative; }}
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        </head>
        <body>
            <div id="canvas-container"></div>
            <script>
                let scene, camera, renderer, flames = [], floatingItems = [];
                let candlesLit = {lit_flag};

                function init() {{
                    const container = document.getElementById('canvas-container');
                    scene = new THREE.Scene();

                    camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
                    camera.position.set(0, 3.8, 8);
                    camera.lookAt(0, 1.1, 0);

                    renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                    renderer.setSize(container.clientWidth, container.clientHeight);
                    renderer.setPixelRatio(window.devicePixelRatio);
                    container.appendChild(renderer.domElement);

                    // Lighting
                    scene.add(new THREE.AmbientLight(0xffffff, 0.7));
                    
                    const light1 = new THREE.DirectionalLight(0x00f3ff, 1.2);
                    light1.position.set(5, 8, 5);
                    scene.add(light1);

                    const light2 = new THREE.DirectionalLight(0xff007f, 1.0);
                    light2.position.set(-5, 5, -5);
                    scene.add(light2);

                    // Build 3D Cake
                    const cakeGroup = new THREE.Group();

                    // Base Pedestal
                    const ped = new THREE.Mesh(
                        new THREE.CylinderGeometry(2.5, 2.8, 0.2, 32),
                        new THREE.MeshStandardMaterial({{ color: 0x111827, metalness: 0.8, roughness: 0.2 }})
                    );
                    ped.position.y = -0.1;
                    cakeGroup.add(ped);

                    // Tier 1 (Dark Base)
                    const t1 = new THREE.Mesh(
                        new THREE.CylinderGeometry(2.0, 2.0, 0.8, 32),
                        new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.3 }})
                    );
                    t1.position.y = 0.4;
                    cakeGroup.add(t1);

                    // Neon Ring 1
                    const ring1 = new THREE.Mesh(
                        new THREE.TorusGeometry(2.02, 0.04, 16, 100),
                        new THREE.MeshBasicMaterial({{ color: 0x00f3ff }})
                    );
                    ring1.rotation.x = Math.PI / 2;
                    ring1.position.y = 0.4;
                    cakeGroup.add(ring1);

                    // Tier 2 (Magenta Base)
                    const t2 = new THREE.Mesh(
                        new THREE.CylinderGeometry(1.3, 1.3, 0.7, 32),
                        new THREE.MeshStandardMaterial({{ color: 0x1e1b4b, roughness: 0.3 }})
                    );
                    t2.position.y = 1.15;
                    cakeGroup.add(t2);

                    // Neon Ring 2
                    const ring2 = new THREE.Mesh(
                        new THREE.TorusGeometry(1.32, 0.04, 16, 100),
                        new THREE.MeshBasicMaterial({{ color: 0xff007f }})
                    );
                    ring2.rotation.x = Math.PI / 2;
                    ring2.position.y = 1.15;
                    cakeGroup.add(ring2);

                    // 3D Candles & Flames
                    const positions = [
                        {{x: 0, z: 0}}, {{x: 0.35, z: 0.35}}, 
                        {{x: -0.35, z: 0.35}}, {{x: 0.35, z: -0.35}}, 
                        {{x: -0.35, z: -0.35}}
                    ];

                    positions.forEach(pos => {{
                        const stick = new THREE.Mesh(
                            new THREE.CylinderGeometry(0.04, 0.04, 0.35, 16),
                            new THREE.MeshStandardMaterial({{ color: 0xffffff, emissive: 0x00f3ff, emissiveIntensity: 0.4 }})
                        );
                        stick.position.set(pos.x, 1.65, pos.z);
                        cakeGroup.add(stick);

                        const flame = new THREE.Mesh(
                            new THREE.ConeGeometry(0.06, 0.18, 16),
                            new THREE.MeshBasicMaterial({{ color: 0xffaa00 }})
                        );
                        flame.position.set(pos.x, 1.9, pos.z);
                        flame.visible = candlesLit;
                        cakeGroup.add(flame);
                        flames.push(flame);
                    }});

                    scene.add(cakeGroup);

                    // Floating 3D Geometric Objects
                    const geos = [new THREE.BoxGeometry(0.25, 0.25, 0.25), new THREE.OctahedronGeometry(0.2)];
                    const mats = [
                        new THREE.MeshStandardMaterial({{ color: 0x00f3ff, wireframe: true }}),
                        new THREE.MeshStandardMaterial({{ color: 0xff007f, wireframe: true }})
                    ];

                    for(let i = 0; i < 10; i++) {{
                        const mesh = new THREE.Mesh(geos[i % 2], mats[i % 2]);
                        mesh.position.set((Math.random() - 0.5) * 8, Math.random() * 3.5 + 0.5, (Math.random() - 0.5) * 5);
                        mesh.userData = {{ speedY: Math.random() * 0.01 + 0.005, rotX: Math.random() * 0.02, initialY: mesh.position.y }};
                        floatingItems.push(mesh);
                        scene.add(mesh);
                    }}

                    animate();
                }}

                function animate() {{
                    requestAnimationFrame(animate);
                    scene.rotation.y += 0.005;

                    if(candlesLit) {{
                        flames.forEach(f => {{
                            f.scale.x = 0.85 + Math.sin(Date.now() * 0.012) * 0.25;
                            f.scale.z = 0.85 + Math.cos(Date.now() * 0.015) * 0.25;
                        }});
                    }}

                    floatingItems.forEach(item => {{
                        item.rotation.x += item.userData.rotX;
                        item.rotation.y += 0.01;
                        item.position.y = item.userData.initialY + Math.sin(Date.now() * item.userData.speedY) * 0.25;
                    }});

                    renderer.render(scene, camera);
                }}

                window.onload = init;
            </script>
        </body>
        </html>
        """
        components.html(html_code, height=330)

    render_3d_cake(st.session_state.candles_lit)

# ---------------------------------------------------------
# 3 Gamer Action Buttons
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    flame_label = "🔥 Extinguish Flames" if st.session_state.candles_lit else "🔥 Light Up Candles"
    if st.button(flame_label):
        st.session_state.candles_lit = not st.session_state.candles_lit
        st.rerun()

with col2:
    if st.button("🎉 Blast Confetti"):
        st.balloons()

with col3:
    if st.button("❄️ Snow Party"):
        st.snow()

# ---------------------------------------------------------
# Clean Dedicated Wish Card
# ---------------------------------------------------------
st.markdown("""
    <div class="wish-card">
        <h3 style="color: #00f3ff; font-family: 'Orbitron', sans-serif; margin-top:0;">
            💬 MESSAGE FOR PLAYER 1: MD SHAHID
        </h3>
        <p style="color: #e0e6ed;">
            <b>Happy Birthday, Shahid! 🎂🎮</b>
        </p>
        <p style="color: #c9d1d9;">
            Having you as both a brother and a friend is an absolute cheat code in life! 
            May this new level bring you zero lag, max frame rates, infinite clutch moments, 
            and total victory in every single challenge you take on.
        </p>
        <p style="color: #ff007f; font-weight: bold; margin-bottom: 0;">
            🚀 Keep taking the leap and leveling up!
        </p>
    </div>
""", unsafe_allow_html=True)
