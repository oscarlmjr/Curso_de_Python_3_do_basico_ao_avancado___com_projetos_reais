# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy
from aula161_package import produtos


novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
	{**produto, 'preco': round(produto['preco'] * 1.1, 2)}
	  for produto in produtos
]

print(produtos, '\n')
print(novos_produtos)


# import copy
#
#
# novos_produtos = copy.deepcopy(produtos)
# novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2)} for produto in novos_produtos]
#
# # produtos_ordenados_por_nome = sorted(produtos, key=lambda item: item['nome'], reverse=True)
#
# produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
# produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)
#
# produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome)
# produtos_ordenados_por_preco.sort(key=lambda item: item['preco'], reverse=True)
# print(produtos_ordenados_por_preco, '\n')
# print(produtos)
