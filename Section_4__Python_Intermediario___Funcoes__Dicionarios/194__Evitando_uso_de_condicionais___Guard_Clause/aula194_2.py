import json, os


try:
	with open('aula194_2.json', 'r', encoding='utf8') as arquivo:
		print('lista_json try:')
		lista_json = json.load(arquivo)

except:		
	   
	lista_json = [[], [], []]   # lista_json = [tarefas, refazer, lista] 
	
	with open('aula194_2.json', 'w+', encoding='utf8') as arquivo:
		print('lista_json except:')
		json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)


while True:	

	tarefa = input('Digite uma tarefa: \n')

	def acao(tarefa, lista_json):

		lista_json[0].append(tarefa)
		lista_json[2].append(lista_json[0][-1])

	def listar(lista_json):
		if lista_json[2] == []:
			return print('Você não tem tarefas a listar.')
		print('Lista:')
		print(*[l for l in lista_json[2]], sep='\n')
		return
		
	def desfazer(lista_json):
		if lista_json[2] == []:
			return print('Você não tem tarefas a desfazer.')
		lista_json[1].append(lista_json[2][-1])
		print(lista_json[1])
		lista_json[2] = lista_json[2][:-1]
		print(lista_json[2])
		return

	def refazer(lista_json):
		if lista_json[1] == []:
			return print('Você não tem tarefas a refazer.')
		lista_json[2].append(lista_json[1][0])
		lista_json[1].pop(0)
		return

	def clear(tarefa):
		os.system(tarefa)   # 'clear'
		return

	tarefas = {'listar': lambda: listar(lista_json), 'desfazer': lambda: desfazer(lista_json), 
			   'refazer': lambda: refazer(lista_json), 'clear': lambda: clear(tarefa)}
	if tarefa in tarefas:
	  tarefas[tarefa]()
	else:
	  acao(tarefa, lista_json)

	with open('aula194_2.json', 'w+', encoding='utf8') as arquivo:
		json.dump(lista_json, arquivo, ensure_ascii=False, indent=2)