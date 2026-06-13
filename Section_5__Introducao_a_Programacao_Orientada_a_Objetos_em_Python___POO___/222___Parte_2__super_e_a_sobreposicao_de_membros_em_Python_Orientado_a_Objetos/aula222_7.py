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
		self.atributo = atributo
	def metodo(self):
		print('A')

class B(A):
	atributo_b = 'valor b'
	def __init__(self, atributo, outra_coisa):
		super().__init__(atributo)
		print(__class__.__name__)
		self.outra_coisa = outra_coisa
	def metodo(self):
		print('B')

class C(B):
	atributo_c = 'valor c'
	def __init__(self, *args, **kwargs):
		print('EI, burlei o sistema.')
		super().__init__(*args, **kwargs)
	def metodo(self):
		print('C')

c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)
