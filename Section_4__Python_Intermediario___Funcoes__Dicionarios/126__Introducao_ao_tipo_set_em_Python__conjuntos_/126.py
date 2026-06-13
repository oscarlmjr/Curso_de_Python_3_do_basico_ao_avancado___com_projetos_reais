# Sets - Conjuntos em Python (tipo set)
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = {}  # dicionário
s1 = set()  # vazio
print(s1, type(s1), '\n')

s1 = set('Luiz')  # só string
print(s1, type(s1), '\n')

s1 = set([1, 2, 3.4])
print(s1, type(s1), '\n')

s1 = {'Luiz'}
print(s1, type(s1), '\n')

s1 = {'Luiz', 1, 2, 3}
print(s1, type(s1), '\n')
