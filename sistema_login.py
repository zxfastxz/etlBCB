import sqlite3
import hashlib

class SistemaLogin:
    def __init__(self):
        self.conn = sqlite3.connect("reserva_restaurante.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                senha_hash TEXT NOT NULL,
                is_admin INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def login(self, username, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.cursor.execute(
            "SELECT is_admin FROM funcionarios WHERE username=? AND senha_hash=?",
            (username, senha_hash)
        )
        resultado = self.cursor.fetchone()
        if resultado:
            return True, bool(resultado[0])
        return False, False
