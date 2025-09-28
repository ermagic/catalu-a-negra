# pages/4_📸_Nuestra_Galería.py

import streamlit as st
from supabase_client import get_planned_visits, upload_photo, add_photo_record, get_photos

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(page_title="Nuestra Galería", page_icon="📸", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- TÍTULO DE LA PÁGINA ---
st.title("📸 Nuestra Galería")
st.markdown("Sube aquí las fotos de vuestras visitas para crear vuestro diario de viaje.")
st.markdown("---")

# --- SECCIÓN PARA SUBIR FOTOS ---
st.header("Añadir una nueva foto")

planned_visits = get_planned_visits()
if not planned_visits:
    st.warning("Primero debéis añadir casos al 'Planificador de Ruta' para poder subir fotos.")
else:
    planned_crime_names = [visit['crime_name'] for visit in planned_visits]
    
    selected_crime = st.selectbox("1. ¿A qué caso pertenece esta foto?", planned_crime_names)
    caption = st.text_input("2. Escribe un pie de foto (opcional)")
    uploaded_file = st.file_uploader("3. Selecciona el archivo de imagen", type=["jpg", "jpeg", "png"])

    if st.button("Subir Foto", disabled=(not uploaded_file or not selected_crime)):
        with st.spinner("Subiendo foto... ¡esto puede tardar un poco!"):
            photo_url = upload_photo(uploaded_file)
            
            if photo_url:
                add_photo_record(selected_crime, photo_url, caption)
                st.success("¡Foto subida y guardada con éxito!")
                st.rerun()
            else:
                st.error("No se pudo subir la foto. Inténtalo de nuevo.")

# --- SECCIÓN PARA MOSTRAR LA GALERÍA ---
st.markdown("---")
st.header("Vuestro Álbum de Crímenes")

all_photos = get_photos()

if not all_photos:
    st.info("La galería está vacía. ¡Subid vuestra primera foto!")
else:
    photos_by_crime = {}
    for photo in all_photos:
        crime_name = photo['crime_name']
        if crime_name not in photos_by_crime:
            photos_by_crime[crime_name] = []
        photos_by_crime[crime_name].append(photo)
    
    for crime_name, photos in photos_by_crime.items():
        with st.expander(f"Caso: {crime_name} ({len(photos)} fotos)"):
            cols = st.columns(3)
            for i, photo in enumerate(photos):
                with cols[i % 3]:
                    # --- ARREGLO AQUÍ ---
                    st.image(photo['photo_url'], caption=photo['caption'] or "", use_container_width=True)