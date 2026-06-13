# Métodos em instâncias de classes Python
# Hard coded - Algo escrito diretamente no código

class Carro:
	
	def __init__(self, nome):
		self.nome = nome


fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro(nome='Celta')
print(celta.nome)
