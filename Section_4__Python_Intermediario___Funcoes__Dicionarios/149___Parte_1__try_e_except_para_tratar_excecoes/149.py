# try, Except, else e finally

try:
	a = 18
	b = 0
	print('Linha 1', '\n')
	c = a / b
	print('Linha 2')

except ZeroDivisionError:
	print('Divisão por zero.')

print('Continuar')
