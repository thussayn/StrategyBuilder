# ui/forms.py
import streamlit as st
from core.i18n import get_text
from users.auth_service import update_user_prefs, get_current_user

def settings_form(cookies=None):
    st.title(get_text("settings"))

    user = get_current_user()
    if not user:
        st.warning(get_text("must_be_logged_in"))
        return

    username = user["username"]
    current_lang = st.session_state.get("lang", "en")
    current_theme = st.session_state.get("theme", "modern_light")

    # Language
    st.markdown("### " + get_text("language"))
    lang_labels = [get_text("english"), get_text("arabic")]
    label_to_lang = {get_text("english"): "en", get_text("arabic"): "ar"}
    current_label = get_text("arabic") if current_lang == "ar" else get_text("english")
    selected_label = st.selectbox(
        get_text("language"),
        options=lang_labels,
        index=lang_labels.index(current_label),
        key="settings_lang_select"
    )
    selected_lang = label_to_lang[selected_label]

    # Theme - للعرض فقط مع معلومات
    st.markdown("### " + get_text("theme"))
    
    theme_display_names = {
        "modern_light": get_text("modern_light"),
        "professional_dark": get_text("professional_dark"),
        "warm_earth": get_text("warm_earth"),
        "saudi": get_text("saudi"),
        "soft": get_text("soft"),
    }
    current_theme_display = theme_display_names.get(current_theme, get_text("modern_light"))
    
    # عرض الثيم الحالي مع رسالة توجيهية - مترجم الآن
    st.info(f"**{get_text('current_theme')}:** {current_theme_display}")
    st.write(get_text("theme_change_hint"))
    
    # خط فاصل
    st.markdown("---")
    
    # زر الحفظ للغة فقط
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button(get_text("save"), type="primary", use_container_width=True):
            update_user_prefs(username, preferred_lang=selected_lang, preferred_theme=current_theme)
            st.session_state.lang = selected_lang
            if cookies is not None:
                cookies["lang"] = selected_lang
                cookies.save()
            st.success(get_text("settings_saved"))
            
    with col2:
        # زر الرجوع - مترجم الآن
        if st.button(get_text("back_to_home"), use_container_width=True):
            # الرجوع للهوم
            st.session_state.active_tab = "Home"
            st.rerun()