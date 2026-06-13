# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
class MyList:
	def __init__(self):
		self._data = {}
		self._index = 0

	def append(self, value):
		self._data[self._index] = value
		self._index += 1


if __name__ == '__main__':
	lista = MyList()
	lista.append('Maria')
	lista.append('Luiz')
	print(lista._data)
	