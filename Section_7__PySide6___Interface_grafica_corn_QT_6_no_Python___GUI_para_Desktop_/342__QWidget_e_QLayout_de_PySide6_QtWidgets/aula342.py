# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys
from PySide6.QtWidgets import QApplication, QPushButton


app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')
botao.show()

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
botao2.show()


app.exec()  # O loop da aplicação
