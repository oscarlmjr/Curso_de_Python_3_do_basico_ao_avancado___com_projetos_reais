# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
	ano = 2023   # atributo de classe

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade


	def metodo_de_classe(self):
		print('Hey')

print(Pessoa.ano)

p1 = Pessoa('João', 34)
p1.metodo_de_classe()
Pessoa.metodo_de_classe(p1)
