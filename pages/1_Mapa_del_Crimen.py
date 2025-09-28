# pages/1_🗺️_Mapa_del_Crimen.py

import streamlit as st
import pandas as pd
from data import get_crime_data
import folium  # La nueva librería de mapas
from streamlit_folium import st_folium # El componente para mostrar el mapa en Streamlit

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(
    page_title="Mapa del Crimen",
    page_icon="🗺️",
    layout="wide"
)

# Verificamos que el usuario haya iniciado sesión.
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- FUNCIÓN PARA CARGAR DATOS ---
@st.cache_data
def load_data_as_dataframe():
    crime_list = get_crime_data()
    df = pd.DataFrame(crime_list)
    df['lat'] = pd.to_numeric(df['lat'])
    df['lon'] = pd.to_numeric(df['lon'])
    return df

# --- TÍTULO DE LA PÁGINA ---
st.title("🗺️ Mapa del Crimen Interactivo")
st.markdown("Pulsa sobre cada pin para ver los detalles del caso. ¡Perfecto para explorar desde el móvil!")
st.markdown("---")

# --- CARGA Y LÓGICA DEL MAPA ---
df_crimes = load_data_as_dataframe()

if not df_crimes.empty:
    
    # 1. Crear el mapa base, centrado en Cataluña
    # Coordenadas aproximadas del centro de Cataluña
    map_center = [41.8781, 1.7856]
    m = folium.Map(location=map_center, zoom_start=8)

    # 2. Añadir un pin (marcador) por cada caso
    for index, row in df_crimes.iterrows():
        
        # Creamos el texto que aparecerá en la ventana emergente (popup)
        popup_html = f"""
        <h4>{row['nombre']}</h4>
        <p><b>Ubicación:</b> {row['ubicacion_principal']}</p>
        <p>{row['resumen_corto']}</p>
        """
        
        # Creamos el marcador y lo añadimos al mapa
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row['nombre'], # Texto que aparece al pasar el ratón por encima (en ordenador)
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

    # 3. Mostrar el mapa en Streamlit
    st_folium(m, height=450, use_container_width=True)

else:
    st.error("No se pudieron cargar los datos de los crímenes para mostrar el mapa.")