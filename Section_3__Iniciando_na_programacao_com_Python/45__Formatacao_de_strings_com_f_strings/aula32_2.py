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
nome = 'Luiz Otávio'
print(f'{nome:s}')
num_1 = 1
print(f'{num_1:0>10}')
num_2 = 1150
print(f'{num_2:0<10}')
num_2 = 1150
print(f'{num_2:0^10}')
num_2 = 1150
print(f'{num_2:.2f}')
num_2 = 1150
print(f'{num_2:0>10.2f}')
