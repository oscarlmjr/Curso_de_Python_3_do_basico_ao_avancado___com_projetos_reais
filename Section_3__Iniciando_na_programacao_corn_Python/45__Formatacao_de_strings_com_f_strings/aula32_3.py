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
print(len(nome))
print(50-len(nome))
print((50-len(nome)) / 2)
print(f'{nome:0^19}')
print(f'{nome:#^30}')
print(len('##################'))
