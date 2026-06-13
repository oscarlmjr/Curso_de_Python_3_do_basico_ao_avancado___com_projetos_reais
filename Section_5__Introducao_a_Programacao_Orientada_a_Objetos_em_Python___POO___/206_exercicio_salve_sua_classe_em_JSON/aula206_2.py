# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula206 import CAMINHO_ARQUIVO, SiteQat, fazer_dump


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
	q1__dict__ = list(json.load(arquivo))
	q1 = SiteQat(**q1__dict__[0])

	print(q1.site)
	print(q1__dict__)
