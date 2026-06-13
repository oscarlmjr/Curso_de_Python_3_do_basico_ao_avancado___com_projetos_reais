class Pessoa:
	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')
print(p1)
print(p1.nome)
print(p1.sobrenome)

print()

p2 = Pessoa(1, True)
print(p2)
print(p2.nome)
print(p2.sobrenome)
