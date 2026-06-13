from modulo_pessoa import cliente, cliente1_solicitacao, cliente2_solicitacao
from modulo_contas import deposito


class Banco:
	
	def autenticar(cliente_solicitacao):
		lista_banco = [{'_nome': 'Oscar', 'agencia': '0001', 'numero_conta': '11111'},
					{'_nome': 'Gabriel', 'agencia': '0001', 'numero_conta': '11112'}
					]

		for cliente_cadastrado in lista_banco:
			# if cliente_cadastrado['_nome'] in cliente_solicitacao['_nome']:
			if cliente_solicitacao['_nome'] == cliente_cadastrado['_nome']:
				if cliente_solicitacao['agencia'] == cliente_cadastrado['agencia']:
					if cliente_solicitacao['numero_conta'] == cliente_cadastrado['numero_conta']:
						print('Cliente autenticado')
						print(f'depósito: R$',deposito)
						print(cliente.conta())
						# print(saque(saque1))
						return
		else:
			print('Cliente não autenticado')


banco = Banco.autenticar(cliente1_solicitacao)
print()
banco = Banco.autenticar(cliente2_solicitacao)
print()
