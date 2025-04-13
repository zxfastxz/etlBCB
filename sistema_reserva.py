from datetime import datetime, timedelta
import uuid


class Reserva:
    """Representa uma reserva única no sistema."""

    def __init__(self, nome, data, hora, numero_pessoas, tipo_mesa, desconto, taxa_servico, valor_total):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.data = data
        self.hora = hora
        self.numero_pessoas = numero_pessoas
        self.tipo_mesa = tipo_mesa
        self.desconto = desconto
        self.taxa_servico = taxa_servico
        self.valor_total = valor_total
        self.valor_completo = valor_total + taxa_servico
        self.criado_em = datetime.now()


class SistemaReservaDB:
    """
    Sistema de gerenciamento de reservas para um restaurante de grande porte.
    Permite reservas com múltiplos parâmetros, cancelamentos com políticas
    definidas e verificação de disponibilidade por tipo de mesa.
    """

    def __init__(self):
        self.reservas = {}  # ID -> Reserva
        self.reservas_por_cliente = {}  # nome -> [IDs de reservas]
        self.preco_mesa = {
            "2 pessoas": 50,
            "4 pessoas": 80,
            "VIP": 150
        }
        self.desconto_por_pessoas = 0.1
        self.taxa_servico_percentual = 0.05
        self.politica_cancelamento = {
            "cancelamento_antecedencia": timedelta(days=2),
            "taxa_cancelamento": 0.2
        }

    def verificar_disponibilidade(self, data, hora, tipo_mesa):
        """
        Verifica se já existe uma reserva no mesmo horário e tipo de mesa.
        """
        for reserva in self.reservas.values():
            if reserva.data == data and reserva.hora == hora and reserva.tipo_mesa == tipo_mesa:
                return False
        return True

    def fazer_reserva(self, nome, data_str, hora_str, numero_pessoas, tipo_mesa):
        """
        Cria uma nova reserva com validação e verificação de disponibilidade.

        :param nome: Nome do cliente
        :param data_str: Data no formato YYYY-MM-DD
        :param hora_str: Hora no formato HH:MM
        :param numero_pessoas: Número de pessoas na reserva
        :param tipo_mesa: Tipo de mesa escolhido
        :return: Mensagem de confirmação ou erro
        """
        try:
            data = datetime.strptime(data_str, '%Y-%m-%d').date()
            hora = datetime.strptime(hora_str, '%H:%M').time()
        except ValueError:
            return "Erro: Data ou hora no formato incorreto."

        if tipo_mesa not in self.preco_mesa:
            return f"Erro: Tipo de mesa inválido. Tipos disponíveis: {', '.join(self.preco_mesa.keys())}"

        if not self.verificar_disponibilidade(data, hora, tipo_mesa):
            return f"Erro: Já existe uma reserva para o tipo de mesa '{tipo_mesa}' neste horário."

        valor_base = self.preco_mesa[tipo_mesa] * numero_pessoas / 2
        desconto = valor_base * self.desconto_por_pessoas if numero_pessoas > 4 else 0
        valor_total = valor_base - desconto
        taxa_servico = valor_total * self.taxa_servico_percentual

        nova_reserva = Reserva(nome, data, hora, numero_pessoas, tipo_mesa, desconto, taxa_servico, valor_total)
        self.reservas[nova_reserva.id] = nova_reserva
        self.reservas_por_cliente.setdefault(nome, []).append(nova_reserva.id)

        return (
            f"Reserva realizada com sucesso! ID: {nova_reserva.id}\n"
            f"Data: {data_str} às {hora_str}\n"
            f"Tipo de mesa: {tipo_mesa}\n"
            f"Número de pessoas: {numero_pessoas}\n"
            f"Desconto: R$ {desconto:.2f}\n"
            f"Taxa de serviço: R$ {taxa_servico:.2f}\n"
            f"Valor total: R$ {nova_reserva.valor_completo:.2f}"
        )

    def verificar_reservas_cliente(self, nome):
        """
        Lista todas as reservas feitas por um cliente.

        :param nome: Nome do cliente
        :return: Lista com os detalhes das reservas
        """
        if nome not in self.reservas_por_cliente:
            return f"Não foram encontradas reservas para {nome}."

        mensagens = []
        for res_id in self.reservas_por_cliente[nome]:
            reserva = self.reservas[res_id]
            mensagens.append(
                f"[ID: {reserva.id}] {reserva.data} às {reserva.hora.strftime('%H:%M')} | "
                f"Mesa: {reserva.tipo_mesa} | Pessoas: {reserva.numero_pessoas} | "
                f"Total: R$ {reserva.valor_completo:.2f}"
            )
        return "\n".join(mensagens)

    def cancelar_reserva(self, reserva_id):
        """
        Cancela uma reserva com base no ID e aplica a política de cancelamento.

        :param reserva_id: ID único da reserva
        :return: Mensagem de cancelamento ou erro
        """
        reserva = self.reservas.get(reserva_id)
        if not reserva:
            return f"Reserva com ID {reserva_id} não encontrada."

        tempo_antecedencia = reserva.data - datetime.now().date()
        if tempo_antecedencia >= self.politica_cancelamento["cancelamento_antecedencia"]:
            self._remover_reserva(reserva)
            return f"Reserva {reserva_id} cancelada com sucesso."
        else:
            taxa_cancelamento = reserva.valor_completo * self.politica_cancelamento["taxa_cancelamento"]
            reembolso = reserva.valor_completo - taxa_cancelamento
            self._remover_reserva(reserva)
            return (
                f"Reserva {reserva_id} cancelada.\n"
                f"Reembolso: R$ {reembolso:.2f} (taxa de cancelamento de R$ {taxa_cancelamento:.2f})."
            )

    def _remover_reserva(self, reserva):
        """Remove a reserva do sistema."""
        del self.reservas[reserva.id]
        self.reservas_por_cliente[reserva.nome].remove(reserva.id)
        if not self.reservas_por_cliente[reserva.nome]:
            del self.reservas_por_cliente[reserva.nome]

    def listar_todas_reservas(self):
        """
        Lista todas as reservas no sistema.

        :return: Lista formatada de reservas
        """
        if not self.reservas:
            return "Nenhuma reserva registrada."

        resultado = ["Reservas registradas:"]
        for res in self.reservas.values():
            resultado.append(
                f"[ID: {res.id}] Cliente: {res.nome} | {res.data} às {res.hora.strftime('%H:%M')} | "
                f"Mesa: {res.tipo_mesa} | Pessoas: {res.numero_pessoas} | Total: R$ {res.valor_completo:.2f}"
            )
        return "\n".join(resultado)
