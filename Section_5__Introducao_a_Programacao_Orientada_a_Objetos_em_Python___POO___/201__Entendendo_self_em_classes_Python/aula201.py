# Entendedo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instância.

class Carro:
	def __init__(blabla, nome):   # self - convenção (referencia a própria instância)
		blabla.nome = nome

	def acelerar(blabla):
		print(f'{blabla.nome} está acelerando...')


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
