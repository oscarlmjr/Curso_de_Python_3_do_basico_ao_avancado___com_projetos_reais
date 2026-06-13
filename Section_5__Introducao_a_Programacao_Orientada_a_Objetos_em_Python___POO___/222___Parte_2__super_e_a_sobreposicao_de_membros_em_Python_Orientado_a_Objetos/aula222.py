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

class A:
	atributo_a = 'valor a'
	# print('super(B)')
	def metodo(self):
		print('A')

class B(A):
	atributo_b = 'valor b'
	def metodo(self):
		print('B')

class C(B):
	atributo_c = 'valor c'
	def metodo(self):
		super().metodo()
		print()
		# super(B).metodo()   # AttributeError: 'super' object has no attribute 'metodo'
		super(B, self).metodo()
		super(C, self).metodo()
		print('C')

c = C()
print(C.atributo_a)
print(C.atributo_b)
print(C.atributo_c)
c.metodo()
