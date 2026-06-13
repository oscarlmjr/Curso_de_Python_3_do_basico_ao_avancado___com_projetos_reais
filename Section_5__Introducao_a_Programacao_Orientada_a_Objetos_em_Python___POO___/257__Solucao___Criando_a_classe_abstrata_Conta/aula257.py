from abc import ABC, abstractmethod


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

class Banco:
	def autenticar(cliente_cadastro):
		lista_banco = [{'_nome': 'Oscar', 'agencia': '0001', 'numero_conta': '11111'},
					{'_nome': 'Gabriel', 'agencia': '0001', 'numero_conta': '11112'}
					]

		for cliente_cadastrado in lista_banco:
			if cliente_cadastrado['_nome'] in cliente_cadastro['_nome']:  # type: ignore
				if cliente_cadastrado['agencia'] in cliente_cadastro['agencia']:  # type: ignore
					if cliente_cadastrado['numero_conta'] in cliente_cadastro['numero_conta']:  # type: ignore
						print('Cliente autenticado')
						print(f'depósito: R$',deposito)
						print(cliente.conta())
						# print(saque(saque1))
						return
		else:
			print('Cliente não autenticado')

def saque(solicitacao: Conta):
	saque_conta = solicitacao.sacar()

	if saque_conta:
		return f'Saque autorizado: R$ {saque_conta}'
	else:
		return 'Saque não autorizado: saldo insuficiente'


conta1 = ContaCorrente('0001', '11111', 100)
deposito = conta1.deposito()
saque1 =  ContaCorrente('0001', '11111', deposito, 110)
cliente = Cliente('Oscar', 47, saque(saque1))
# cliente1.conta()
cliente1_cadastro = cliente.__dict__ | conta1.__dict__
print(cliente1_cadastro)
print()
banco = Banco.autenticar(cliente1_cadastro)

print()
conta2 = ContaPoupanca('0001', '11112', 100)
deposito = conta2.deposito()
saque2 =  ContaPoupanca('0001', '11112', deposito, 110)
cliente = Cliente('Gabriel', 17, saque(saque2))
# cliente2.conta()
cliente2_cadastro = cliente.__dict__ | conta2.__dict__
print(cliente2_cadastro)
print()

banco = Banco.autenticar(cliente2_cadastro)
print()


# print(cliente1.nome)
# print(cliente1.idade)

# cliente1 = Cliente
# cliente1.nome = 'Oscar'
# cliente1.idade = 47
# print(Cliente.nome)
# print(Cliente.idade)
