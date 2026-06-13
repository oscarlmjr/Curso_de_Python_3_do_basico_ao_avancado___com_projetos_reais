"""
Faça um programa que peça o primeiro nome do usuário. Se
o nome tiver 4 letras ou menos escreva "Seu nome é
curto"; se tiver entre 5 e 6 letras, escreva "Seu nome
é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite o seu primeiro nome: ')
quant_nome = len(nome)
if nome.isalpha() and quant_nome > 0:
	if quant_nome <= 4:
		print('Seu nome é curto.')
	if 4 < quant_nome < 7:
		print('Seu nome é normal.')
	if quant_nome > 6:
		print('Seu nome é muito grande.')
else:
	print(f'"{nome}" não é nome.')
