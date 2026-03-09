import streamlit as st
import googlemaps
import math

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="La Casa del Chilaquil", page_icon="🌶️")

# LLAVE DE GOOGLE
MI_LLAVE = "AIzaSyAQSfBp29rK_P9iVLmYb0o-IKLIfJY4a3k" 
gmaps = googlemaps.Client(key=MI_LLAVE)
ORIGEN = "E. Aguirre Benavides 1216, Topochico, Saltillo, Coah."

# --- ESTILO (NARANJA Y BOTÓN AMARILLO) ---
st.markdown(f"""
<style>
    .stApp {{
        background-color: #FF8C00 !important;
    }}
    h1, h2, h3, p, label {{
        color: black !important;
        text-align: center !important;
        font-family: 'Arial Black', sans-serif;
    }}
    /* Botón Amarillo */
    div.stButton > button {{
        background-color: #FFD700 !important;
        color: black !important;
        font-weight: bold !important;
        font-size: 20px !important;
        width: 100% !important;
        border: 2px solid black !important;
        border-radius: 10px;
        height: 55px;
    }}
    .res-box {{
        background-color: black;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# --- CONTENIDO ---

# MÉTODO DEFINITIVO PARA CENTRAR EL LOGO
# Creamos 3 columnas: la del medio (col2) es donde va el logo
vacia1, col_logo, vacia2 = st.columns([1, 2, 1])
with col_logo:
    logo_url = "https://scontent.fntr1-2.fna.fbcdn.net/v/t39.30808-6/541503739_122215258532142370_5934744794648823732_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=1d70fc&_nc_eui2=AeFWKG6akVesjlPmtEoKz5OcPkEyaHUEvmE-QTJodQS-YWZi_Z4_yK9_OkPntPPHRpUxkZQxoNS6e4QZiJ5KuHTW&_nc_ohc=kjm3a_ijRrgQ7kNvwFXWgyE&_nc_oc=Adk4qClZ88evhAu3YXHPYJNUSQhw0k0mmNkmslOWQb8AhLDOPQMIvPNBCWjkuN6AJrYiTEVksfhlbYY97nhpYTAQ&_nc_zt=23&_nc_ht=scontent.fntr1-2.fna&_nc_gid=NiPwkybC8KUukSBI-WF4mA&_nc_ss=8&oh=00_Afz2BU6YZVKoskP1mTQR51UMxZGKWufU5FLaQXAwONElaw&oe=69B52B79"
    st.image(logo_url, use_container_width=True)

st.markdown("<h2>LA CASA DEL CHILAQUIL</h2>", unsafe_allow_html=True)
st.markdown(f"<p><b>Origen:</b> {ORIGEN}</p>", unsafe_allow_html=True)

def obtener_costo(distancia):
    d = math.ceil(distancia)
    tarifas = {
        1: 25, 2: 25, 3: 29, 4: 38, 5: 48, 6: 58, 7: 67, 8: 77, 9: 86, 10: 96,
        11: 106, 12: 115, 13: 125, 14: 134, 15: 144, 16: 154, 17: 163, 18: 173, 19: 182, 20: 192,
        21: 202, 22: 211, 23: 221, 24: 230, 25: 240, 26: 250, 27: 259, 28: 269, 29: 278, 30: 288
    }
    return tarifas.get(d, 288 + ((d - 30) * 10))

st.markdown("<p style='text-align: left !important;'>Dirección del cliente:</p>", unsafe_allow_html=True)
direccion = st.text_input("Dirección", label_visibility="collapsed", placeholder="Calle, número y colonia")

# Centramos también el botón usando la misma técnica de columnas
v1, col_btn, v2 = st.columns([1, 2, 1])
with col_btn:
    if st.button("🚀 CALCULAR COSTO"):
        if direccion:
            try:
                res = gmaps.distance_matrix(ORIGEN, f"{direccion}, Saltillo", mode='driving')
                dist = res['rows'][0]['elements'][0]['distance']['value'] / 1000
                costo = obtener_costo(dist)
                
                st.markdown(f"""
                <div class="res-box">
                    <h2 style="color:white !important;">PRECIO: ${costo} MXN</h2>
                    <p style="color:#FFD700 !important;">Distancia: {dist:.2f} km</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            except:
                st.error("Dirección no encontrada.")
