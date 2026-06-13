from abc import ABC, abstractmethod
from modulo_contas import Conta, saque1, saque2, conta1, conta2


class Pessoa(ABC):
# class Pessoa:
	def __init__(self, nome, idade, solicitacao=None):
		self.nome = nome
		self.idade = idade
		self.solicitacao = solicitacao

	@property
	def nome(self):
		return self._nome 

	@nome.setter
	def nome(self, valor):
		self._nome = valor

	@property
	def idade(self):
		return self._idade

	@idade.setter
	def idade(self, valor):
		self._idade = valor

	@abstractmethod
	def conta(self):
		...

class Cliente(Pessoa):

	def conta(self):
		return self.solicitacao
		...


def saque(solicitacao: Conta):
	saque_conta = solicitacao.sacar()

	if saque_conta:
		return f'Saque autorizado: R$ {saque_conta}'
	else:
		return 'Saque não autorizado: saldo insuficiente'
	

cliente = Cliente('Oscar', 47, saque(saque1))
cliente1_solicitacao = cliente.__dict__ | conta1.__dict__
print(cliente1_solicitacao)
print()
cliente = Cliente('Gabriel', 17, saque(saque2))
cliente2_solicitacao = cliente.__dict__ | conta2.__dict__
print(cliente2_solicitacao)
print()
