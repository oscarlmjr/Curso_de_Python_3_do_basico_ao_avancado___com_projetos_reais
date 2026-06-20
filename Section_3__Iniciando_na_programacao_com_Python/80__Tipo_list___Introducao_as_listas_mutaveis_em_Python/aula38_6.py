cont = 0
while cont < 1:
	palavra_secreta = input('Digite uma palavra: ')
	cont = 0
	while cont < 1:
		if len(palavra_secreta) > 1 and palavra_secreta.isalpha():
			palavra_secreta = palavra_secreta.lower()
			chances = len(palavra_secreta)
			asteristico = chances
			secreto_temporario = asteristico * '*'
			novo_secreto_temporario = ''
			print(secreto_temporario)
			letra_temp = input('Digite uma letra: ')
			while chances > 0:
				if len(letra_temp) == 1 and letra_temp.isalpha():
					letra_temp = letra_temp.lower()
					cont = 0
					for n in palavra_secreta:
						if n == letra_temp:
							novo_secreto_temporario += letra_temp
						else:
							novo_secreto_temporario += secreto_temporario[cont]
						cont += 1
					secreto_temporario = novo_secreto_temporario
					novo_secreto_temporario = ''
					if letra_temp not in palavra_secreta:
						chances -= 1
					if secreto_temporario == palavra_secreta:
						print(f'Você acertou! "{palavra_secreta}" é a palavra secreta.')
						break
					if chances > 0:
						print(f'"{secreto_temporario}" você tem {chances} chances.')
					else:
						print(f'"{secreto_temporario}" suas chances acabaram.')
						break
					letra_temp = input('Digite uma letra: ')
					while letra_temp in secreto_temporario:
						print('Você já digitou essa letra.')
						letra_temp = input('Digite outra letra: ')
				else:
					letra_temp = input('Digite apenas uma letra: ')
					while letra_temp in secreto_temporario:
						print('Você já digitou essa letra.')
						letra_temp = input('Digite outra letra: ')
		else:
			palavra_secreta = input('Digite uma palavra: ')
	cont = 0
