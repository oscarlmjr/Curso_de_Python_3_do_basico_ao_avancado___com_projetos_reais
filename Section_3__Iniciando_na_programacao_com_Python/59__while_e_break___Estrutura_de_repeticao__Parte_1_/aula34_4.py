"""
while em Python - Utilizado para realizar ações enquanto
uma condição for verdadeira.
Requisitos: entender condições e operadores
"""

x = 0  # coluna
while x < 5:
	y = 0  # linha
	while y < 3:
		print(f'x vale {x} e Y vale {y}.')
		y += 1
	x += 1  # x = x + 1
print('Término da operação.')
