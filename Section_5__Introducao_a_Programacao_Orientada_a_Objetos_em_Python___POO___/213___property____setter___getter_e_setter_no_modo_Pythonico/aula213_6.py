class Caneta:
	def __init__(self, cor):
		# _private protected public
		self.cor = cor   # self.outra_cor = cor
		self._cor_tampa = None

	@property
	def cor(self):
		print('ESTOU NO GETTER')
		return self._cor

	@cor.setter
	def cor(self, valor):
		print('ESTOU NO SETTER')
		self._cor = valor

	@property
	def cor_tampa(self):
		print('ESTOU NO_GETTER')
		return self._cor_tampa

	@cor_tampa.setter
	def cor_tampa(self, valor):
		print('ESTOU NO_SETTER')
		self._cor_tampa = valor


caneta = Caneta('Azul')
print()

caneta.cor = 'Rosa'
print(caneta.cor)
print()

caneta.cor_tampa = 'Azul'
print(caneta.cor_tampa)
