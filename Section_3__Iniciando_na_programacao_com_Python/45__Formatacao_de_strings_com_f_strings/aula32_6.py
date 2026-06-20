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
print(nome)
nome = nome.rjust(20, '#')
print(nome)
nome = nome.ljust(20, '#')
print(nome)
nome = 'Luiz Otávio MirANDa'
print(nome)
print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # Primeiras letras maiúsculas
