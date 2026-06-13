"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'Luiz'.__iter__()  # iterável
print(texto)

texto = iter('Luiz')
print(texto)

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())   # StopIteration
