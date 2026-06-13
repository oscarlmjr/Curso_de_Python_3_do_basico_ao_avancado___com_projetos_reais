"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista

print(lista)
print(n1, n2, n)
print(*lista)
print(*lista, sep='-')
