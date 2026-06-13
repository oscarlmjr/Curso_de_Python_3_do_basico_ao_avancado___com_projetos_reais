# Métodos em instâncias de classes Python
# Hard coded - Algo escrito diretamente no código

class Carro:
	
	def __init__(self, alguma_coisa='Sei lá'):
		self.nome = alguma_coisa


fusca = Carro()
print(fusca.nome)

celta = Carro()
print(celta.nome)
