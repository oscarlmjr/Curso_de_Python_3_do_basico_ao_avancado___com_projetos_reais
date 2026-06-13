# Escopo da classe e de métodos da classe

class Animal:

	def __init__(self, nome):
		self.nome = nome

		variavel = 'valor'
		print(variavel)


leao = Animal(nome='Leão')
print(leao.nome)
