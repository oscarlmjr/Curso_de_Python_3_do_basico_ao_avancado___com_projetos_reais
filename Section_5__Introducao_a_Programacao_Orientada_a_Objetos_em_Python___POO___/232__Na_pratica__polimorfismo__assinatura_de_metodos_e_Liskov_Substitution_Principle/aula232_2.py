from abc import ABC, abstractmethod


class Notificacao(ABC):
	def __init__(self, mensagem) -> None:
		self.mensagem = mensagem

	@abstractmethod
	def enviar(self) -> bool:
		...


class NotificacaoEmail(Notificacao):
	def enviar(self):
		print('E-mail: enviando:', self.mensagem)


class NotificacaoSMS(Notificacao):
	def enviar(self):
		print('SMS: enviando - ', self.mensagem)


n = NotificacaoSMS('testando notificação')
n.enviar()
