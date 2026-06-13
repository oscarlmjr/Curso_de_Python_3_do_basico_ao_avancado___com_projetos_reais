# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começarem com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
	def __init__(self, cor):
		# _private protected public
		self._cor = cor
		print(self._cor)

	@property
	def cor(self):
		print('PROPERTY')
		return self._cor

	@cor.setter
	def cor(self, valor):
		print('ESTOU NO SETTER', valor)
		self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'

# getter -> obter valor
print(caneta.cor)
