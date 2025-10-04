# features/strategy_dialogs.py
import streamlit as st
from core.i18n import get_text
from data.strategy_elements import get_all_visions, get_messages_for_vision

@st.dialog(get_text("select_vision"))
def vision_selector_dialog(username, current_data):
    """Dialog لاختيار الرؤية من القائمة"""
    visions = get_all_visions(username)
    if not visions:
        st.warning(get_text("no_visions_available"))
        return

    selected_vision = st.selectbox(
        get_text("select_vision_from_list"),
        options=visions,
        key="dialog_vision_select"
    )
    
    if st.button(get_text("confirm_selection")):
        current_data["selected_vision"] = selected_vision
        current_data["edited_vision"] = selected_vision
        st.session_state.vision_text_area = selected_vision
        st.rerun()

@st.dialog(get_text("select_message"))
def message_selector_dialog(username, current_data):
    """Dialog لاختيار الرسالة من القائمة"""
    original_vision = current_data.get("selected_vision")
    if not original_vision:
        st.error(get_text("please_select_vision_first"))
        return

    messages = get_messages_for_vision(original_vision, username)
    if not messages:
        st.warning(get_text("no_messages_available"))
        return

    selected_message = st.selectbox(
        get_text("select_message_from_list"),
        options=messages,
        key="dialog_message_select"
    )
    
    if st.button(get_text("confirm_selection")):
        current_data["selected_message"] = selected_message
        current_data["edited_message"] = selected_message
        st.session_state.message_text_area = selected_message
        st.rerun()