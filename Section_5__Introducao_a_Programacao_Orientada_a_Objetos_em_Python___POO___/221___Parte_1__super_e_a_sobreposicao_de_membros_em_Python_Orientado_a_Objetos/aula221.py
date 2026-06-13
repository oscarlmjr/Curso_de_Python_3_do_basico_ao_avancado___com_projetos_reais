# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
	...


string = MinhaString('Luiz')
print(string.upper())


class MinhaString(str):
	def upper(self):
		return 'ABC'
		# super()


string = MinhaString('Luiz')
print(string.upper())
