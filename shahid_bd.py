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
# 3D Interactive Three.js Cake & Revolving Photo Fragments
# ---------------------------------------------------------
def render_3d_arena(is_lit):
    lit_flag = "true" if is_lit else "false"
    
    # Using a standard string template with .format() to avoid f-string curly brace conflicts
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; background: transparent; }}
            #canvas-container {{ width: 100%; height: 420px; position: relative; }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="canvas-container"></div>
        <script>
            let scene, camera, renderer, flames = [], photoFragments = [];
            let candlesLit = {LitFlag};

            function init() {{
                const container = document.getElementById('canvas-container');
                scene = new THREE.Scene();

                camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
                camera.position.set(0, 4, 9);
                camera.lookAt(0, 1.2, 0);

                renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(container.clientWidth, container.clientHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                container.appendChild(renderer.domElement);

                // Lighting Setup
                scene.add(new THREE.AmbientLight(0xffffff, 0.7));
                
                const light1 = new THREE.DirectionalLight(0x00f3ff, 1.2);
                light1.position.set(5, 8, 5);
                scene.add(light1);

                const light2 = new THREE.DirectionalLight(0xff007f, 1.0);
                light2.position.set(-5, 5, -5);
                scene.add(light2);

                // Build 3D Cake
                const cakeGroup = new THREE.Group();

                const ped = new THREE.Mesh(
                    new THREE.CylinderGeometry(2.5, 2.8, 0.2, 32),
                    new THREE.MeshStandardMaterial({{ color: 0x111827, metalness: 0.8, roughness: 0.2 }})
                );
                ped.position.y = -0.1;
                cakeGroup.add(ped);

                const t1 = new THREE.Mesh(
                    new THREE.CylinderGeometry(2.0, 2.0, 0.8, 32),
                    new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.3 }})
                );
                t1.position.y = 0.4;
                cakeGroup.add(t1);

                const ring1 = new THREE.Mesh(
                    new THREE.TorusGeometry(2.02, 0.04, 16, 100),
                    new THREE.MeshBasicMaterial({{ color: 0x00f3ff }})
                );
                ring1.rotation.x = Math.PI / 2;
                ring1.position.y = 0.4;
                cakeGroup.add(ring1);

                const t2 = new THREE.Mesh(
                    new THREE.CylinderGeometry(1.3, 1.3, 0.7, 32),
                    new THREE.MeshStandardMaterial({{ color: 0x1e1b4b, roughness: 0.3 }})
                );
                t2.position.y = 1.15;
                cakeGroup.add(t2);

                const ring2 = new THREE.Mesh(
                    new THREE.TorusGeometry(1.32, 0.04, 16, 100),
                    new THREE.MeshBasicMaterial({{ color: 0xff007f }})
                );
                ring2.rotation.x = Math.PI / 2;
                ring2.position.y = 1.15;
                cakeGroup.add(ring2);

                // Candles & Flames
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

                // Load Texture & Create Revolving Photo Fragments (15 Fragments Orbiting)
                const textureLoader = new THREE.TextureLoader();
                textureLoader.load('shahid.jpg', (texture) => {{
                    createOrbits(texture);
                }}, undefined, (err) => {{
                    createOrbits(null);
                }});

                animate();
            }}

            function createOrbits(texture) {{
                const fragmentCount = 15;
                for (let i = 0; i < fragmentCount; i++) {{
                    const matOpts = texture ? {{ map: texture, side: THREE.DoubleSide }} : {{ color: i % 2 === 0 ? 0x00f3ff : 0xff007f, wireframe: true }};
                    const geo = new THREE.PlaneGeometry(0.5, 0.6);
                    const mat = new THREE.MeshStandardMaterial(matOpts);
                    const mesh = new THREE.Mesh(geo, mat);

                    const angle = (i / fragmentCount) * Math.PI * 2;
                    const radius = 3.2 + Math.random() * 0.8;
                    
                    mesh.userData = {{
                        angle: angle,
                        radius: radius,
                        speed: 0.01 + Math.random() * 0.015,
                        bobSpeed: 0.02 + Math.random() * 0.03,
                        initialY: 1.2 + Math.random() * 1.5
                    }};

                    photoFragments.push(mesh);
                    scene.add(mesh);
                }}
            }}

            function animate() {{
                requestAnimationFrame(animate);

                photoFragments.forEach(frag => {{
                    frag.userData.angle += frag.userData.speed;
                    frag.position.x = Math.cos(frag.userData.angle) * frag.userData.radius;
                    frag.position.z = Math.sin(frag.userData.angle) * frag.userData.radius;
                    frag.position.y = frag.userData.initialY + Math.sin(Date.now() * 0.003 * frag.userData.bobSpeed) * 0.4;
                    frag.rotation.y = -frag.userData.angle + Math.PI / 2;
                }});

                if (candlesLit) {{
                    flames.forEach(f => {{
                        f.scale.x = 0.85 + Math.sin(Date.now() * 0.012) * 0.25;
                        f.scale.z = 0.85 + Math.cos(Date.now() * 0.015) * 0.25;
                    }});
                }}

                renderer.render(scene, camera);
            }}

            window.onload = init;
        </script>
    </body>
    </html>
    """
    
    html_code = html_template.format(LitFlag=lit_flag)
    components.html(html_code, height=430)

# Render 3D Cake & Revolving Photos Arena
render_3d_arena(st.session_state.candles_lit)

# ---------------------------------------------------------
# 3 Gamer Action Buttons
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    flame_label = "🔥 Extinguish Flames" if st.session_state.candles_lit else "🔥 Light Up Candles"
    if st.button(flame_label):
        st.session_state.candles_lit = not st.session_state.candles_lit
        if st.session_state.candles_lit:
            st.balloons()
        st.rerun()

with col2:
    if st.button("🎉 Blast Confetti"):
        st.balloons()

with col3:
    if st.button("❄️ Snow Party"):
        st.snow()

# ---------------------------------------------------------
# Clean Dedicated Wish Card with Photo Thumbnail
# ---------------------------------------------------------
col_wish_img, col_wish_txt = st.columns([1, 2.2])

with col_wish_img:
    try:
        st.image("shahid.jpg", use_container_width=True)
    except Exception:
        st.info("💡 Place 'shahid.jpg' in your folder to display his portrait here!")

with col_wish_txt:
    st.markdown("""
        <div class="wish-card" style="margin-top: 0;">
            <h3 style="color: #00f3ff; font-family: 'Orbitron', sans-serif; margin-top:0;">
                💬 MESSAGE FOR MD SHAHID
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
