secreto = 'python'
secreto_temporario = ''
digitadas = ['t', 'o', 'y', 'h', 'p']
for letra_secreta in secreto:
	print(f'Iteração para a letra {letra_secreta}')
	if letra_secreta in digitadas:
		print(f'Eba! A letra que eu queria {letra_secreta}')
		secreto_temporario += letra_secreta
	else:
		print(f'Essa letra eu não queria {letra_secreta}')
		secreto_temporario += '*'
	print('secreto_temporario=', secreto_temporario)
print(secreto_temporario)
if secreto == secreto_temporario:
	print('Você ganhou!')
