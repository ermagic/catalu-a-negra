# pages/3_🗓️_Planificador_de_Ruta.py

import streamlit as st
import datetime
# Importamos la nueva función
from supabase_client import get_planned_visits, update_visit_date, delete_visit, update_visit_rating, update_visit_status

# --- CONFIGURACIÓN Y VERIFICACIÓN DE LOGIN ---
st.set_page_config(page_title="Planificador de Ruta", page_icon="🗓️", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Debes iniciar sesión para acceder a esta página.")
    st.stop()

# --- TÍTULO DE LA PÁGINA ---
st.title("🗓️ Planificador de Ruta")
st.markdown("Organiza vuestras visitas, cambia su estado, asigna fechas y puntúa vuestra experiencia.")
st.markdown("---")

# --- LÓGICA DEL PLANIFICADOR ---
planned_visits = get_planned_visits()

if not planned_visits:
    st.info("Aún no habéis añadido ningún caso a vuestra ruta. Id al 'Archivo de Casos' para empezar.")
else:
    # Separamos las visitas en dos listas: planeadas y visitadas
    planeadas = [v for v in planned_visits if v.get('status', 'Planeado') == 'Planeado']
    visitadas = [v for v in planned_visits if v.get('status') == 'Visitado']

    # Mostramos primero las visitas planeadas
    st.header("Visitas Planeadas")
    if not planeadas:
        st.info("¡No hay nuevas rutas en el horizonte! Añade más casos desde el Archivo.")
    
    for visit in planeadas:
        with st.container(border=True): # Usamos un contenedor para crear el efecto "tarjeta"
            col_header, col_button_delete = st.columns([4, 1])
            with col_header:
                st.subheader(visit['crime_name'])
            with col_button_delete:
                if st.button("❌ Eliminar", key=f"del_{visit['id']}", use_container_width=True):
                    delete_visit(visit['id'])
                    st.rerun()

            col1, col2 = st.columns(2)
            with col1:
                # Selector de fecha
                current_date = datetime.datetime.strptime(visit['visit_date'], '%Y-%m-%d').date()
                new_date = st.date_input("Fecha:", value=current_date, key=f"date_{visit['id']}")
                if new_date != current_date:
                    update_visit_date(visit['id'], new_date)
                    st.rerun()
            
            with col2:
                # Selector de estado
                if st.button("✅ Marcar como Visitado", key=f"status_{visit['id']}", use_container_width=True):
                    update_visit_status(visit['id'], 'Visitado')
                    st.rerun()

    st.markdown("---")

    # Mostramos las visitas ya realizadas en un expander para no ocupar espacio
    st.header("Historial de Visitas")
    if not visitadas:
        st.info("Aún no habéis marcado ninguna visita como realizada.")
    
    for visit in visitadas:
         with st.expander(f"✅ {visit['crime_name']} (Visitado el {visit['visit_date']})"):
            # Slider para la puntuación (solo aparece para los visitados)
            current_rating = visit['rating'] if visit['rating'] is not None else 0
            new_rating = st.slider("Tu Puntuación (1-100):", 0, 100, value=current_rating, key=f"rating_{visit['id']}")
            if new_rating != current_rating:
                update_visit_rating(visit['id'], new_rating)

            # Opción para volver a planificar
            if st.button("↩️ Mover a 'Planeado'", key=f"replan_{visit['id']}"):
                update_visit_status(visit['id'], 'Planeado')
                st.rerun()