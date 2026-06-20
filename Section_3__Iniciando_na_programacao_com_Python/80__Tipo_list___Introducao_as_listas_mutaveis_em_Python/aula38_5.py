"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
secreto = 'perfume'
digitadas = []
chances = 7
while True:
	if chances == 0:
		print('Você perdeu.')
		break
	letra = input('Digite uma letra: ')
	if len(letra) > 1:
		print('Digite apenas uma letra.')
		continue
	digitadas.append(letra)
	if letra in secreto:
		print(f'A letra "{letra}" existe na palavra '
			  f'secreta.')
	else:
		print(f'A letra "{letra}" NÃO EXISTE na palavra '
			  f'secreta.')
		digitadas.pop()
	secreto_temp = ''
	for letra_secreta in secreto:
		if letra_secreta in digitadas:
			secreto_temp += letra_secreta
		else:
			secreto_temp += '*'
	if secreto_temp == secreto:
		print(f'Parabêns, você ganhou! A palavra '
			  f'é {secreto_temp}.')
		break
	else:
		print(f'A palavra secreta está assim: '
			  f'{secreto_temp}')
	if letra not in secreto:
		chances -= 1
	print(f'Você ainda tem {chances} chances.')
	print('')
