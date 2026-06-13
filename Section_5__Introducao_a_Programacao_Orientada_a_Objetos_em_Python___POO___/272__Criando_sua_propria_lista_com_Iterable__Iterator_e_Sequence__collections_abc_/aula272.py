# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
class MyList:
	def __init__(self):
		self._data = {}

	def append(self, value):
		self._data[0] = value


if __name__ == '__main__':
	lista = MyList()
	lista.append('Maria')
	lista.append('Luiz')
	print(lista._data)
