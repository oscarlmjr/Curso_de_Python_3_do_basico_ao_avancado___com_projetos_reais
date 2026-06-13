class A:

	def __new__(cls):
		return object.__new__(A)

	def __init__(self):
		print('Sou o init')

	def __repr__(self):
		return f'A.__repr__'


a = A()
print(a)
