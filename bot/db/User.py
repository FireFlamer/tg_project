import sqlite3

db_name = "users.db"

class User:
    
    @staticmethod
    def create_user(id: int, username: str, role: str):
        con = sqlite3.connect(db_name)
        con.execute(
            "INSERT INTO users (id, username, role) VALUES (? ,?, ?)",
            (id, username, role),
        )

        con.commit()
        con.close()
    
    @staticmethod
    def check_user_existance(user_id: int) -> bool:
        con = sqlite3.connect(db_name)
        existence = con.execute(f"SELECT * FROM users WHERE id = {user_id}").fetchone()
        con.close()

        if existence:
            return True
        return False
        
    @staticmethod
    def get_user_role(user_id: int) -> str | None:
        con = sqlite3.connect(db_name)
        try:
            role = con.execute(f"SELECT role FROM users WHERE id = {user_id}").fetchone()[0]
            return role
        except TypeError:
            return None
