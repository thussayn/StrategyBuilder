# features/dashboard_admin.py
import streamlit as st
from core.i18n import get_text

def render():
    """Renders the Admin Dashboard."""
    st.title(get_text("admin_dashboard_title"))
    st.write(get_text("admin_dashboard_welcome"))
    # Admin-related functionalities (user management, settings, etc.) can be added here.