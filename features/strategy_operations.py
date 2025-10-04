# features/strategy_operations.py
import streamlit as st
import os  # ✅ إضافة استيراد os
from core.i18n import get_text
from data.strategy_elements import (
    get_all_visions,
    get_messages_for_vision,
    get_objectives_for_vision_and_message,
    get_all_objectives,
    get_values_for_vision_and_message,
    get_all_values
)

def validate_strategy_step(current_step, data):
    """التحقق من صحة البيانات في كل خطوة"""
    if current_step == 1:
        if not data.get("edited_vision", "").strip() and not data.get("vision", "").strip():
            st.error(get_text("vision_cannot_be_empty"))
            return False
    
    elif current_step == 2:
        if not data.get("edited_message", "").strip() and not data.get("message", "").strip():
            st.error(get_text("message_cannot_be_empty"))
            return False
    
    elif current_step == 5:
        if not data.get("name", "").strip():
            st.error(get_text("strategy_name_required"))
            return False
    
    return True

def get_available_elements(username, data, element_type):
    """الحصول على العناصر المتاحة حسب النوع"""
    if element_type == "visions":
        return get_all_visions(username)
    
    elif element_type == "messages":
        vision = data.get("selected_vision", "")
        if vision:
            return get_messages_for_vision(vision, username)
        return []
    
    elif element_type == "linked_objectives":
        vision = data.get("selected_vision", "")
        message = data.get("selected_message", "")
        if vision and message:
            return get_objectives_for_vision_and_message(vision, message, username)
        return []
    
    elif element_type == "all_objectives":
        return get_all_objectives(username)
    
    elif element_type == "linked_values":
        vision = data.get("selected_vision", "")
        message = data.get("selected_message", "")
        if vision and message:
            return get_values_for_vision_and_message(vision, message, username)
        return []
    
    elif element_type == "all_values":
        return get_all_values(username)
    
    return []

def update_selected_elements(data, element_type, selected_items):
    """تحديث العناصر المختارة"""
    if element_type == "objectives":
        if "selected_objectives_list" not in data:
            data["selected_objectives_list"] = []
        
        # إضافة العناصر المختارة الجديدة
        for item in selected_items:
            if item not in data["selected_objectives_list"]:
                data["selected_objectives_list"].append(item)
        
        # حفظ القائمة النهائية
        data["objectives"] = data["selected_objectives_list"]
    
    elif element_type == "values":
        if "selected_values_list" not in data:
            data["selected_values_list"] = []
        
        # إضافة العناصر المختارة الجديدة
        for item in selected_items:
            if item not in data["selected_values_list"]:
                data["selected_values_list"].append(item)
        
        # حفظ القائمة النهائية
        data["values"] = data["selected_values_list"]

def remove_element_from_list(data, element_type, index):
    """إزالة عنصر من القائمة"""
    if element_type == "objective" and "selected_objectives_list" in data:
        if 0 <= index < len(data["selected_objectives_list"]):
            data["selected_objectives_list"].pop(index)
            data["objectives"] = data["selected_objectives_list"]
            return True
    
    elif element_type == "value" and "selected_values_list" in data:
        if 0 <= index < len(data["selected_values_list"]):
            data["selected_values_list"].pop(index)
            data["values"] = data["selected_values_list"]
            return True
    
    return False

def prepare_strategy_export_data(data):
    """تحضير بيانات الاستراتيجية للتصدير"""
    return {
        "name": data.get("name", ""),
        "description": data.get("description", ""),
        "vision": data.get("edited_vision", data.get("vision", "")),
        "message": data.get("edited_message", data.get("message", "")),
        "objectives": data.get("objectives", []),
        "values": data.get("values", []),
        "edited_vision": data.get("edited_vision", data.get("vision", "")),
        "edited_message": data.get("edited_message", data.get("message", "")),
        "logo_path": data.get("temp_logo_path") or data.get("logo_path")
    }

def handle_logo_upload(uploaded_file, username, strategy_id, current_logo_path):
    """معالجة رفع اللوجو"""
    from core.file_utils import validate_logo_file, save_logo_file, delete_logo_file
    
    try:
        validate_logo_file(uploaded_file)
        
        # حذف اللوجو القديم إذا موجود
        if current_logo_path:
            delete_logo_file(current_logo_path)
        
        # حفظ اللوجو الجديد
        new_logo_path = save_logo_file(uploaded_file, username, strategy_id)
        return new_logo_path, True
    
    except Exception as e:
        return str(e), False

def get_strategy_builder_steps():
    """الحصول على خطوات بناء الاستراتيجية"""
    return [
        get_text("select_vision"),
        get_text("select_message"),
        get_text("strategic_objectives"),
        get_text("strategic_values"),
        get_text("preview_and_save")
    ]

def get_current_step_progress(current_step, total_steps=5):
    """الحصول على تقدم الخطوة الحالية"""
    if current_step == 0:
        return 0, ""
    
    step = current_step - 1
    steps = get_strategy_builder_steps()
    progress_text = f"{steps[step]} ({step + 1}/{total_steps})"
    progress_value = (step + 1) / total_steps
    
    return progress_value, progress_text

def apply_dialog_styles(lang):
    """تطبيق الأنماط على الـ Dialogs"""
    is_rtl = lang == "ar"
    font_family = "'Tajawal', sans-serif" if lang == "ar" else "sans-serif"
    text_align = "right" if is_rtl else "left"
    direction = "rtl" if is_rtl else "ltr"
    
    st.markdown(f"""
    <style>
    /* تطبيق الستايل على جميع عناصر الـ Dialog */
    .stDialog * {{
        font-family: {font_family} !important;
        direction: {direction} !important;
        text-align: {text_align} !important;
    }}
    
    /* تطبيق الستايل على الزر */
    .stDialog .stButton > button {{
        border-radius: 12px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        background: var(--brand) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15) !important;
        width: 100% !important;
    }}
    
    .stDialog .stButton > button:hover {{
        background: color-mix(in srgb, var(--brand), white 10%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    }}
    
    /* تطبيق الستايل على مربع النص */
    .stDialog .stTextArea > div > div > textarea {{
        background: var(--input-bg) !important;
        color: var(--input-text) !important;
        border: 1px solid var(--input-border) !important;
        border-radius: 14px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        text-align: {text_align} !important;
        font-family: {font_family} !important;
    }}
    
    /* تطبيق الستايل على القائمة المنسدلة */
    .stDialog [data-baseweb="select"] {{
        direction: {direction} !important;
    }}
    
    .stDialog [data-baseweb="menu"] {{
        font-family: {font_family} !important;
        direction: {direction} !important;
    }}
    
    .stDialog [data-baseweb="menu"] li {{
        font-family: {font_family} !important;
        text-align: {text_align} !important;
    }}
    </style>
    """, unsafe_allow_html=True)