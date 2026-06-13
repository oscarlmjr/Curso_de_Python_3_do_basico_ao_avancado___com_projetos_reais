# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
	def __init__(self, name):
		self._name = None
		self.name = name
		print(f'AbstractFoo.__init__ {__class__.__name__}')

	@property   # getter   # a @property pertence a class
	def name(self):
		return self._name
	
	@name.setter
	@abstractmethod
	def name(self, name): ...


class Foo(AbstractFoo):
	def __init__(self, name):
		print(f'Foo.__init__ {__class__.__name__}')
		super().__init__(name)
		# print('Sou inútil')

	@AbstractFoo.name.setter
	def name(self, name):
		print(f'Foo.name {__class__.__name__}')
		self._name = name


foo = Foo('Bar')
print(foo.name)
