# features/about.py
import streamlit as st
from core.i18n import get_text

def render():
    st.title(get_text("about_title"))
    st.write(get_text("about_content"))