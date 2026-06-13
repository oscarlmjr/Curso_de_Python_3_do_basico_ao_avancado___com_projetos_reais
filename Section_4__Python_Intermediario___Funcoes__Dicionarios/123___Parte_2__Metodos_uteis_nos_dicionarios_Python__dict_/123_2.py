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

p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

p1.update(((((({'nome': 'novo valor', 'idade': 30}))))))
print(p1)
p1.update({'nome': 'novo valor', 'idade': 30})
print(p1, '\n')

p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

p1.update(nome='novo valor', idade=30)
print(p1, '\n')

p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)
print(p1, '\n')

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1, '\n')
