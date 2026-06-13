"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = 'Luiz'
noutra_variavel = nome
nome = 'João'
print(nome)
print(noutra_variavel, '\n')

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
print(lista_b)
lista_a[0] = 'Qualquer coisa'
print(lista_b, '\n')


lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
print(lista_b, '\n')

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
