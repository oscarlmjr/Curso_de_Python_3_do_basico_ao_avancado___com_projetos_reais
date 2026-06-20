"""
Formantando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
nome = 'Otávio'
sobrenome = 'Miranda'
nome_formatado = '{1}'.format(nome, sobrenome)
print(nome_formatado)
nome_formatado = '{1:#^30}'.format(nome, sobrenome)
print(nome_formatado)
nome_formatado = '{0:$<10} {1:#^19}'.format(nome, sobrenome)
print(nome_formatado)
