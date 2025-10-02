# users/auth_service.py
import secrets
import streamlit as st
from data.db import get_conn
from data.models import migrate
from data.seed import seed_admin
from core.security import verify_password, hash_password

SESSION_KEY = "auth_user"

def ensure_db_ready():
    migrate()
    seed_admin()

def load_user_preferences(username: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT preferred_lang, preferred_theme FROM user_settings WHERE username = ?", (username,))
    row = cur.fetchone()
    if row:
        return {"preferred_lang": row[0] or "en", "preferred_theme": row[1] or "light"}
    return {"preferred_lang": "en", "preferred_theme": "light"}

def login(username: str, password: str, remember: bool, cookies=None):
    if not username or not password:
        return False, "missing_credentials"
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username, password_hash, role FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    if not row:
        return False, "user_not_found"
    if not verify_password(password, row[1]):
        return False, "invalid_password"
    
    prefs = load_user_preferences(username)
    st.session_state[SESSION_KEY] = {
        "username": row[0],
        "role": row[2],
        "preferred_lang": prefs["preferred_lang"],
        "preferred_theme": prefs["preferred_theme"]
    }
    st.session_state.pop("explicitly_logged_out", None)

    if cookies is not None:
        cookies["auth_user"] = username
        cookies["lang"] = prefs["preferred_lang"]
        cookies["theme"] = prefs["preferred_theme"]
        cookies.save()
    return True, "ok"

def is_authenticated() -> bool:
    return SESSION_KEY in st.session_state

def get_current_user():
    return st.session_state.get(SESSION_KEY)

def logout(cookies=None):
    st.session_state.pop(SESSION_KEY, None)
    st.session_state.pop("lang", None)
    st.session_state.pop("theme", None)
    st.session_state.pop("last_username", None)  # ← إضافة جديدة
    st.session_state["explicitly_logged_out"] = True
    if cookies is not None:
        for key in ["auth_user", "lang", "theme"]:
            cookies[key] = ""
        cookies.save()

def restore_session_from_cookie(cookies):
    if st.session_state.get("explicitly_logged_out"):
        return False
    if SESSION_KEY in st.session_state:
        return True
    username = cookies.get("auth_user")
    if not username:
        return False
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username, role FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if row:
        prefs = load_user_preferences(username)
        st.session_state[SESSION_KEY] = {
            "username": row[0],
            "role": row[1],
            "preferred_lang": prefs["preferred_lang"],
            "preferred_theme": prefs["preferred_theme"]
        }
        st.session_state.pop("explicitly_logged_out", None)
        cookies["lang"] = prefs["preferred_lang"]
        cookies["theme"] = prefs["preferred_theme"]
        cookies.save()
        return True
    else:
        for key in ["auth_user", "lang", "theme"]:
            if key in cookies:
                del cookies[key]
        cookies.save()
        st.session_state.pop("explicitly_logged_out", None)
        return False

# --- User Management ---
def list_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username, role FROM users ORDER BY username")
    return [{"username": r[0], "role": r[1]} for r in cur.fetchall()]

def create_user(username: str, password: str, role: str):
    if not username or not password:
        return False, "username_password_required"
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users(username, password_hash, role) VALUES (?,?,?)",
                    (username, hash_password(password), role))
        cur.execute("INSERT INTO user_settings(username, preferred_lang, preferred_theme) VALUES (?,?,?)",
                    (username, None, None))
        conn.commit()
        return True, "user_created"
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            return False, "username_exists"
        return False, "unknown_error"

def delete_user(username: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username=?", (username,))
    cur.execute("DELETE FROM user_settings WHERE username=?", (username,))
    conn.commit()

def set_role(username: str, role: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE users SET role=? WHERE username=?", (role, username))
    conn.commit()

def request_password_reset(username: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users WHERE username=?", (username,))
    if not cur.fetchone():
        return None
    token = secrets.token_urlsafe(12)
    cur.execute("INSERT INTO reset_tokens(username, token) VALUES (?,?)", (username, token))
    conn.commit()
    return token

def change_password_with_token(token: str, new_password: str) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username FROM reset_tokens WHERE token=? ORDER BY id DESC LIMIT 1", (token,))
    row = cur.fetchone()
    if not row:
        return False
    cur.execute("UPDATE users SET password_hash=? WHERE username=?", (hash_password(new_password), row[0]))
    cur.execute("DELETE FROM reset_tokens WHERE token=?", (token,))
    conn.commit()
    return True

def update_user_prefs(username: str, preferred_lang=None, preferred_theme=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE user_settings SET preferred_lang=?, preferred_theme=? WHERE username=?",
                (preferred_lang, preferred_theme, username))
    conn.commit()