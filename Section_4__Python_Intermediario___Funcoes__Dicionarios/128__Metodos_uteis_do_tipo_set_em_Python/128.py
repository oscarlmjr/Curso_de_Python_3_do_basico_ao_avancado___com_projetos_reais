# Métodos úteis:
# add, update, clear, discard

s1 = ('Luiz', 1, 2, 3)
print(s1, type(s1), '\n')

s1 = set('Luiz',)
print(s1, type(s1), '\n')

# s1.add('Luiz', 2, 3, 1)  # só aceita um elemento
s1.add('Luiz')  # só aceita um elemento
print(s1, '\n')

# s1.update(2, 3, 1)   # não aceita int
s1.update('OLÁ MUNDO')
print(s1, '\n')

s1.discard('OLÁ MUNDO')   # não exclui caracteres fatiados
print(s1, '\n')

s1.update(['Olá mundo', 2, 3, 1])   # encapsulado
print(s1, '\n')

s1.update(('Olá mundo', 2, 3, 1))   # encapsulado
print(s1, '\n')

s1.discard('Olá mundo')
print(s1, '\n')

s1.clear()
print(s1)
