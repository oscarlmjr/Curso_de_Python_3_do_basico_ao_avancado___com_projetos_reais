"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings
(com as chaves)
"""
nome = 'Oscar Mendes'; idade = 44; altura = 1.80; peso = 80.0; ano_atual = 2022
ano_nasc = ano_atual - idade; IMC = peso / altura ** 2
print('{} tem {} anos de idade, {}m de altura e pesa {}Kg.'.format(nome, idade, altura, peso))
print('Nasceu em {} e seu IMC é {}.'.format(ano_nasc, IMC))
print(f'{nome} tem {idade} anos de idade, {altura}m de altura e pesa {peso}Kg.')
print(f'Nasceu em {ano_nasc} e seu IMC é {IMC:.2f}')
