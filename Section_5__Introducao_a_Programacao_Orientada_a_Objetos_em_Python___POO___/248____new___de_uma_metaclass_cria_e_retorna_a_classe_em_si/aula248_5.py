def meu_repr(self):
	return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
	def __new__(mcs, name, bases, dct):
		print('METACLASS NEW')
		cls = super().__new__(mcs, name, bases, dct)
		cls.attr = 1234
		cls.__repr__ = meu_repr
		print(cls.__dict__)
		return cls


class Pessoa(metaclass=Meta):
	def __new__(cls, *args, **kwargs):
		print('MEU NEW')
		instancia = super().__new__(cls)
		return instancia

	def __init__(self, nome):
		print('MEU INIT')
		self.nome = nome

	def falar(self):
		print('FALANDO ...')


p1 = Pessoa('Luiz')
print(p1.attr)
print(p1)
