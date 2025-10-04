# features/strategy_management.py - النسخة المخفضة بعد التقسيم
import streamlit as st
from core.i18n import get_text
from users.auth_service import get_current_user

# استيراد الوحدات الجديدة
from features.strategy_crud import (
    initialize_strategy_session,
    reset_strategy_session
)
from features.strategy_operations import (
    apply_dialog_styles,
    get_strategy_builder_steps,
    get_current_step_progress
)
from features.strategy_ui import (
    render_strategy_list,
    render_step_vision,
    render_step_message,
    render_step_objectives,
    render_step_values,
    render_step_preview
)

def render():
    """وظيفة العرض الرئيسية - النسخة المخفضة"""
    st.title(get_text("strategy_management"))
    
    # تطبيق أنماط الـ Dialogs
    lang = st.session_state.get("lang", "ar")
    apply_dialog_styles(lang)
    
    # التحقق من تسجيل الدخول
    user = get_current_user()
    if not user:
        st.error(get_text("must_be_logged_in"))
        return
    
    username = user["username"]
    
    # تهيئة جلسة الاستراتيجية
    initialize_strategy_session()
    
    # التوجيه بناءً على الخطوة الحالية
    if st.session_state.strategy_builder_step == 0:
        render_strategy_list(username)
    else:
        render_strategy_builder(username)

def render_strategy_builder(username):
    """عرض منشئ الاستراتيجية"""
    # شريط التقدم
    steps = get_strategy_builder_steps()
    step = st.session_state.strategy_builder_step - 1
    progress_value, progress_text = get_current_step_progress(
        st.session_state.strategy_builder_step, 
        len(steps)
    )
    
    st.progress(progress_value, text=progress_text)
    
    # أزرار التنقل بين الخطوات
    cols = st.columns(6)
    for i, label in enumerate(steps):
        disabled = (i < step - 1 or i > step + 1) and i != step
        if cols[i].button(label, disabled=disabled, use_container_width=True):
            st.session_state.strategy_builder_step = i + 1
            st.rerun()
    
    st.markdown("---")
    
    # الحصول على البيانات الحالية
    data = st.session_state.current_strategy_data
    
    # عرض الخطوة المناسبة
    if st.session_state.strategy_builder_step == 1:
        render_step_vision(username, data)
    
    elif st.session_state.strategy_builder_step == 2:
        render_step_message(username, data)
    
    elif st.session_state.strategy_builder_step == 3:
        render_step_objectives(username, data)
    
    elif st.session_state.strategy_builder_step == 4:
        render_step_values(username, data)
    
    elif st.session_state.strategy_builder_step == 5:
        render_step_preview(username, data)
    
    # زر العودة للقائمة الرئيسية
    st.markdown("---")
    if st.button("← " + get_text("back_to_strategy_list"), use_container_width=True):
        reset_strategy_session()
        st.rerun()