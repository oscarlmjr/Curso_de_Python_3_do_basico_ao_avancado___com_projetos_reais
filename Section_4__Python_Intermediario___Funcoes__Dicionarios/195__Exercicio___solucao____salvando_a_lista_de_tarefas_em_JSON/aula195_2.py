import json


try:
	with open('aula195_2.json', 'r', encoding='utf8') as arquivo:
		listas = json.load(arquivo)
		lista = listas[0]
		lista_refazer = listas[1]

except FileNotFoundError:
	lista = []
	lista_refazer = []
	listas = [lista, lista_refazer]
	with open('aula195_2.json', 'w', encoding='utf8') as arquivo:
		json.dump(listas, arquivo, ensure_ascii=False, indent=2)


def comeco(lista, lista_refazer):
	with open('aula195_2.json', 'w', encoding='utf8') as arquivo:
		json.dump(listas, arquivo, ensure_ascii=False, indent=2)

	return lista


while True:

	def listar(lista, lista_refazer, acao):
		if acao == 'listar':
			lista.pop()
			if lista == []:
				print('Não há ações à listar.')
			return comeco(lista, lista_refazer)

		elif acao == 'desfazer':
			lista.pop()
			if lista == []:
				print('Não há ações à desfazer.')
				return comeco(lista, lista_refazer)
			lista_refazer.append(lista[-1])
			lista.pop()
			return comeco(lista, lista_refazer)

		elif acao == 'refazer':
			lista.pop()
			if lista_refazer == []:
				print('Não há ações à refazer.')
				return comeco(lista, lista_refazer)
			lista.append(lista_refazer[0])
			lista_refazer.pop(0)
			return comeco(lista, lista_refazer)

		elif acao == 'apagar':
			lista.pop()
			if lista == []:
				print('Não há ações a apagar.')
				return comeco(lista, lista_refazer)
			lista.pop()
			return comeco(lista, lista_refazer)

		return comeco(lista, lista_refazer)


	acao = input('Digite uma ação: ')

	lista.append(acao)
	variavel = listar(lista, lista_refazer, acao)
	print('LISTA:', *variavel, sep='\n')
