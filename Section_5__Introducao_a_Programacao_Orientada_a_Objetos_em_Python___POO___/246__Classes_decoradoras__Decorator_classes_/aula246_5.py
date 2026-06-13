# Classes decoradoras (Decorator classes)
class Multiplicar:

	def __init__(self, func):
		self.func = func
		self._multiplicador = 10   # protegido

	def __call__(self, *args, **kwargs):
		resultado = self.func(*args, **kwargs)
		return resultado * self._multiplicador


@Multiplicar   # decorator
def soma(x, y):
	return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
