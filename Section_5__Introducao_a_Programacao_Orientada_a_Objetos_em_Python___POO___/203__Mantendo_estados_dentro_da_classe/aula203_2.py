# Mantendo estados dentro da classe

class Camera:
	def __init__(self, nome, filmando=False):
		self.nome = nome
		self.filmando = filmando

	def filmar(self):
		if self.filmando:
			print(f'{self.nome} JÁ está filmando...')
			return
		self.filmando = True
		print(f'{self.nome} está filmando...')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
