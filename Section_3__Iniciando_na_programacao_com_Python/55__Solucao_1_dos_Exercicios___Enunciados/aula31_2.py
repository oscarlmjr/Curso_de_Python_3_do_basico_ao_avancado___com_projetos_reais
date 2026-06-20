"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite as horas com dois dígitos: ')
quant_digito = len(hora)
if hora.isdigit() and quant_digito == 2:
	hora = int(hora)
	if hora <= 11:
		print('Bom dia!')
	if 12 <= hora <= 17:
		print('Boa tarde!')
	if 18 <= hora <= 23:
		print('Boa noite!')
	if hora > 23:
		print(f'"{hora}" não corresponde a hora.')
#  if hora != int:
#  print(f'"{hora}" não corresponde a dois dígitos inteiros')
else:
	print(f'"{hora}" não corresponde a dois dígitos')
