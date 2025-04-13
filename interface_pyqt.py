import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QComboBox, QDialog, QFormLayout, QTextEdit, QHBoxLayout, QSpinBox
)
from sistema_login import SistemaLogin
from sistema_reserva import SistemaReservaDB
from painel_admin import cadastrar_disponibilidade, gerar_relatorio

login_sys = SistemaLogin()
reserva_sys = SistemaReservaDB()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.user_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        layout.addRow("Usuário:", self.user_input)
        layout.addRow("Senha:", self.pass_input)

        login_btn = QPushButton("Entrar")
        login_btn.clicked.connect(self.fazer_login)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def fazer_login(self):
        user = self.user_input.text()
        senha = self.pass_input.text()
        success, is_admin = login_sys.login(user, senha)
        if success:
            self.hide()
            self.main = MainWindow(is_admin)
            self.main.show()
        else:
            QMessageBox.critical(self, "Erro", "Login inválido")

class MainWindow(QWidget):
    def __init__(self, is_admin):
        super().__init__()
        self.setWindowTitle("Sistema de Reservas")
        self.is_admin = is_admin
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        self.nome = QLineEdit()
        self.data = QLineEdit()
        self.hora = QLineEdit()
        self.pessoas = QSpinBox()
        self.pessoas.setRange(1, 20)
        self.tipo = QComboBox()
        self.tipo.addItems(["2 pessoas", "4 pessoas", "VIP"])

        layout.addRow("Nome:", self.nome)
        layout.addRow("Data (YYYY-MM-DD):", self.data)
        layout.addRow("Hora (HH:MM):", self.hora)
        layout.addRow("Nº de Pessoas:", self.pessoas)
        layout.addRow("Tipo de Mesa:", self.tipo)

        reservar_btn = QPushButton("Fazer Reserva")
        reservar_btn.clicked.connect(self.reservar)
        layout.addWidget(reservar_btn)

        if self.is_admin:
            admin_btn = QPushButton("Painel Admin")
            admin_btn.clicked.connect(self.abrir_admin)
            layout.addWidget(admin_btn)

        self.resultado = QLabel("")
        layout.addRow("Resultado:", self.resultado)

        self.setLayout(layout)

    def reservar(self):
        msg = reserva_sys.fazer_reserva(
            self.nome.text(),
            self.data.text(),
            self.hora.text(),
            self.pessoas.value(),
            self.tipo.currentText()
        )
        self.resultado.setText(msg)

    def abrir_admin(self):
        self.admin_dialog = AdminWindow()
        self.admin_dialog.exec_()

class AdminWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painel Administrativo")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Configuração de disponibilidade
        config_layout = QFormLayout()
        self.data_disp = QLineEdit()
        self.tipo_disp = QComboBox()
        self.tipo_disp.addItems(["2 pessoas", "4 pessoas", "VIP"])
        self.total_disp = QSpinBox()
        self.total_disp.setRange(0, 50)
        config_layout.addRow("Data (YYYY-MM-DD):", self.data_disp)
        config_layout.addRow("Tipo Mesa:", self.tipo_disp)
        config_layout.addRow("Total de Mesas:", self.total_disp)

        disp_btn = QPushButton("Salvar Disponibilidade")
        disp_btn.clicked.connect(self.salvar_disponibilidade)
        config_layout.addWidget(disp_btn)

        # Relatório mensal
        relatorio_layout = QHBoxLayout()
        self.mes_input = QLineEdit()
        self.ano_input = QLineEdit()
        gerar_btn = QPushButton("Gerar Relatório")
        gerar_btn.clicked.connect(self.gerar_relatorio)
        relatorio_layout.addWidget(QLabel("Mês:"))
        relatorio_layout.addWidget(self.mes_input)
        relatorio_layout.addWidget(QLabel("Ano:"))
        relatorio_layout.addWidget(self.ano_input)
        relatorio_layout.addWidget(gerar_btn)

        self.relatorio_area = QTextEdit()
        self.relatorio_area.setReadOnly(True)

        layout.addLayout(config_layout)
        layout.addLayout(relatorio_layout)
        layout.addWidget(self.relatorio_area)

        self.setLayout(layout)

    def salvar_disponibilidade(self):
        msg = cadastrar_disponibilidade(
            self.data_disp.text(),
            self.tipo_disp.currentText(),
            self.total_disp.value()
        )
        QMessageBox.information(self, "Info", msg)

    def gerar_relatorio(self):
        relatorio = gerar_relatorio(self.mes_input.text(), self.ano_input.text())
        self.relatorio_area.setText(relatorio)

# Execução da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
