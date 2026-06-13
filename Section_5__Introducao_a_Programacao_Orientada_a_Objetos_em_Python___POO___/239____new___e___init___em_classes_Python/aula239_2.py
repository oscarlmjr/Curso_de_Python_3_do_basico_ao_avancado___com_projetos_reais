class A:

	def __init__(self):
		print('Sou o init')

	def __repr__(self):
		return f'A.__repr__'


a = A()
print(a, '\n')

a = object.__new__(A)
print(a, '\n')

a.__init__()
print(a)
