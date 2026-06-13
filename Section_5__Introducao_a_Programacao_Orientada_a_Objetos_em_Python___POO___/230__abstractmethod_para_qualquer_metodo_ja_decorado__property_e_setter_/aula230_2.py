# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC


class AbstractFoo(ABC):
	def __init__(self, name):
		self.name = name

	@property   # getter   # a @property pertence a class
	def name(self):
		return 123

	@name.setter
	def name(self, name): ...


class Foo(AbstractFoo):
	def __init__(self, name):
		super().__init__(name)
		print('Sou inútil')


foo = Foo('Bar')
print(foo.name)
