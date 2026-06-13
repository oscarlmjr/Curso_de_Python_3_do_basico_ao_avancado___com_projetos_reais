class Meta(type):
	def __new__(mcs, name, bases, dct):
		print('METACLASS NEW')
		cls = super().__new__(mcs, name, bases, dct)
		return cls


class Pessoa(metaclass=Meta):
	def __new__(cls, *args, **kwargs):
		print('MEU NEW')
		instancia = super().__new__(cls)
		return instancia

	def __init__(self, nome):
		print('MEU INIT')
		self.nome = nome


# p1 = Pessoa('Luiz')
