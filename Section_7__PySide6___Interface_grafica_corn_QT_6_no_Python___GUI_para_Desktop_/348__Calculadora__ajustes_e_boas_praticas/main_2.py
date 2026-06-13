import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel


def temp_label(texto):
	label1 = QLabel(texto)
	label1.setStyleSheet('font-size: 100px;')
	return label1


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()

	window.addWidgetToVLayout(temp_label('Label 1'))
	window.addWidgetToVLayout(temp_label('Label 2'))
	window.addWidgetToVLayout(temp_label('Label 3'))
	window.addWidgetToVLayout(temp_label('Label 4'))
	window.addWidgetToVLayout(temp_label('Label 5'))

	window.show()
	app.exec()
