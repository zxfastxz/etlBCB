import sqlite3
import hashlib

def criar_banco():
    conn = sqlite3.connect("reserva_restaurante.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL,
            is_admin INTEGER NOT NULL
        )
    ''')

    # Criar admin padrão
    senha_hash = hashlib.sha256("admin123".encode()).hexdigest()

    cursor.execute(
        "INSERT OR IGNORE INTO funcionarios (username, senha_hash, is_admin) VALUES (?, ?, ?)",
        ("admin", senha_hash, 1)
    )

    conn.commit()
    conn.close()
    print("✅ Banco de dados configurado com sucesso.")

# Executar setup
criar_banco()
