import sqlite3

DB_NAME = "finwise.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Users Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    # Chat History Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            role TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_login(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def save_message(username, role, message):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (username, role, message) VALUES (?, ?, ?)", (username, role, message))
    conn.commit()
    conn.close()

def get_chat_history(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT role, message FROM chat_history WHERE username=? ORDER BY timestamp", (username,))
    rows = c.fetchall()
    conn.close()
    return [{"role": role, "text": message} for role, message in rows]
