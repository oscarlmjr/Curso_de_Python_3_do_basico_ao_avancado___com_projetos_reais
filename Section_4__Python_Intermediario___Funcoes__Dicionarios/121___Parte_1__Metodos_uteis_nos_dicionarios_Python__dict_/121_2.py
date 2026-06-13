# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
	'nome': 'Luiz Otávio', 
	'sobrenome': 'Miranda1',
	'sobrenome': 'Miranda2',
	'sobrenome': 'Miranda3',
	}

print(len(pessoa))
print(pessoa['sobrenome'], '\n')


for chave in pessoa:
	print(chave)

print('')

for chave, valor in pessoa.items():
	print(chave, valor)

print('')

pessoa = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 900}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
