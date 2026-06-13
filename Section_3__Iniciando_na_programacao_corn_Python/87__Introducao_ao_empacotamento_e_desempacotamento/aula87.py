"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome1, nome2, nome3, '\n')

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _, '\n')

_, _, nome, *resto = ['Maria', 'Helena', 'Joana', 'Luiz', 'Otávio']
print(_,)
print(_,)
print(nome)
print(*resto)
