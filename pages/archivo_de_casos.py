# pages/2_🗃️_Archivo_de_Casos.py

import streamlit as st
import pandas as pd
from data import get_crime_data
import datetime
from supabase_client import get_planned_visits, add_visit
import folium

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(page_title="Archivo de Casos", page_icon="🗃️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- FUNCIONES DE CARGA DE DATOS ---
@st.cache_data
def load_data_as_dataframe():
    crime_list = get_crime_data()
    df = pd.DataFrame(crime_list)
    return df

# --- FUNCIÓN PARA MOSTRAR LA PÁGINA DE DETALLE DE UN CASO ---
def display_detail_page(caso):
    st.title(caso['nombre'])
    
    # Botón para volver al listado principal
    if st.button("⬅️ Volver al Archivo de Casos"):
        # Limpiamos los parámetros de la URL para volver al listado
        st.query_params.clear()
        st.rerun()

    st.markdown("---")
    
    # Crónica y foto principal
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(caso['foto_url_archivo'], use_container_width=True)
    with col2:
        st.subheader("La Crónica")
        st.write(caso['cronica_detallada'])

    st.markdown("---")
    st.subheader("Galería de Archivo")
    if caso['galeria_fotos_archivo']:
        # Mostramos hasta 5 fotos por fila
        cols = st.columns(5)
        for i, photo_url in enumerate(caso['galeria_fotos_archivo']):
            with cols[i % 5]:
                st.image(photo_url)
    else:
        st.info("No hay fotos de archivo adicionales para este caso.")
        
# --- FUNCIÓN PARA MOSTRAR EL LISTADO PRINCIPAL DE CASOS ---
def display_list_page():
    st.title("🗃️ Archivo de Casos")
    st.markdown("Explora en detalle los casos más notorios de la crónica negra catalana.")
    
    df_crimes = load_data_as_dataframe()
    planned_crimes_names = [visit['crime_name'] for visit in get_planned_visits()]

    st.sidebar.header("Filtros de Búsqueda")
    provincias = ["Todas"] + sorted(df_crimes['provincia'].unique().tolist())
    selected_provincia = st.sidebar.selectbox("Filtrar por provincia:", provincias)
    status_options = ["Todos"] + sorted(df_crimes['status'].unique().tolist())
    selected_status = st.sidebar.selectbox("Filtrar por estado:", status_options)

    filtered_df = df_crimes.copy()
    if selected_provincia != "Todas":
        filtered_df = filtered_df[filtered_df['provincia'] == selected_provincia]
    if selected_status != "Todos":
        filtered_df = filtered_df[filtered_df['status'] == selected_status]
    
    st.markdown("---")
    
    if not filtered_df.empty:
        st.success(f"Mostrando {len(filtered_df)} de {len(df_crimes)} casos.")
        for index, row in filtered_df.iterrows():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(row['foto_url_archivo'], use_container_width=True)
                with col2:
                    st.subheader(row['nombre'])
                    st.markdown(f"**📍 {row['ubicacion_principal']}** | **🗓️ {row['fecha_suceso']}** | **⚖️ {row['status']}**")
                    st.write(row['resumen_corto'])
                    
                    # Botón para ir a la página de detalle
                    if st.button("Ver Ficha Completa ➔", key=f"detail_{row['id']}"):
                        # Añadimos el ID del caso a la URL para cambiar de vista
                        st.query_params["caso_id"] = row['id']
                        st.rerun()

                    if row['nombre'] not in planned_crimes_names:
                        if st.button("➕ Añadir al Planificador", key=f"add_{row['id']}"):
                            add_visit(row['id'], row['nombre'], datetime.date.today())
                            st.success(f"'{row['nombre']}' añadido a vuestra ruta!")
                            st.rerun()
                    else:
                        st.info("Este caso ya está en el planificador.")
    else:
        st.warning("No se encontraron casos con los filtros seleccionados.")

# --- LÓGICA PRINCIPAL DEL "ROUTER" ---
# Leemos el ID del caso de la URL. Si no existe, es None.
case_id_from_url = st.query_params.get("caso_id")

if case_id_from_url:
    # Si hay un ID en la URL, buscamos el caso y mostramos la página de detalle
    df = load_data_as_dataframe()
    # Convertimos la columna 'id' a string para comparar con el parámetro de la URL
    df['id'] = df['id'].astype(str)
    caso_seleccionado = df[df['id'] == case_id_from_url]
    
    if not caso_seleccionado.empty:
        display_detail_page(caso_seleccionado.iloc[0])
    else:
        st.error("Caso no encontrado.")
        if st.button("Volver al Archivo"):
            st.query_params.clear()
            st.rerun()
else:
    # Si no hay ID en la URL, mostramos el listado principal de casos
    display_list_page()