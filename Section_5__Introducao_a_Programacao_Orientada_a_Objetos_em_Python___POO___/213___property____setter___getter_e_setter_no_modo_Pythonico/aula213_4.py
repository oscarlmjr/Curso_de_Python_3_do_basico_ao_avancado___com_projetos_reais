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

	@property
	def cor(self):
		return self._cor

	@cor.setter
	def cor(self, valor):
		if valor == 'Rosa':
			raise ValueError('Não aceito essa cor')
		self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Pink'
print(caneta.cor)
caneta.cor = 'Rosa'   # ValueError: Não aceito essa cor
