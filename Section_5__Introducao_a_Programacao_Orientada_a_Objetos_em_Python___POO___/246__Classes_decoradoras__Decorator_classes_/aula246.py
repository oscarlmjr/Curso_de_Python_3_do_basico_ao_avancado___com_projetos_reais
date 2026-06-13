# Classes decoradoras (Decorator classes)
class Multiplicar:

	def __init__(self, args):
		print('INIT', args)

	def __call__(self, *args, **kwargs):
		print(args, kwargs)


@Multiplicar   # decorator
def soma(x, y):
	return x + y


dois_mais_dois = soma(2, 4)
print(dois_mais_dois)
