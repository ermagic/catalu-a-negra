# pages/2_🗃️_Archivo_de_Casos.py

import streamlit as st
import pandas as pd
from data import get_crime_data
import datetime
from supabase_client import get_planned_visits, add_visit

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(page_title="Archivo de Casos", page_icon="🗃️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- FUNCIÓN PARA CARGAR DATOS ---
@st.cache_data
def load_data_as_dataframe():
    crime_list = get_crime_data()
    df = pd.DataFrame(crime_list)
    return df

# --- TÍTULO DE LA PÁGINA ---
st.title("🗃️ Archivo de Casos")
st.markdown("Explora en detalle los casos más notorios de la crónica negra catalana.")

# --- LÓGICA DE LA PÁGINA ---
df_crimes = load_data_as_dataframe()
planned_crimes_names = [visit['crime_name'] for visit in get_planned_visits()]

# --- ¡NUEVO! FILTROS EN LA BARRA LATERAL ---
st.sidebar.header("Filtros de Búsqueda")

# Filtro por Provincia
provincias = ["Todas"] + sorted(df_crimes['provincia'].unique().tolist())
selected_provincia = st.sidebar.selectbox("Filtrar por provincia:", provincias)

# Filtro por Estado
status_options = ["Todos"] + sorted(df_crimes['status'].unique().tolist())
selected_status = st.sidebar.selectbox("Filtrar por estado:", status_options)

# Aplicamos los filtros al DataFrame
filtered_df = df_crimes.copy()
if selected_provincia != "Todas":
    filtered_df = filtered_df[filtered_df['provincia'] == selected_provincia]
if selected_status != "Todos":
    filtered_df = filtered_df[filtered_df['status'] == selected_status]

st.markdown("---")

# --- VISUALIZACIÓN DE CASOS FILTRADOS ---
if not filtered_df.empty:
    st.success(f"Mostrando {len(filtered_df)} de {len(df_crimes)} casos.")
    for index, row in filtered_df.iterrows():
        st.subheader(row['nombre'])
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(row['foto_url_archivo'], use_column_width=True)
        
        with col2:
            st.markdown(f"**📍 Ubicación:** {row['ubicacion_principal']}")
            st.markdown(f"**🗓️ Fecha:** {row['fecha_suceso']}")
            st.markdown(f"**⚖️ Estado:** {row['status']}")
            
            if row['nombre'] not in planned_crimes_names:
                if st.button("➕ Añadir al Planificador", key=f"add_{row['id']}"):
                    add_visit(row['id'], row['nombre'], datetime.date.today())
                    st.success(f"'{row['nombre']}' añadido a vuestra ruta!")
                    st.rerun()
            else:
                st.info("Este caso ya está en vuestro planificador.")

            with st.expander("Ver la crónica completa del caso"):
                st.write(row['cronica_detallada'])
        st.markdown("---")
else:
    st.warning("No se encontraron casos que coincidan con los filtros seleccionados.")