# supabase_client.py

import streamlit as st
from supabase import create_client, Client
import uuid

# --- INICIALIZACIÓN ---
@st.cache_resource
def init_supabase_connection() -> Client:
    supabase_url = st.secrets["supabase"]["url"]
    supabase_key = st.secrets["supabase"]["key"]
    return create_client(supabase_url, supabase_key)

supabase = init_supabase_connection()
BUCKET_NAME = "fotos_visitas"

# --- FUNCIONES PARA VISITAS PLANIFICADAS ---

def get_planned_visits():
    try:
        response = supabase.table('planned_visits').select('*').order('visit_date', desc=False).execute()
        return response.data
    except Exception as e:
        st.error(f"Error al obtener las visitas: {e}")
        return []

def add_visit(crime_id, crime_name, visit_date):
    try:
        supabase.table('planned_visits').insert({'crime_id': crime_id, 'crime_name': crime_name, 'visit_date': visit_date.isoformat()}).execute()
    except Exception as e:
        st.error(f"Error al añadir la visita: {e}")

def update_visit_date(visit_id, new_date):
    try:
        supabase.table('planned_visits').update({'visit_date': new_date.isoformat()}).eq('id', visit_id).execute()
    except Exception as e:
        st.error(f"Error al actualizar la fecha: {e}")

def update_visit_rating(visit_id, new_rating):
    try:
        supabase.table('planned_visits').update({'rating': new_rating}).eq('id', visit_id).execute()
    except Exception as e:
        st.error(f"Error al actualizar la puntuación: {e}")

# --- ¡NUEVA FUNCIÓN! ---
def update_visit_status(visit_id, new_status):
    """
    Actualiza el estado de una visita ('Planeado' o 'Visitado').
    """
    try:
        supabase.table('planned_visits').update({'status': new_status}).eq('id', visit_id).execute()
    except Exception as e:
        st.error(f"Error al actualizar el estado: {e}")

def delete_visit(visit_id):
    try:
        supabase.table('planned_visits').delete().eq('id', visit_id).execute()
    except Exception as e:
        st.error(f"Error al eliminar la visita: {e}")

# --- FUNCIONES PARA LA GALERÍA DE FOTOS ---

def upload_photo(file):
    try:
        file_extension = file.name.split('.')[-1]
        file_path = f"public/{uuid.uuid4()}.{file_extension}"
        supabase.storage.from_(BUCKET_NAME).upload(file_path, file.getvalue(), {"content-type": file.type})
        public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)
        return public_url
    except Exception as e:
        st.error(f"Error al subir la foto: {e}")
        return None

def add_photo_record(crime_name, photo_url, caption):
    try:
        supabase.table('user_photos').insert({'crime_name': crime_name, 'photo_url': photo_url, 'caption': caption}).execute()
    except Exception as e:
        st.error(f"Error al guardar el registro de la foto: {e}")

def get_photos():
    try:
        response = supabase.table('user_photos').select('*').order('created_at', desc=True).execute()
        return response.data
    except Exception as e:
        st.error(f"Error al obtener las fotos: {e}")
        return []