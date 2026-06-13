# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


CAMINHO_ARQUIVO = 'aula206.json'

class SiteQat():

	def __init__(self, site):
		self.site = site

# dados = {'site': 'qat.com'}
# q1 = Qat(**dados)
# print(vars(q1))

q1 = SiteQat('qat.com')
bd = [q1.__dict__]
# print(q1.site)
# print(q1.__dict__)
# print(vars(q1))

def fazer_dump():

	with open(CAMINHO_ARQUIVO, 'w+', encoding='utf8') as arquivo:
		json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
	fazer_dump()
