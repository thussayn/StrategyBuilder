# data/models.py
from data.db import get_conn
import json
from typing import List, Dict, Optional

def migrate():
    """Creates tables if they do not exist."""
    conn = get_conn()
    cursor = conn.cursor()

    # Existing tables (users, user_settings, reset_tokens)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        preferred_lang TEXT,
        preferred_theme TEXT,
        FOREIGN KEY(username) REFERENCES users(username)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reset_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        token TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # New: strategies table with logo_path
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        vision TEXT NOT NULL,
        message TEXT NOT NULL,
        objectives TEXT NOT NULL,
        strategic_values TEXT NOT NULL,
        logo_path TEXT,  -- ✅ الحقل الجديد
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # New: custom_elements table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS custom_elements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        element_type TEXT NOT NULL CHECK(element_type IN ('vision', 'message', 'objective', 'value')),
        original_text TEXT,
        custom_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# === Strategy CRUD ===

def create_strategy(
    username: str,
    name: str,
    description: str,
    vision: str,
    message: str,
    objectives: List[str],
    values: List[str],
    logo_path: str = None  # ✅ الباراميتر الجديد
) -> int:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO strategies (username, name, description, vision, message, objectives, strategic_values, logo_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (username, name, description, vision, message, json.dumps(objectives), json.dumps(values), logo_path))
    strategy_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return strategy_id


def get_user_strategies(username: str) -> List[Dict]:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM strategies WHERE username = ? ORDER BY created_at DESC", (username,))
    rows = cursor.fetchall()
    conn.close()
    strategies = []
    for row in rows:
        strategies.append({
            "id": row[0],
            "username": row[1],
            "name": row[2],
            "description": row[3],
            "vision": row[4],
            "message": row[5],
            "objectives": json.loads(row[6]),
            "values": json.loads(row[7]),
            "logo_path": row[8],  # ✅ الحقل الجديد
            "created_at": row[9],
            "updated_at": row[10]
        })
    return strategies


def get_strategy_by_id(strategy_id: int, username: str) -> Optional[Dict]:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM strategies WHERE id = ? AND username = ?", (strategy_id, username))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    return {
        "id": row[0],
        "username": row[1],
        "name": row[2],
        "description": row[3],
        "vision": row[4],
        "message": row[5],
        "objectives": json.loads(row[6]),
        "values": json.loads(row[7]),
        "logo_path": row[8],  # ✅ الحقل الجديد
        "created_at": row[9],
        "updated_at": row[10]
    }


def update_strategy(
    strategy_id: int,
    username: str,
    name: str,
    description: str,
    vision: str,
    message: str,
    objectives: List[str],
    values: List[str],
    logo_path: str = None  # ✅ الباراميتر الجديد
) -> bool:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE strategies
        SET name = ?, description = ?, vision = ?, message = ?, objectives = ?, strategic_values = ?, logo_path = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ? AND username = ?
    """, (name, description, vision, message, json.dumps(objectives), json.dumps(values), logo_path, strategy_id, username))
    changed = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return changed


def delete_strategy(strategy_id: int, username: str) -> bool:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM strategies WHERE id = ? AND username = ?", (strategy_id, username))
    changed = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return changed

# دوال custom_elements تبقى كما هي بدون تغيير
def save_custom_element(username: str, element_type: str, custom_text: str, original_text: str = None) -> int:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO custom_elements (username, element_type, original_text, custom_text)
        VALUES (?, ?, ?, ?)
    """, (username, element_type, original_text, custom_text))
    element_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return element_id


def get_custom_elements(username: str, element_type: str) -> List[Dict]:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, custom_text, original_text
        FROM custom_elements
        WHERE username = ? AND element_type = ?
        ORDER BY created_at ASC
    """, (username, element_type))
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "text": r[1], "original": r[2]} for r in rows]