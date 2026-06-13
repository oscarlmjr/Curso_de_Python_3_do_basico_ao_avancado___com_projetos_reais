'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y):
	print(f'{x=}, y={y}', '|', 'x + y = ', x + y)

print(soma(1, 2), '\n')

soma(1, 2)
soma(y=2, x=1)
print()


def soma(x, y, z):
	print(f"{x}, {y}, {z}, sep=' - '", end=' | ')
	print(x, y, z, sep=" - ")

soma(1, 2, 3)
soma(y=2, z=3, x=1)  # ao nomear um argumento todos os outros
					 # devem ser nomeados "após" ele.
