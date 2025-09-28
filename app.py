import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Rutas de la Cataluña Negra",
    page_icon="🩸",
    layout="wide"
)

# --- FUNCIÓN DE LOGIN ---
def check_login():
    """Valida el usuario y la contraseña con los secretos."""
    correct_usernames = st.secrets["credentials"]["usernames"]
    correct_password = st.secrets["credentials"]["password"]
    
    if (st.session_state["username"] in correct_usernames and
        st.session_state["password"] == correct_password):
        st.session_state["logged_in"] = True
        del st.session_state["password"]
        del st.session_state["username"]
    else:
        st.session_state["logged_in"] = False
        st.error("❌ Usuario o contraseña incorrectos.")

# --- INICIALIZACIÓN DEL ESTADO DE LA SESIÓN ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- PANTALLA DE LOGIN ---
if not st.session_state["logged_in"]:
    st.title("Rutas de la Cataluña Negra 🩸")
    st.header("Acceso al Panel")
    st.text_input("Usuario", key="username")
    st.text_input("Contraseña", type="password", key="password")
    st.button("Entrar", on_click=check_login)

# --- APLICACIÓN PRINCIPAL ---
if st.session_state["logged_in"]:
    st.sidebar.success(f"Sesión iniciada.")
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["logged_in"] = False
        st.rerun()
        
    # --- PÁGINA DE BIENVENIDA ---
    st.title("Panel de Control - Rutas de la Cataluña Negra")
    st.markdown("### ¡Bienvenidas! Aquí empieza vuestro diario de viaje.")
    st.markdown("---")
    st.info(
        """
        Usa el menú de la izquierda para navegar por las diferentes secciones:
        - **🗃️ Archivo de Casos:** Explora todos los casos que hemos recopilado.
        - **🗺️ Mapa del Crimen:** Visualiza las ubicaciones en un mapa interactivo.
        - **🗓️ Planificador de Ruta:** Organiza vuestras próximas visitas.
        - **📸 Nuestra Galería:** Sube y comparte vuestras fotos.
        """
    )