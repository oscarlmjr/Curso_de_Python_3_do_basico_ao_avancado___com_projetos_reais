# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
	def upper(self):
		print('CHAMOU UPPER')
		retorno = super(MinhaString, self).upper()
		print('DEPOIS DO UPPER')
		return retorno


string = MinhaString('Luiz')
print(string.upper())
