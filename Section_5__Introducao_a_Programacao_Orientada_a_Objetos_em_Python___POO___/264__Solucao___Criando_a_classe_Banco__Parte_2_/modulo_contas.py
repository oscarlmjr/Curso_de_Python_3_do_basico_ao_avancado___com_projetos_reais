from abc import ABC, abstractmethod


class Conta(ABC):
	def __init__(self, agencia, numero_conta, saldo=0, saque=0):
		self.agencia = agencia
		self.numero_conta = numero_conta
		self.saldo = saldo
		self.saque = saque

	@abstractmethod
	def sacar(self):
		...

class ContaCorrente(Conta):

	def deposito(self):
		return self.saldo

	def sacar(self):
		self.limite_extra = 1.1
		if self.saque <= self.saldo * self.limite_extra:
			# return True
			return self.saque

class ContaPoupanca(Conta):

	def deposito(self):
		return self.saldo

	def sacar(self):
		if self.saque <= self.saldo:
			return self.saque
		

conta1 = ContaCorrente('0001', '11111', 100)
deposito = conta1.deposito()
saque1 =  ContaCorrente('0001', '11111', deposito, 110)

conta2 = ContaPoupanca('0001', '11112', 100)
deposito = conta2.deposito()
saque2 =  ContaPoupanca('0001', '11112', deposito, 110)
