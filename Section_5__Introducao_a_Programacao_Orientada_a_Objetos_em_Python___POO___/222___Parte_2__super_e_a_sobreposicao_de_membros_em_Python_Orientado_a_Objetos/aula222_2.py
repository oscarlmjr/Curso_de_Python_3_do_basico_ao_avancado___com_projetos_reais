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
	print('super(A)')
	def metodo(self):
		print('A')


class B(A):
	atributo_b = 'valor b'
	print('super(B)')
	def metodo(self):
		print('B')


class C(B):
	atributo_c = 'valor c'
	def metodo(self):
		super()   # Não executa após a chamada da primeira função.
		super(A)
		super(B)
		super(C)
