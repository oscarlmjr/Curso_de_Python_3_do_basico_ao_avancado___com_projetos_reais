# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
print(a, b, '\n')
a, b = b, a
print(a, b, '\n')

pessoa = {'nome': 'Aline', 'sobrenome': 'Souza'}
print(pessoa, '\n')

a = pessoa
print(*a, '\n')

a, b = pessoa
print(a)
print(f'a = {a}, b = {b}', '\n')

a, b = pessoa.items()
print(f'a = {a}, b = {b}')
print(*a, *b, '\n')

print(*a, *b, sep='\n')
print()

(a1, a2), b = pessoa.items()
print(a1, a2)
print(b)
