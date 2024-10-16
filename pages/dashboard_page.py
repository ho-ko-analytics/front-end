# pages/dashboard_page.py
import streamlit as st

from pages.components.filters import filters

def dashboard_page():
    filters()
    #st.write(f'Bem vindo *{st.session_state["name"]}*')
    st.title('Página de dados gerais')