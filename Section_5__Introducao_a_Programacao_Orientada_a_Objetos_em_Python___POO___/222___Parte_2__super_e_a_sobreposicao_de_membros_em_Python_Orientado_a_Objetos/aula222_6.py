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

class A(object):
	atributo_a = 'valor a'
	def __init__(self, atributo):
		print(__class__.__name__)
		print(f'__init__ atributo')
		self.atributo = atributo

	def metodo(self):
		print('A')
		

class B(A):
	atributo_b = 'valor b'
	def metodo(self):
		print('B')


class C(B):
	atributo_c = 'valor c'
	def metodo(self):
		print('C')


c = C('atributo')
print(c.atributo)
