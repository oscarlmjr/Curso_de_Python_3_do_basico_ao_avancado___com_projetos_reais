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

print(p1['nome'])
print(p1.get('nome', 'Não existe'), '\n')

nome = p1.pop('nome')
print(nome)
print(p1, '\n')

p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1, '\n')

p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}

print(p1.pop)
p1.pop
print(p1, '\n')
