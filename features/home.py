# features/home.py
import streamlit as st
from core.i18n import get_text

def render():
    """Renders the Home page."""
    st.title(get_text("home_page_title"))
    st.write(get_text("home_page_welcome"))
    # يمكنك إضافة محتوى الصفحة الرئيسية هنا، مثل المقالات أو الأخبار أو أي شيء آخر