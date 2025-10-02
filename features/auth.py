import streamlit as st
from core.i18n import get_text
from users.auth_service import login

def render(cookies=None):
    st.title(get_text("login"))
    
    # مفاتيح الجلسة لتخزين المدخلات مؤقتًا
    if "login_username" not in st.session_state:
        st.session_state.login_username = ""
    if "login_password" not in st.session_state:
        st.session_state.login_password = ""
    if "login_remember" not in st.session_state:
        st.session_state.login_remember = False

    # عرض الحقول
    username = st.text_input(
        get_text("username"),
        value=st.session_state.login_username,
        key="login_username_input"
    )
    password = st.text_input(
        get_text("password"),
        type="password",
        value=st.session_state.login_password,
        key="login_password_input"
    )
    
    # ✅ حل مضمون لعرض "Remember me" بدون اختفاء أو كسر
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        remember = st.checkbox("", value=st.session_state.login_remember, key="login_remember_checkbox")
    with col2:
        st.markdown(
            f"<span style='color: var(--text); font-weight: 500; line-height: 1.5;'>{get_text('remember_me')}</span>",
            unsafe_allow_html=True
        )

    # تحديث القيم في الجلسة عند التغيير
    st.session_state.login_username = username
    st.session_state.login_password = password
    st.session_state.login_remember = remember

    # زر تسجيل الدخول من نوع primary (يتبع الثيم)
    if st.button(get_text("login_button"), type="primary", use_container_width=True):
        if username.strip() == "" or password.strip() == "":
            st.error(get_text("username_password_required"))
        else:
            success, message_key = login(username, password, remember, cookies=cookies)
            if success:
                # حفظ اسم المستخدم في الجلسة فقط (لو طلب تذكرني)
                if remember:
                    st.session_state.last_username = username
                st.success(get_text("logged_in_success"))
                st.rerun()
            else:
                st.error(get_text(message_key))


def render_register_user():
    st.title(get_text("create_new_user"))
    username = st.text_input(get_text("username"))
    password = st.text_input(get_text("password"), type="password")
    role_options = ["Admin", "Editor", "Viewer"]
    role = st.selectbox(get_text("role"), options=role_options)
    
    if st.button(get_text("create_user_button")):
        from users.auth_service import create_user
        success, message_key = create_user(username, password, role)
        if success:
            st.success(get_text("user_created_success"))
        else:
            st.error(get_text(message_key))


def render_logout():
    from users.auth_service import logout
    logout()
    st.success(get_text("logged_out_success"))
    st.rerun()