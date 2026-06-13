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

pessoa = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}

print(pessoa.__len__())
print(len(pessoa), '\n')

print(pessoa.keys())
print(*pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()), '\n')

print(list(pessoa.values()), '\n')

print(list(pessoa.items()), '\n')

pessoa.setdefault('idade', None)
print(pessoa['idade'])
