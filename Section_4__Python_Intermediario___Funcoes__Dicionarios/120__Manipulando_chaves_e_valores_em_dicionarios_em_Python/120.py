pessoa = {}
pessoa['nome'] = 'Luiz Otávio'
print(pessoa)
print(pessoa['nome'], '\n')

chave = 'sobrenome'
pessoa[chave] = 'Miranda'
print(pessoa)
print(pessoa[chave], '\n')

del pessoa[chave]
print(pessoa, '\n')

pessoa['sobrenome'] = 'Miranda'
chave = pessoa['sobrenome']
print(chave, '\n')

del chave   # del não se aplica a variavel e não retorna erro
print(pessoa, '\n')

del pessoa['sobrenome']
print(pessoa.get('sobrenome'))
print(pessoa.get('sobrenome', 'Não existe.'))
