import sys

from main_window_2 import MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow,
						 QWidget, QVBoxLayout, QLabel)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()

	label1 = QLabel('O meu texto')
	window.v_layout.addWidget(label1)

	window.show()
	app.exec()


