import sys

from main_window_2 import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH


def temp_label(texto):
	label1 = QLabel(texto)
	label1.setStyleSheet('font-size: 100px;')
	return label1


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	# icon = QIcon(WINDOW_ICON_PATH)
	icon = QIcon(str(WINDOW_ICON_PATH))
	window.setWindowIcon(icon)
	app.setWindowIcon(icon)

	window.show()
	app.exec()
