import streamlit as st
import googlemaps
import math
from streamlit_searchbox import st_searchbox

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="La Casa del Chilaquil", page_icon="🌶️")

# LLAVE DE GOOGLE
MI_LLAVE = "AIzaSyAQSfBp29rK_P9iVLmYb0o-IKLIfJY4a3k" 
gmaps = googlemaps.Client(key=MI_LLAVE)
ORIGEN = "E. Aguirre Benavides 1216, Topochico, Saltillo, Coah."

# --- ESTILO ---
st.markdown(f"""
<style>
    .stApp {{ background-color: #FF8C00 !important; }}
    [data-testid="stImage"] {{ display: flex; justify-content: center; margin-bottom: -20px; }}
    h2, p, label {{ color: black !important; text-align: center !important; font-family: 'Arial Black', sans-serif; }}
    .res-success {{
        background-color: #28a745 !important; color: white !important; padding: 40px 20px !important;
        border-radius: 20px; text-align: center; border: 4px solid white; margin-top: 15px;
    }}
</style>
""", unsafe_allow_html=True)

# LOGO
v1, col_logo, v2 = st.columns([2, 1, 2])
with col_logo:
    st.image("https://scontent.fntr1-2.fna.fbcdn.net/v/t39.30808-6/541503739_122215258532142370_5934744794648823732_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=1d70fc&_nc_eui2=AeFWKG6akVesjlPmtEoKz5OcPkEyaHUEvmE-QTJodQS-YWZi_Z4_yK9_OkPntPPHRpUxkZQxoNS6e4QZiJ5KuHTW&_nc_ohc=kjm3a_ijRrgQ7kNvwFXWgyE&_nc_oc=Adk4qClZ88evhAu3YXHPYJNUSQhw0k0mmNkmslOWQb8AhLDOPQMIvPNBCWjkuN6AJrYiTEVksfhlbYY97nhpYTAQ&_nc_zt=23&_nc_ht=scontent.fntr1-2.fna&_nc_gid=NiPwkybC8KUukSBI-WF4mA&_nc_ss=8&oh=00_Afz2BU6YZVKoskP1mTQR51UMxZGKWufU5FLaQXAwONElaw&oe=69B52B79", width=100)

st.markdown("<h2 style='font-size: 18px;'>LA CASA DEL CHILAQUIL</h2>", unsafe_allow_html=True)

# Función que busca en Google Maps mientras escribes
def buscar_en_google(searchterm: str):
    if not searchterm: return []
    res = gmaps.places_autocomplete(searchterm, location="25.4232,-100.9927", radius=10000, language="es")
    return [r["description"] for r in res]

st.markdown("<p style='font-size: 14px;'>📍 Busca el Edificio o Dirección:</p>", unsafe_allow_html=True)

# EL BUSCADOR INTELIGENTE
destino_seleccionado = st_searchbox(buscar_en_google, key="google_search")

def obtener_costo(distancia):
    d = math.ceil(distancia)
    tarifas = {1:25, 2:25, 3:29, 4:38, 5:48, 6:58, 7:67, 8:77, 9:86, 10:96, 11:106, 12:115, 13:125, 14:134, 15:144, 16:154, 17:163, 18:173, 19:182, 20:192, 21:202, 22:211, 23:221, 24:230, 25:240, 26:250, 27:259, 28:269, 29:278, 30:288}
    return tarifas.get(d, 288 + ((d - 30) * 10))

if destino_seleccionado:
    try:
        res = gmaps.distance_matrix(ORIGEN, destino_seleccionado, mode='driving')
        if res['rows'][0]['elements'][0]['status'] == 'OK':
            dist = res['rows'][0]['elements'][0]['distance']['value'] / 1000
            costo = obtener_costo(dist)
            st.markdown(f"""
            <div class="res-success">
                <p style="font-size: 35px; font-weight: 900;">PRECIO DE ENVÍO: ${costo} MXN</p>
                <p style="font-size: 20px;">🛣️ DISTANCIA: {dist:.2f} km</p>
            </div>
            """, unsafe_allow_html=True)
    except:
        st.error("Error al calcular. Intenta con otra dirección.")

