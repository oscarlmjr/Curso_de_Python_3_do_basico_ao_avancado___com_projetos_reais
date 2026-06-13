# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json


try:
	with open('aula193_2.json', 'r', encoding='utf8') as arquivo:
		print('lista_json try:')
		lista_json = json.load(arquivo)

except:		
	   
	lista_json = [[], [], []]   # lista_json = [tarefas, refazer, lista] 
	
	with open('aula193_2.json', 'w+', encoding='utf8') as arquivo:
		print('lista_json except:')
		json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)


while True:	

	tarefa = input('Digite uma tarefa: \n')

	def acao(tarefa):

		if tarefa == 'listar':
			if lista_json[2] == []:
				return print('Você não tem tarefas a listar.')
			print('Lista:')
			print(*[l for l in lista_json[2]], sep='\n')
			return
		
		elif tarefa == 'desfazer':
			if lista_json[2] == []:
				return print('Você não tem tarefas a desfazer.')
			lista_json[1].append(lista_json[2][-1])
			print(lista_json[1])
			lista_json[2] = lista_json[2][:-1]
			print(lista_json[2])
			return

		elif tarefa == 'refazer':
			if lista_json[1] == []:
				return print('Você não tem tarefas a refazer.')
			lista_json[2].append(lista_json[1][0])
			lista_json[1].pop(0)
			return

		lista_json[0].append(tarefa)
		lista_json[2].append(lista_json[0][-1])

	acao(tarefa)

	with open('aula193_2.json', 'w+', encoding='utf8') as arquivo:
		json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)



#########################
# import json


# try:
#	 with open('aula193_2.json', 'r', encoding='utf8') as arquivo:
#		 print('lista_json try:')
#		 lista_json = json.load(arquivo)

# except:	
#	 tarefas = []
#	 refazer = []
#	 lista = []
#	 lista_json = [tarefas, refazer, lista]	
	
#	 with open('aula193_2.json', 'w+', encoding='utf8') as arquivo:
#		 print('lista_json except:')
#		 json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)


# while True:	

#	 tarefa = input('Digite uma tarefa: \n')

#	 def acao(tarefa):
#		 global lista

#		 if tarefa == 'listar':
#			 if lista == []:
#				 return print('Você não tem tarefas a listar.')
#			 print('Lista:')
#			 print(*[l for l in lista], sep='\n')
#			 return
		
#		 elif tarefa == 'desfazer':
#			 if lista == []:
#				 return print('Você não tem tarefas a desfazer.')
#			 refazer.append(lista[-1])
#			 print(refazer)
#			 lista = lista[:-1]
#			 print(lista)
#			 return

#		 elif tarefa == 'refazer':
#			 if refazer == []:
#				 return print('Você não tem tarefas a refazer.')
#			 lista.append(refazer[0])
#			 refazer.pop(0)
#			 return

#		 tarefas.append(tarefa)
#		 lista.append(tarefas)

#	 acao(tarefa)

#	 lista_json = [tarefas, refazer, lista]

#	 with open('aula193_2.json', 'w+', encoding='utf8') as arquivo:
#		 json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)


########################


# refaz = []
# lista = []

# def acao(t):
#	 lista.append(t)   
#	 return

# def listar():
#	 print('Lista:')
#	 if lista == []:
#		 return print('Você não tem tarefas a listar.')
#	 print(*[l for l in lista], sep='\n')
#	 # print(*lista)
#	 return

# def desfazer():   
#	 global lista
#	 if lista == []:
#		 return print('Você não tem tarefas a desfazer.')
#	 refaz.append(lista[-1])
#	 lista = lista[:-1]
#	 return

# def refazer():
#	 if refaz == []:
#		 return print('Você não tem tarefas a refazer.')
#	 lista.append(refaz[0])
#	 refaz.pop(0)
#	 return

# tarefas = [
#	 'a', 'b', 'c', 'listar', 'desfazer', 'listar', 'desfazer', 
#	 'listar', 'desfazer', 'listar', 'desfazer', 'listar', 'refazer', 
#	 'listar', 'refazer', 'listar', 'refazer', 'listar', 'refazer', 'listar'
#	 ]

# for t in tarefas:
#	 if t == 'listar':
#		 listar()
#	 elif t == 'desfazer':
#		 desfazer()
#	 elif t == 'refazer':
#		 refazer()
#	 else:
#		 acao(t)

########################

# tarefas = []
# refazer = []
# lista = []

# while True:

#	 tarefa = input('Digite uma tarefa: \n')

#	 def acao(tarefa):
#		 global lista

#		 if tarefa == 'listar':
#			 if lista == []:
#				 return print('Você não tem tarefas a listar.')
#			 print('Lista:')
#			 print(*[l for l in lista], sep='\n')
#			 return
		
#		 elif tarefa == 'desfazer':
#			 if lista == []:
#				 return print('Você não tem tarefas a desfazer.')
#			 refazer.append(lista[-1])
#			 print(refazer)
#			 lista = lista[:-1]
#			 print(lista)
#			 return

#		 elif tarefa == 'refazer':
#			 if refazer == []:
#				 return print('Você não tem tarefas a refazer.')
#			 lista.append(refazer[0])
#			 refazer.pop(0)
#			 return

#		 tarefas.append(tarefa)
#		 lista = copy.deepcopy(tarefas)


#	 acao(tarefa)
