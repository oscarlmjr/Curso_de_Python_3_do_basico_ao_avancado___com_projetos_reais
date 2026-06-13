# Variáveis livres + nonlocal (locals, globals)

def fora(x):
	a = x   # variável livre

	def dentro():
		print(locals(), '\n')
		print(dentro.__code__.co_freevars, '\n')
		return a

	return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print()
print(dentro2())
