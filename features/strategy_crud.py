# features/strategy_crud.py
import streamlit as st
from core.i18n import get_text
from data.models import (
    create_strategy,
    get_user_strategies,
    get_strategy_by_id,
    update_strategy,
    delete_strategy,
    save_custom_element
)

def create_new_strategy(username, strategy_data):
    """إنشاء استراتيجية جديدة"""
    try:
        strategy_id = create_strategy(
            username=username,
            name=strategy_data["name"],
            description=strategy_data["description"],
            vision=strategy_data.get("edited_vision", strategy_data["vision"]),
            message=strategy_data.get("edited_message", strategy_data["message"]),
            objectives=strategy_data["objectives"],
            values=strategy_data["values"],
            logo_path=strategy_data.get("logo_path")
        )
        return strategy_id, True
    except Exception as e:
        st.error(f"خطأ في إنشاء الاستراتيجية: {str(e)}")
        return None, False

def update_existing_strategy(strategy_id, username, strategy_data):
    """تحديث استراتيجية موجودة"""
    try:
        success = update_strategy(
            strategy_id=strategy_id,
            username=username,
            name=strategy_data["name"],
            description=strategy_data["description"],
            vision=strategy_data.get("edited_vision", strategy_data["vision"]),
            message=strategy_data.get("edited_message", strategy_data["message"]),
            objectives=strategy_data["objectives"],
            values=strategy_data["values"],
            logo_path=strategy_data.get("logo_path")
        )
        return success
    except Exception as e:
        st.error(f"خطأ في تحديث الاستراتيجية: {str(e)}")
        return False

def delete_user_strategy(strategy_id, username):
    """حذف استراتيجية"""
    try:
        success = delete_strategy(strategy_id, username)
        return success
    except Exception as e:
        st.error(f"خطأ في حذف الاستراتيجية: {str(e)}")
        return False

def get_strategies_for_user(username):
    """الحصول على جميع استراتيجيات المستخدم"""
    try:
        strategies = get_user_strategies(username)
        return strategies
    except Exception as e:
        st.error(f"خطأ في جلب الاستراتيجيات: {str(e)}")
        return []

def get_strategy_details(strategy_id, username):
    """الحصول على تفاصيل استراتيجية محددة"""
    try:
        strategy = get_strategy_by_id(strategy_id, username)
        return strategy
    except Exception as e:
        st.error(f"خطأ في جلب تفاصيل الاستراتيجية: {str(e)}")
        return None

def save_custom_element_for_user(username, element_type, custom_text, original_text=None):
    """حفظ عنصر مخصص للمستخدم"""
    try:
        element_id = save_custom_element(username, element_type, custom_text, original_text)
        return element_id
    except Exception as e:
        st.error(f"خطأ في حفظ العنصر المخصص: {str(e)}")
        return None

def initialize_strategy_session():
    """تهيئة جلسة الاستراتيجية"""
    if "strategy_builder_step" not in st.session_state:
        st.session_state.strategy_builder_step = 0
    if "current_strategy_data" not in st.session_state:
        st.session_state.current_strategy_data = {
            "name": "", 
            "description": "", 
            "vision": "", 
            "message": "", 
            "objectives": [], 
            "values": [], 
            "logo_path": None,
            "edited_vision": "",
            "edited_message": ""
        }
    if "editing_strategy_id" not in st.session_state:
        st.session_state.editing_strategy_id = None

def reset_strategy_session():
    """إعادة تعيين جلسة الاستراتيجية"""
    st.session_state.strategy_builder_step = 0
    st.session_state.current_strategy_data = {
        "name": "", 
        "description": "", 
        "vision": "", 
        "message": "", 
        "objectives": [], 
        "values": [], 
        "logo_path": None,
        "edited_vision": "",
        "edited_message": ""
    }
    st.session_state.editing_strategy_id = None