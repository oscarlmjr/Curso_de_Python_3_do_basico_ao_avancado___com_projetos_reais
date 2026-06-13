class A:

	def __new__(cls, *args, **kwargs):
		instancia = super().__new__(cls)
		return instancia

	def __init__(self, x):
		self.x = x
		print('Sou o init')

	def __repr__(self):
		return f'A.__repr__'


a = A(123)
print(a.x)
