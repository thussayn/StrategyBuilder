from data.db import get_conn

def get_user_pref_lang(user) -> str | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT preferred_lang FROM user_settings WHERE username=?", (user["username"],))
    row = cur.fetchone()
    return row[0] if row and row[0] else None

def get_user_pref_theme(user) -> str | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT preferred_theme FROM user_settings WHERE username=?", (user["username"],))
    row = cur.fetchone()
    return row[0] if row and row[0] else None
