# pages/3_🗓️_Planificador_de_Ruta.py

import streamlit as st
import datetime
# Importamos la nueva función
from supabase_client import get_planned_visits, update_visit_date, delete_visit, update_visit_rating

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(page_title="Planificador de Ruta", page_icon="🗓️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- TÍTULO DE LA PÁGINA ---
st.title("🗓️ Planificador de Ruta")
st.markdown("Organiza vuestras visitas, asigna fechas y puntúa vuestra experiencia.")
st.markdown("---")

# --- LÓGICA DEL PLANIFICADOR ---
planned_visits = get_planned_visits()

if not planned_visits:
    st.info("Aún no habéis añadido ningún caso a vuestra ruta.")
else:
    st.success("¡Esta es vuestra próxima ruta! Los cambios se guardan automáticamente.")
    
    for visit in planned_visits:
        st.subheader(visit['crime_name'])
        
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            # Selector de fecha
            current_date = datetime.datetime.strptime(visit['visit_date'], '%Y-%m-%d').date()
            new_date = st.date_input("Fecha:", value=current_date, key=f"date_{visit['id']}")
            if new_date != current_date:
                update_visit_date(visit['id'], new_date)
                st.rerun()
        
        with col2:
            # --- ¡NUEVO! Slider para la puntuación ---
            current_rating = visit['rating'] if visit['rating'] is not None else 0
            new_rating = st.slider("Puntuación (1-100):", 0, 100, value=current_rating, key=f"rating_{visit['id']}")
            if new_rating != current_rating:
                update_visit_rating(visit['id'], new_rating)
                # No hacemos rerun aquí para que la experiencia sea más fluida
        
        with col3:
            st.write("")
            st.write("")
            if st.button("Eliminar", key=f"del_{visit['id']}"):
                delete_visit(visit['id'])
                st.rerun()
        
        st.markdown("---")