# Métodos em instâncias de classes Python

class Carro:
	
	def __init__(self):
		self.nome = 'Fusca'   # Hard coded


fusca = Carro()
# fusca.nome = 'Fusca'
print(fusca.nome)

celta = Carro()
print(celta.nome)
