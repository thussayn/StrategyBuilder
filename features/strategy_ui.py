# features/strategy_ui.py
import streamlit as st
import os  # ✅ إضافة استيراد os
from core.i18n import get_text
from data.strategy_elements import (
    get_objectives_for_vision_and_message,
    get_all_objectives,
    get_values_for_vision_and_message,
    get_all_values
)
from data.models import save_custom_element
from core.file_utils import validate_logo_file, save_logo_file, delete_logo_file

def render_strategy_list(username):
    """عرض قائمة الاستراتيجيات المحفوظة"""
    from data.models import get_user_strategies, delete_strategy
    
    st.subheader(get_text("saved_strategies"))
    strategies = get_user_strategies(username)
    
    if not strategies:
        st.info(get_text("no_saved_strategies"))
    else:
        for strategy in strategies:
            with st.expander(f"📌 {strategy['name']}", expanded=False):
                if strategy.get('logo_path') and os.path.exists(strategy['logo_path']):
                    st.image(strategy['logo_path'], width=100, caption="شعار الاستراتيجية")
                
                st.markdown(f"**{get_text('strategy_description')}**: {strategy['description'] or '—'}")
                st.markdown(f"**{get_text('select_vision')}**: {strategy['vision']}")
                st.markdown(f"**{get_text('select_message')}**: {strategy['message']}")
                st.markdown(f"**{get_text('strategic_objectives')}**: {', '.join(strategy['objectives'])}")
                st.markdown(f"**{get_text('strategic_values')}**: {', '.join(strategy['values'])}")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(get_text("edit"), key=f"edit_{strategy['id']}"):
                        st.session_state.current_strategy_data = {
                            "name": strategy["name"],
                            "description": strategy["description"],
                            "vision": strategy["vision"],
                            "message": strategy["message"],
                            "objectives": strategy["objectives"],
                            "values": strategy["values"],
                            "logo_path": strategy.get("logo_path"),
                            "edited_vision": strategy["vision"],
                            "edited_message": strategy["message"]
                        }
                        st.session_state.editing_strategy_id = strategy["id"]
                        st.session_state.strategy_builder_step = 1
                        st.rerun()
                with col2:
                    if st.button(get_text("delete"), key=f"delete_{strategy['id']}"):
                        if delete_strategy(strategy["id"], username):
                            if strategy.get('logo_path'):
                                delete_logo_file(strategy['logo_path'])
                            st.success(get_text("strategy_deleted_success"))
                            st.rerun()
                        else:
                            st.error(get_text("error_deleting_strategy"))
                with col3:
                    if st.button(get_text("view"), key=f"view_{strategy['id']}"):
                        st.session_state.view_strategy = strategy
                        st.session_state.strategy_builder_step = 5
                        st.session_state.editing_strategy_id = None
                        st.rerun()
    
    st.markdown("---")
    if st.button("➕ " + get_text("create_new_strategy")):
        st.session_state.current_strategy_data = {
            "name": "", "description": "", "vision": "", "message": "", "objectives": [], "values": [], "logo_path": None,
            "edited_vision": "", "edited_message": ""
        }
        st.session_state.editing_strategy_id = None
        st.session_state.strategy_builder_step = 1
        st.rerun()

def render_step_vision(username, data):
    """عرض الخطوة 1: الرؤية"""
    current_value = data.get("edited_vision", data.get("vision", ""))
    st.text_area(
        get_text("edit_or_create_vision"),
        value=current_value,
        height=120,
        key="vision_text_area"
    )

    col1, col2 = st.columns([2, 5])
    with col1:
        if st.button(get_text("browse_visions"), use_container_width=True):
            from features.strategy_dialogs import vision_selector_dialog
            vision_selector_dialog(username, data)

    if st.button(get_text("save_and_continue"), use_container_width=True):
        final_vision = st.session_state.vision_text_area.strip()
        if not final_vision:
            st.error(get_text("vision_cannot_be_empty"))
        else:
            data["edited_vision"] = final_vision
            data["vision"] = final_vision
            if "selected_vision" not in data:
                data["selected_vision"] = final_vision
            st.session_state.strategy_builder_step = 2
            st.rerun()

def render_step_message(username, data):
    """عرض الخطوة 2: الرسالة"""
    current_value = data.get("edited_message", data.get("message", ""))
    st.text_area(
        get_text("edit_or_create_message"),
        value=current_value,
        height=120,
        key="message_text_area"
    )

    col1, col2 = st.columns([2, 5])
    with col1:
        if st.button(get_text("browse_messages"), use_container_width=True):
            from features.strategy_dialogs import message_selector_dialog
            message_selector_dialog(username, data)

    col3, col4 = st.columns(2)
    with col3:
        if st.button(get_text("back"), use_container_width=True):
            st.session_state.strategy_builder_step = 1
            st.rerun()
    with col4:
        if st.button(get_text("save_and_continue"), use_container_width=True):
            final_message = st.session_state.message_text_area.strip()
            if not final_message:
                st.error(get_text("message_cannot_be_empty"))
            else:
                data["edited_message"] = final_message
                data["message"] = final_message
                if "selected_message" not in data:
                    data["selected_message"] = final_message
                st.session_state.strategy_builder_step = 3
                st.rerun()

def render_step_objectives(username, data):
    """عرض الخطوة 3: الأهداف"""
    linked_objectives = get_objectives_for_vision_and_message(
        data.get("selected_vision", ""),
        data.get("selected_message", ""),
        username
    )
    all_objectives = get_all_objectives(username)
    
    if "selected_objectives_list" not in data:
        data["selected_objectives_list"] = data.get("objectives", [])
    
    st.subheader(get_text("strategic_objectives"))

    if linked_objectives:
        st.markdown(f"#### {get_text('objectives_linked_to_message')}")
        selected_from_linked = st.multiselect(
            get_text("select_from_linked_objectives"),
            options=linked_objectives,
            default=[obj for obj in linked_objectives if obj in data["selected_objectives_list"]],
            key="linked_objectives"
        )
        for obj in selected_from_linked:
            if obj not in data["selected_objectives_list"]:
                data["selected_objectives_list"].append(obj)
    else:
        st.info(get_text("no_linked_objectives"))

    st.markdown("---")

    st.markdown(f"#### {get_text('all_bank_objectives')}")
    selected_from_all = st.multiselect(
        get_text("select_from_all_objectives"),
        options=all_objectives,
        default=[obj for obj in all_objectives if obj in data["selected_objectives_list"]],
        key="all_objectives"
    )
    for obj in selected_from_all:
        if obj not in data["selected_objectives_list"]:
            data["selected_objectives_list"].append(obj)

    st.markdown("---")

    new_objective = st.text_input(get_text("or_add_new_objective"))
    if st.button(get_text("add_objective")) and new_objective.strip():
        obj_clean = new_objective.strip()
        if obj_clean not in data["selected_objectives_list"]:
            data["selected_objectives_list"].append(obj_clean)
            save_custom_element(username, "objective", obj_clean)

    st.markdown("---")

    if data["selected_objectives_list"]:
        st.markdown(f"#### {get_text('selected_objectives')}")
        for i, obj in enumerate(data["selected_objectives_list"]):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.text(obj)
            with col2:
                if st.button("🗑️", key=f"del_obj_{i}"):
                    data["selected_objectives_list"].pop(i)
                    st.rerun()
    else:
        st.info(get_text("no_objectives_selected"))

    data["objectives"] = data["selected_objectives_list"]

    col1, col2 = st.columns(2)
    with col1:
        if st.button(get_text("back"), use_container_width=True):
            st.session_state.strategy_builder_step = 2
            st.rerun()
    with col2:
        if st.button(get_text("save_and_continue"), use_container_width=True):
            st.session_state.strategy_builder_step = 4
            st.rerun()

def render_step_values(username, data):
    """عرض الخطوة 4: القيم"""
    linked_values = get_values_for_vision_and_message(
        data.get("selected_vision", ""),
        data.get("selected_message", ""),
        username
    )
    all_values = get_all_values(username)
    
    if "selected_values_list" not in data:
        data["selected_values_list"] = data.get("values", [])
    
    st.subheader(get_text("strategic_values"))

    if linked_values:
        st.markdown(f"#### {get_text('values_linked_to_message')}")
        selected_from_linked = st.multiselect(
            get_text("select_from_linked_values"),
            options=linked_values,
            default=[val for val in linked_values if val in data["selected_values_list"]],
            key="linked_values"
        )
        for val in selected_from_linked:
            if val not in data["selected_values_list"]:
                data["selected_values_list"].append(val)
    else:
        st.info(get_text("no_linked_values"))

    st.markdown("---")

    st.markdown(f"#### {get_text('all_bank_values')}")
    selected_from_all = st.multiselect(
        get_text("select_from_all_values"),
        options=all_values,
        default=[val for val in all_values if val in data["selected_values_list"]],
        key="all_values"
    )
    for val in selected_from_all:
        if val not in data["selected_values_list"]:
            data["selected_values_list"].append(val)

    st.markdown("---")

    new_value = st.text_input(get_text("or_add_new_value"))
    if st.button(get_text("add_value")) and new_value.strip():
        val_clean = new_value.strip()
        if val_clean not in data["selected_values_list"]:
            data["selected_values_list"].append(val_clean)
            save_custom_element(username, "value", val_clean)

    st.markdown("---")

    if data["selected_values_list"]:
        st.markdown(f"#### {get_text('selected_values')}")
        for i, val in enumerate(data["selected_values_list"]):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.text(val)
            with col2:
                if st.button("🗑️", key=f"del_val_{i}"):
                    data["selected_values_list"].pop(i)
                    st.rerun()
    else:
        st.info(get_text("no_values_selected"))

    data["values"] = data["selected_values_list"]

    col1, col2 = st.columns(2)
    with col1:
        if st.button(get_text("back"), use_container_width=True):
            st.session_state.strategy_builder_step = 3
            st.rerun()
    with col2:
        if st.button(get_text("save_and_continue"), use_container_width=True):
            st.session_state.strategy_builder_step = 5
            st.rerun()

def render_step_preview(username, data):
    """عرض الخطوة 5: المعاينة والحفظ"""
    import os
    from data.models import create_strategy, update_strategy
    
    st.subheader(get_text("preview_and_save"))
    
    name = st.text_input(get_text("strategy_name"), value=data["name"])
    description = st.text_area(get_text("strategy_description"), value=data["description"])
    data["name"] = name
    data["description"] = description
    
    st.markdown("---")
    st.subheader("📸 " + get_text("upload_logo"))
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        current_logo_path = data.get("logo_path")
        if current_logo_path and os.path.exists(current_logo_path):
            st.image(current_logo_path, width=150, caption=get_text("current_logo"))
            if st.button("🗑️ " + get_text("remove_logo"), use_container_width=True):
                if delete_logo_file(current_logo_path):
                    data["logo_path"] = None
                    st.success(get_text("logo_removed_success"))
                    st.rerun()
        else:
            st.info(get_text("no_logo_uploaded"))
    
    with col2:
        uploaded_logo = st.file_uploader(
            get_text("upload_logo"),
            type=["png", "jpg", "jpeg"],
            help="الحد الأقصى 5MB - PNG, JPG, JPEG"
        )
        
        if uploaded_logo:
            try:
                validate_logo_file(uploaded_logo)
                temp_logo_path = save_logo_file(uploaded_logo, username, "temp")
                if temp_logo_path:
                    st.image(temp_logo_path, width=150)
                    data["temp_logo_path"] = temp_logo_path
                    data["uploaded_logo"] = uploaded_logo
                    
            except Exception as e:
                st.error(str(e))
    
    vision = data.get("edited_vision", data.get("vision", ""))
    message = data.get("edited_message", data.get("message", ""))
    
    st.markdown("---")
    st.subheader("👁️ " + get_text("preview_and_save"))
    
    preview_logo_path = data.get("temp_logo_path") or data.get("logo_path")
    if preview_logo_path and os.path.exists(preview_logo_path):
        st.image(preview_logo_path, width=120)
    
    st.markdown(f"### {get_text('select_vision')}")
    st.markdown(f"> {vision}")
    st.markdown(f"### {get_text('select_message')}")
    st.markdown(f"> {message}")
    st.markdown(f"### {get_text('strategic_objectives')}")
    for obj in data["objectives"]:
        st.markdown(f"- {obj}")
    st.markdown(f"### {get_text('strategic_values')}")
    for val in data["values"]:
        st.markdown(f"- {val}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button(get_text("back"), use_container_width=True):
            st.session_state.strategy_builder_step = 4
            st.rerun()
    with col2:
        if st.button(get_text("save_strategy"), use_container_width=True):
            if not name.strip():
                st.error(get_text("strategy_name_required"))
            else:
                final_logo_path = data.get("logo_path")
                if "uploaded_logo" in data:
                    if data.get("logo_path"):
                        delete_logo_file(data["logo_path"])
                    strategy_id = st.session_state.editing_strategy_id or "new"
                    final_logo_path = save_logo_file(data["uploaded_logo"], username, strategy_id)
                
                final_vision = data.get("edited_vision", data.get("vision", ""))
                final_message = data.get("edited_message", data.get("message", ""))
                
                if st.session_state.editing_strategy_id:
                    success = update_strategy(
                        st.session_state.editing_strategy_id, username, name, description,
                        final_vision, final_message, data["objectives"], data["values"], final_logo_path
                    )
                else:
                    strategy_id = create_strategy(
                        username, name, description,
                        final_vision, final_message, data["objectives"], data["values"], final_logo_path
                    )
                    success = True
                
                if success:
                    st.success(get_text("strategy_saved_success"))
                    st.session_state.strategy_builder_step = 0
                    st.rerun()
    with col3:
        if st.button(get_text("export_to_word"), use_container_width=True):
            from features.strategy_export import export_to_word
            export_data = {
                "name": name,
                "description": description,
                "vision": vision,
                "message": message,
                "objectives": data["objectives"],
                "values": data["values"],
                "edited_vision": vision,
                "edited_message": message,
                "logo_path": preview_logo_path
            }
            export_to_word(export_data)
    with col4:
        if st.button(get_text("export_to_pdf"), use_container_width=True):
            from features.strategy_export import export_to_pdf
            export_data = {
                "name": name,
                "description": description,
                "vision": vision,
                "message": message,
                "objectives": data["objectives"],
                "values": data["values"],
                "edited_vision": vision,
                "edited_message": message,
                "logo_path": preview_logo_path
            }
            export_to_pdf(export_data)
