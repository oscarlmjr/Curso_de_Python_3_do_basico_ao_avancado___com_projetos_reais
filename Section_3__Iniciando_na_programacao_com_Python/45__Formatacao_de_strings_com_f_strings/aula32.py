# Formantando valores com modificadores
# :s - Texto (strings)
# :d - Inteiros (int)
# :f - Números de ponto flutuante (float)
# :.(NÚMERO)f - Quantidade de casas decimais (float)
# :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
# > - Esquerda
# < - Direita
# ^ - Centro
num1 = 10
num2 = 3
divisao = num1 / num2
divisao_int = num1 // num2
print(divisao)
print(divisao_int)
print('{}'.format(divisao))
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
