import sqlite3

def build_users_db():
    con = sqlite3.connect('users.db', check_same_thread=False)
    cur = con.cursor() 

    _create_users_db(cur=cur) 

    con.close()


def _create_users_db(cur: sqlite3.Cursor):
    return cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            role TEXT NOT NULL
        )"""
    )

build_users_db()
