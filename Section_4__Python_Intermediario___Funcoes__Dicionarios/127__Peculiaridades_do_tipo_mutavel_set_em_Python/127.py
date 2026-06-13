# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem indexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {2, 3, 3, 1, 3, 3, 1, (1, 3), (3, 1),}
print(s1, '\n')

s1 = {2, 3, 3, 1, 3, 3, 1, (3, 1),}
print(s1, '\n')

l1 = [2, 3, 3, 1, 3, 3, 1]
s1 = set(l1)
print(s1, '\n')

l2 = list(s1)
print(l2, '\n')

print(3 in s1, '\n')

s1 = {1, 2, 3}

for s in s1:
	print(s)
