# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy
from aula161_package import produtos, ordena


produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda item: item['nome'])
print(produtos, '\n')
print(produtos_ordenados_por_preco, '\n')


produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=ordena)
print(produtos, '\n')
print(produtos_ordenados_por_preco)
