import sqlite3
import hashlib

def cadastrar_usuario(username, senha, is_admin=True):
    # Conectando ao banco de dados (deve ser o mesmo usado no sistema)
    conn = sqlite3.connect("reserva_restaurante.db")
    cursor = conn.cursor()

    # Criar a tabela se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL,
            is_admin INTEGER NOT NULL
        )
    ''')

    # Criptografar a senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO funcionarios (username, senha_hash, is_admin) VALUES (?, ?, ?)",
            (username, senha_hash, int(is_admin))
        )
        conn.commit()
        print(f"✅ Usuário '{username}' cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print(f"⚠️ O usuário '{username}' já existe.")
    finally:
        conn.close()

# 🔐 Altere aqui os dados do admin
cadastrar_usuario("admin", "admin123", is_admin=True)
