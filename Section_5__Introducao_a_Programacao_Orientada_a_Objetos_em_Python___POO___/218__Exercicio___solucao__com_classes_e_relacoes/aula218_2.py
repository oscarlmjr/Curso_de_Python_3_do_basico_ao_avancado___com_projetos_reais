class Carro:
	def __init__(self, nome):
		self.nome = nome
		self._motor = None
		self._fabricante = None

	@property
	def motor(self):
		return self._motor

	@motor.setter
	def motor(self, valor):
		self._motor = valor

	@property
	def fabricante(self):
		return self._fabricante

	@fabricante.setter
	def fabricante(self, valor):
		self._fabricante = valor

class Motor:
	def __init__(self, nome):
		self.nome = nome

class Fabricante:
	def __init__(self, nome):
		self.nome = nome

motor_1_0 = Motor('1.0')
motor_2_0 = Motor('2.0')
volkswagen = Fabricante('Volkswagen')
chevrolet = Fabricante('Chevrolet')
	
polo = Carro('Polo')
polo.motor = motor_2_0
polo.fabricante = volkswagen
print(polo.nome, polo.fabricante.nome, polo.motor.nome)

onix = Carro('Ônix')
onix.motor = motor_2_0
onix.fabricante = chevrolet

print(onix.nome, onix.fabricante.nome, onix.motor.nome)
