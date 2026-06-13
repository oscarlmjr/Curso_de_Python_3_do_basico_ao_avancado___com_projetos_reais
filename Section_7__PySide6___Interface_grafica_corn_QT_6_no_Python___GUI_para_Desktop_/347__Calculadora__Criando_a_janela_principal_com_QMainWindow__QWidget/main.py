import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = QMainWindow()

	cw = QWidget()
	v_layout = QVBoxLayout()
	cw.setLayout(v_layout)

	label1 = QLabel('O meu texto')
	# label1.setStyleSheet('font-size: 150px;')
	# window.v_layout.addWidget(label1)
	v_layout.addWidget(label1)
	
	window.setCentralWidget(cw)

	window.show()
	app.exec()
