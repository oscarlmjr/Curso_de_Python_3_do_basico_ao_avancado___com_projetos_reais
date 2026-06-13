# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
	def __init__(self):
		self._data = {}
		self._index = 0

	def append(self, value):
		self._data[self._index] = value
		self._index += 1

	def __len__(self) -> int:
		return self._index

	def __getitem__(self, index):
		print('__getitem__')
		return self._data[index]


if __name__ == '__main__':
	lista = MyList()
	lista.append('Maria')
	lista.append('Luiz')
	print(lista[0])
	print(len(lista))
	