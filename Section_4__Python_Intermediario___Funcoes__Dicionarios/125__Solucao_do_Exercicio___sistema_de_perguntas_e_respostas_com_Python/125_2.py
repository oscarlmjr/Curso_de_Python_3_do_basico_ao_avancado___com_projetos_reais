print('\nTeste seus conhecimentos: \n')

perguntas = [
	{
		'Pergunta': 'Quanto é 2+2?',
		'Opções': ['1', '3', '4', '5'],
		'Resposta': '4',
	},
	{
		'Pergunta': 'Quanto é 5*5?',
		'Opções': ['25', '55', '10', '51'],
		'Resposta': '25',
	},
	{
		'Pergunta': 'Quanto é 10/2?',
		'Opções': ['4', '5', '2', '1'],
		'Resposta': '5',
	},
]


cont = 0
while cont < len(perguntas):

	print(f"{perguntas[cont]['Pergunta']}\n")

	for n, p in enumerate(perguntas[cont]['Opções']):
		print(f'{n}) {p}')
	print('')

	opcao = input('Escolha uma opção:\n')

	if cont == 0 and opcao == '2':
		print('Acertou')
	elif cont == 1 and opcao == '0':
		print('Acertou')
	elif cont == 2 and opcao == '1':
		print('Acertou')
	else:
		print('Errou')
	print('')	
	cont += 1


# for n in range(perguntas.__len__()):
#	 print(f"Pergunta: {perguntas[n]['Pergunta']}")
#	 print('Opções: ', *perguntas[n]['Opções'], '\n')
#	 resposta = input('Escolha uma opção: ')

#	 if resposta == perguntas[n]['Resposta']: print('Certo\n')
#	 else: print('Errado\n')


# for n in range(perguntas.__len__()):
#	 print(perguntas[n]['Pergunta'], *perguntas[n]['Opções'], sep='\n')
#	 resposta = input('Resposta: ')
#
#	 if resposta == perguntas[n]['Resposta']:
#		 print('Você acertou!\n')
#	 else:
#		 print('Você errou.\n')

