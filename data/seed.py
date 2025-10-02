# data/seed.py
from data.db import get_conn
from core.security import hash_password

def seed_admin():
    """Seeds the database with an admin user if it doesn't exist."""
    conn = get_conn()
    cur = conn.cursor()
    
    # Check if the admin user already exists
    cur.execute("SELECT username FROM users WHERE username='admin'")
    if cur.fetchone():
        return  # Admin already exists, no need to insert

    # Insert a default admin user
    password_hash = hash_password("admin123")  # You can change the password here
    cur.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "Admin"))
    
    # Insert default settings for the admin user
    cur.execute("INSERT INTO user_settings (username, preferred_lang, preferred_theme) VALUES (?, ?, ?)",
                ("admin", "en", "light"))  # You can change the default language/theme
    
    conn.commit()
    conn.close()
