import os


lista_acao = []
lista = []
refazer = []

while True:

	print('\nTarefa ou comando:\nlistar, desfazer, refazer')
	acao = input('Digite uma tarefa ou comando: ')

	if acao == ' ' or acao == '':
		continue
	# if acao == 'clear':
	#	 os.system('clear')
	#	 continue

	if acao == 'desfazer':
		if len(lista_acao) == 0:
			print('Não há tarefas para desfazer na lista.')
			continue
		print(f'{lista_acao[-1]} foi removida de suas tarefas.\n')
		refazer.extend([lista_acao[-1]])
		lista_acao = lista_acao[:-1]
		if len(lista_acao) == 0:
			print('TAREFAS:')
			continue
		print('TAREFAS:', *lista_acao, sep='\n')

	elif acao == 'refazer':
		if len(refazer) == 0:
			print('Não há tarefas para refazer.')
			continue
		lista_acao.extend([refazer[0]])
		print(f'{lista_acao[-1]} foi restaurada a suas tarefas.\n')
		print('TAREFAS:', *lista_acao, sep='\n')
		refazer.pop(0)

	elif acao == 'listar':
		if len(lista_acao) == 0:
			print('Não há tarefas na lista.')
			continue
		print('TAREFAS:', *lista_acao, sep='\n')

	else:
		print(f'{acao} foi adicinada a suas tarefas.')
		lista_acao += [acao]
		lista += [acao]


# lista = []
# lista_refazer = []
#
# while True:
#
#	 acao = input('Digite uma ação: ')
#	 lista.append(acao)
#
#	 if acao == 'listar':
#		 lista.pop()
#		 if lista == []:
#			 print('Não há ações à listar.')
#
#	 elif acao == 'refazer':
#		 lista.pop()
#		 if lista_refazer == []:
#			 print('Não há ações à refazer.')
#			 print(f'LISTA:', *lista, sep='\n')
#			 continue
#		 lista.append(lista_refazer[0])
#		 lista_refazer.pop(0)
#
#	 elif acao == 'desfazer':
#		 lista.pop()
#		 if lista == []:
#			 print('Não há ações à desfazer.')
#			 print(f'LISTA:', *lista, sep='\n')
#			 continue
#		 lista_refazer.append(lista[-1])
#		 lista = lista[:-1]
#
#	 # print(f'LISTA:\n{*lista}', sep='\n')   # SyntaxError: f-string: cannot use starred expression here
#	 print(f'LISTA:', *lista, sep='\n')


# lista = []
# lista_refazer = []
#
# while True:
#
#	 def listar(lista, lista_refazer, acao):
#		 if acao == 'listar':   # is not None
#			 def listar_acao(lista):
#				 lista.pop()
#				 if lista == []:
#					 print('Não há ações à listar.')
#				 return listar(lista, lista_refazer, acao=None)
#			 return listar_acao(lista)
#
#		 elif acao == 'desfazer':
#			 def desfazer(lista, lista_refazer):
#				 lista.pop()
#				 if lista == []:
#					 print('Não há ações à desfazer.')
#					 return listar(lista, lista_refazer, acao=None)
#				 lista_refazer.append(lista[-1])
#				 # lista = lista[:-1]
#				 lista.pop()
#				 return listar(lista, lista_refazer, acao=None)
#			 return desfazer(lista, lista_refazer)
#
#		 elif acao == 'refazer':
#			 def refazer(lista, lista_refazer):
#				 lista.pop()
#				 if lista_refazer == []:
#					 print('Não há ações à refazer.')
#					 return listar(lista, lista_refazer, acao=None)
#				 lista.append(lista_refazer[0])
#				 lista_refazer.pop(0)
#				 return listar(lista, lista_refazer, acao=None)
#			 return refazer(lista, lista_refazer)
#
#		 return print(f'LISTA-:', *lista, sep='\n')
#
#	 acao = input('Digite uma ação: ')
#	 lista.append(acao)
#
#	 listar(lista, lista_refazer, acao)

