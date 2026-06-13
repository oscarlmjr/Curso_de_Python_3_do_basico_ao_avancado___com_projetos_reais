"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:

	opcao = input('\nSelecione uma opção\n[i]nserir [a]pagar [l]istar: ')

	if opcao == 'i':
		inserir = input('Insira um produto: ')
		lista.append(inserir)
		print(*lista)

	elif opcao == 'l':
		for n, p in enumerate(lista, 1):
			print(n, p)
			if n % 3 == 0 and n > 3:
				enter = input('Tecle Enter para continuar\n')
				if enter == '':
					continue
				else:
					print('Sair da lista')
					break

	elif opcao == 'a':
		print('Escolha uma opção para apagar: \n')

		for n, p in enumerate(lista, 1):
			print(n, p)
			if n % 3 == 0 and n > 3:
				enter = input('Continuar [s]im\n')
				if enter == 's':
					continue
				else:
					print('Sair da lista')
					break		
		while True:
			apagar = int(input(': '))
			if apagar > len(lista):
				print('Digite uma opção da lista:')
				continue
			else:
				del lista[apagar - 1]
				break
			

