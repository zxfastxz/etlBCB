# painel_admin.py

from sistema_reserva import SistemaReservaDB

def cadastrar_disponibilidade(data, tipo_mesa, total_mesas):
    """
    Cadastra a disponibilidade de mesas para uma data e tipo de mesa.
    :param data: Data para a disponibilidade (formato 'YYYY-MM-DD')
    :param tipo_mesa: Tipo de mesa (ex: "2 pessoas", "4 pessoas", "VIP")
    :param total_mesas: Número total de mesas disponíveis
    :return: Mensagem indicando se a disponibilidade foi cadastrada com sucesso ou erro
    """
    sistema = SistemaReservaDB()
    sistema.configurar_disponibilidade(tipo_mesa, total_mesas)
    sistema.fechar_conexao()
    return f"Disponibilidade de {total_mesas} mesas do tipo {tipo_mesa} para o dia {data} cadastrada com sucesso."

def gerar_relatorio(mes, ano):
    """
    Gera um relatório de reservas para um mês e ano específicos.
    :param mes: Mês para o relatório
    :param ano: Ano para o relatório
    :return: Relatório das reservas no formato string
    """
    sistema = SistemaReservaDB()
    relatorio = sistema.gerar_relatorio(mes, ano)
    sistema.fechar_conexao()
    return relatorio
