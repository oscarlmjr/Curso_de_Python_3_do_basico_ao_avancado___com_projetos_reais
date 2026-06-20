"""
while em Python - Utilizado para realizar ações enquanto
uma condição for verdadeira.
Requisitos: entender condições e operadores
"""
x = 0
while x < 10:
	if x == 3:
		x = x + 1
		print(x)
		break
	print(x)
	x = x + 1
print('Término da operação.')
