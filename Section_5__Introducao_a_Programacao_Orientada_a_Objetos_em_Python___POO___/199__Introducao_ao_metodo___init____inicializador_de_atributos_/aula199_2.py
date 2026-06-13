class Pessoa:
	def __init__(self, nome, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')
p1.nome = 'Otávio'
p1.sobrenome = 'Luiz'
print(p1)
print(p1.nome)
print(p1.sobrenome)

print()

p2 = Pessoa(1, True)
p2.nome = 2
p2.sobrenome = False
print(p2)
print(p2.nome)
print(p2.sobrenome)
