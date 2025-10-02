# features/dashboard_viewer.py
import streamlit as st
from core.i18n import get_text

def render():
    """Renders the Viewer Dashboard."""
    st.title(get_text("viewer_dashboard_title"))
    st.write(get_text("viewer_dashboard_welcome"))
    # يمكنك إضافة المحتوى الذي يمكن للمشاهدين الوصول إليه هنا