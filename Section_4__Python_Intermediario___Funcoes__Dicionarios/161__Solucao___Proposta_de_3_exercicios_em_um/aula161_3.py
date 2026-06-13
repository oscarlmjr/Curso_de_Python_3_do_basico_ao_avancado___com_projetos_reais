# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

import copy
from aula161_package import produtos, ordena


produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda item:
item['nome'], reverse=True)
print(*produtos, '\n')
print(*produtos_ordenados_por_nome, '\n')


produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=ordena, reverse=True)
print(*produtos, '\n')
print(*produtos_ordenados_por_nome)
