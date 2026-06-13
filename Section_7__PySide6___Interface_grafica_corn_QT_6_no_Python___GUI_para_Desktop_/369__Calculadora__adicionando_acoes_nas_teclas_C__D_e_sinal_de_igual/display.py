from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
	# eqRequested = Signal()
	eqPressed = Signal()
	delPressed = Signal()
	clearPressed = Signal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.configStyle()

	def configStyle(self):
		margins = [TEXT_MARGIN for _ in range(4)]
		self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
		self.setMinimumHeight(BIG_FONT_SIZE * 2)
		self.setMinimumWidth(MINIMUM_WIDTH)
		self.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.setTextMargins(*margins)

	def keyPressEvent(self, event: QKeyEvent) -> None:
		text = event.text().strip()
		key = event.key()
		KEYS = Qt.Key

		# isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
		isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
		# isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
		isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
		# isEsc = key in [KEYS.Key_Escape]
		isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

		if isEnter:
		# if isEnter or text == '=':
			# print('Enter pressionado, sinal emitido', type(self).__name__)
			print(f'EQ {text} pressionado, sinal emitido', type(self).__name__)
			self.eqPressed.emit()
			return event.ignore()
		# return super().keyPressEvent(event)

		if isDelete:
		# if isDelete or text.lower() == 'c':
			# print('isDelete pressionado, sinal emitido', type(self).__name__)
			print(f'isDelete {text} pressionado, sinal emitido',
			type(self).__name__)
			self.delPressed.emit()
			return event.ignore()

		if isEsc:
			print('isEsc pressionado, sinal emitido', type(self).__name__)
			self.clearPressed.emit()
			return event.ignore()

		# Não passar daqui se não tiver texto
		if isEmpty(text):
			return event.ignore()

		print('Texto', text)

