# app.py
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# Set page config early
st.set_page_config(
    page_title="Secure Modular Starter", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Encrypted Cookie Manager
cookies = EncryptedCookieManager(
    prefix="secure_modular_starter/",
    password="your-very-strong-secret-key-change-in-prod-2025!"  # ⚠️ Change in production
)

if not cookies.ready():
    st.stop()

# --- Early imports for auth and session management ---
from users.auth_service import (
    ensure_db_ready,
    restore_session_from_cookie,
    is_authenticated,
    get_current_user,
    logout
)

# Helper to update user preferences from sidebar
def update_user_language_and_theme(lang: str, theme: str):
    from users.auth_service import update_user_prefs
    user = get_current_user()
    if user:
        update_user_prefs(user["username"], preferred_lang=lang, preferred_theme=theme)


# Ensure DB is ready
ensure_db_ready()

# Restore session from cookie — unless we just logged out
if st.session_state.get("post_logout"):
    st.session_state.pop("post_logout", None)
else:
    restore_session_from_cookie(cookies)

# Initialize language and theme if not set
if "lang" not in st.session_state:
    st.session_state.lang = cookies.get("lang", "en")
if "theme" not in st.session_state:
    st.session_state.theme = cookies.get("theme", "modern_light")

# Import other modules
from core.i18n import get_text
from features import auth as auth_feature
from core.layout import app_header, app_footer
from features import dashboard_admin, dashboard_editor, dashboard_viewer, home, about
from core.theme import apply_theme, apply_navigation_fix

# Sidebar
with st.sidebar:
    st.markdown("### 🌐 " + get_text("language"))
    lang_keys = ["en", "ar"]
    idx = lang_keys.index(st.session_state.lang) if st.session_state.lang in lang_keys else 0
    lang = st.selectbox(
        get_text("language_selector_label"),
        options=lang_keys,
        format_func=lambda x: {"en": get_text("english"), "ar": get_text("arabic")}[x],
        index=idx,
        key="lang_selector"
    )
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        cookies["lang"] = lang
        if is_authenticated():
            update_user_language_and_theme(lang, st.session_state.get("theme", "modern_light"))
        cookies.save()
        st.rerun()

    st.markdown("---")
    st.markdown("### 🎨 " + get_text("theme"))
    theme_keys = ["modern_light", "professional_dark", "warm_earth", "saudi", "soft"]
    current_theme = st.session_state.get("theme", "modern_light")
    
    # إنشاء قاموس لتحويل قيم الثيم إلى نصوص معروضة
    theme_display_names = {
        "modern_light": get_text("modern_light"),
        "professional_dark": get_text("professional_dark"), 
        "warm_earth": get_text("warm_earth"),
        "saudi": get_text("saudi"),
        "soft": get_text("soft")
    }
    
    theme = st.selectbox(
        get_text("theme_selector_label"),
        options=theme_keys,
        index=theme_keys.index(current_theme) if current_theme in theme_keys else 0,
        format_func=lambda x: theme_display_names[x],
        key="theme_selector"
    )
    if theme != st.session_state.get("theme", "modern_light"):
        st.session_state.theme = theme
        cookies["theme"] = theme
        if is_authenticated():
            update_user_language_and_theme(st.session_state.lang, theme)
        cookies.save()
        st.rerun()

    # Logout button
    if is_authenticated():
        st.markdown("---")
        if st.button(get_text("logout")):
            logout(cookies=cookies)
            st.session_state.post_logout = True
            st.rerun()

# Apply theme and fixes
apply_theme(st.session_state.theme, st.session_state.lang)
apply_navigation_fix()

# Header
app_header(get_text("app_title"), lang=st.session_state.lang)

# Routing
if not is_authenticated():
    auth_feature.render(cookies=cookies)
else:
    user = get_current_user()
    role = user.get("role", "Viewer")

    # تحديد التبويب النشط
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "Home"

    home_label = get_text("home_title")
    about_label = get_text("about_title")
    dashboard_label = get_text("dashboard")
    settings_label = get_text("settings")

    tab_labels = [home_label, about_label, dashboard_label, settings_label]

    # تحديد index التبويب النشط
    tab_index = 0
    if st.session_state.active_tab == "About":
        tab_index = 1
    elif st.session_state.active_tab == "Dashboard": 
        tab_index = 2
    elif st.session_state.active_tab == "Settings":
        tab_index = 3

    tab = st.tabs(tab_labels)

    with tab[0]:
        home.render()
    with tab[1]:
        about.render()
    with tab[2]:
        if role == "Admin":
            dashboard_admin.render()
        elif role == "Editor":
            dashboard_editor.render()
        else:
            dashboard_viewer.render()
    with tab[3]:
        from ui.forms import settings_form
        settings_form(cookies=cookies)

app_footer(lang=st.session_state.lang)