class A:

	def __new__(cls):
		print('Antes de criar a instância')
		instancia = super().__new__(cls)
		print('Depois')
		instancia.x = 213
		return instancia

	def __init__(self):
		print('Sou o init')

	def __repr__(self):
		return f'A.__repr__'


a = A()
print(a.x)
