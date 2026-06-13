
try:
	import sys

	# sys.path.append('C:\Users\oscar\AppData\Local\Programs\Python\Python313')
	sys.path.append('D:\projeto_sistema_bancario_v006')
except ModuleNotFoundError:
	...

# import modulo_agencia_matriz
from modulo_agencia_matriz import Matriz
Matriz('0001').menu_self(None)
