import sqlite3

def ver_reservas():
    conn = sqlite3.connect("reserva_restaurante.db")
    cursor = conn.cursor()

    # Exibir todas as reservas
    print("\n--- Reservas ---")
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    if reservas:
        for reserva in reservas:
            print(reserva)
    else:
        print("Nenhuma reserva encontrada.")

def ver_mesas_disponiveis():
    conn = sqlite3.connect("reserva_restaurante.db")
    cursor = conn.cursor()

    # Exibir mesas disponíveis
    print("\n--- Mesas Disponíveis ---")
    cursor.execute("SELECT * FROM mesas_disponiveis")
    mesas = cursor.fetchall()
    if mesas:
        for mesa in mesas:
            print(mesa)
    else:
        print("Nenhuma mesa disponível encontrada.")

def ver_funcionarios():
    conn = sqlite3.connect("reserva_restaurante.db")
    cursor = conn.cursor()

    # Exibir funcionários cadastrados
    print("\n--- Funcionários Cadastrados ---")
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    if funcionarios:
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Nenhum funcionário cadastrado.")

if __name__ == "__main__":
    ver_reservas()
    ver_mesas_disponiveis()
    ver_funcionarios()
