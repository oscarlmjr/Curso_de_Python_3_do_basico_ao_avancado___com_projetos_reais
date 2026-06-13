# (Parte 2) try, Except, else e finally

try:
	a = 18
	b = 0
	c = a / b  # para no erro
	print('Continua')

except ZeroDivisionError as e:
	print(e.__class__)
	print(e.__class__.__name__)
	print(e, '\n')

print('Continuar')
