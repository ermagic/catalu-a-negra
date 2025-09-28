import streamlit as st
import pandas as pd
from data import get_crime_data
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster # Importamos la herramienta de clustering

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
st.markdown("Explora el mapa. Los iconos se agrupan al alejar el zoom. Pulsa sobre cada pin para ver los detalles.")
st.markdown("---")

# --- CARGA Y LÓGICA DEL MAPA ---
df_crimes = load_data_as_dataframe()

if not df_crimes.empty:
    
    # 1. Crear el mapa base, centrado en Cataluña
    map_center = [41.8781, 1.7856]
    m = folium.Map(location=map_center, zoom_start=8, tiles="CartoDB positron")

    # 2. Crear un grupo de marcadores (cluster)
    marker_cluster = MarkerCluster().add_to(m)

    # 3. Añadir un pin por cada caso AL CLUSTER
    for index, row in df_crimes.iterrows():
        
        # Creamos el contenido HTML para la ventana emergente
        # Ahora incluye una imagen en miniatura
        popup_html = f"""
        <div style="width: 250px;">
            <h5 style="margin-bottom: 5px;">{row['nombre']}</h5>
            <img src="{row['foto_url_archivo']}" width="100%" style="border-radius: 5px;"/>
            <p style="font-size: 12px; margin-top: 10px;"><b>Ubicación:</b> {row['ubicacion_principal']}</p>
        </div>
        """
        
        # Creamos el marcador y lo añadimos al grupo
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=folium.Popup(popup_html),
            tooltip=row['nombre'],
            icon=folium.Icon(color='darkred', icon='-')
        ).add_to(marker_cluster)

    # 4. Mostrar el mapa en Streamlit
    st_folium(m, height=500, use_container_width=True, returned_objects=[])

else:
    st.error("No se pudieron cargar los datos de los crímenes para mostrar el mapa.")
