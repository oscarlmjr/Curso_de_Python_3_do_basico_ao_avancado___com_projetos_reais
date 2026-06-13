# (Parte 2) try, Except, else e finally

try:
	print('Linha 1'[1000])

except (TypeError, IndexError) as error:
	print('TypeError + IndexError')
	print('MSG:', error)
	print('Nome:', error.__class__.__name__)

print('Continuar')
