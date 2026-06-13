# Escopo da classe e de métodos da classe

class Animal:

	def __init__(self, nome):
		self.nome = nome


leao = Animal(nome='Leão')
print(leao.nome)
