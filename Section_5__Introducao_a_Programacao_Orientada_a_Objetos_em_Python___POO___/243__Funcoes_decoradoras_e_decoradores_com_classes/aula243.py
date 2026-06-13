# Funções decoradoras e decoradores com classes
class Time:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		class_name = self.__class__.__name__
		class_dict = self.__dict__
		class_repr = f'{class_name} - ({class_dict})'
		return class_repr

class Planeta:
	def __init__(self, nome):
		self.nome = nome
	
	def __repr__(self):
		class_name = self.__class__.__name__
		class_dict = self.__dict__
		class_repr = f'{class_name}({class_dict})'
		return class_repr


brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
