# Escopo da classe e de métodos da classe

class Animal:

	def __init__(self, nome):
		self.nome = nome

		variavel = 'valor'
		print(variavel)

	def acao(self):
		return f'{self.nome} está executando uma ação'
		

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.acao())
# leao.acao()
