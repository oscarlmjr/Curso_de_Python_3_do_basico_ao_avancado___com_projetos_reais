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
nome = 'Otávio Miranda'
nome_formatado = '{}'.format(nome)
print(nome_formatado)
nome_formatado = '{:@>30}'.format(nome)
print(nome_formatado)
nome_formatado = '{n}'.format(n=nome)
print(nome_formatado)
nome_formatado = '{n} {n}, {n}{n}'.format(n=nome)
print(nome_formatado)
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)
