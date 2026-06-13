# try, Except, else e finally

try:
	print('Linha 1'[1000])


except (TypeError, IndexError):
	print('TypeError + IndexError')

print('Continuar')
