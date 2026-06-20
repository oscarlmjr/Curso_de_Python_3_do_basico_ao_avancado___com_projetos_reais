"""
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação
apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa
noite 18-23.
"""
hora = input('Digite uma hora entre 00 e 23 horas: ')

if hora.isdigit():
	hora = int(hora)
	if 0 <= hora and hora <= 23:
		if 0 <= hora and hora <= 11:
			print('Bom dia!')
		if 12 <= hora and hora <= 17:
			print('Boa tarde!')
		if 18 <= hora and hora <= 23:
			print('Boa noite!')
else:
	print('Digite a hora entre 00 e 23 horas: ')


	nome = input('Digite o seu primeiro nome: ')
	letras = len(nome)
	if nome.isalpha() and not letras == 0:
		if letras <= 4:
			print('Seu nome é curto.')
		elif letras <= 6:
			print('Seu nome é normal.')
		elif letras > 6:
			print('Seu nome é muito grande')
	else:
		print('Digite um nome próprio.')
