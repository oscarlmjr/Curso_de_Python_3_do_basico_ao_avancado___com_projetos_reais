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
		self.cor_tinta = cor

	@property
	def cor(self):
		print('PROPERTY')
		return self.cor_tinta

def mostrar(caneta):
	return caneta.cor


caneta = Caneta('Azul')
# getter -> obter valor
print(caneta.cor)
mostrar(caneta)
