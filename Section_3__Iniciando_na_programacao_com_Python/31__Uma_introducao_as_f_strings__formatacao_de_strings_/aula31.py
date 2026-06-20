nome = 'Luiz Otávio'
altura = 1.80
altura_2 = 100050.4
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'{nome} tem {altura_2:,.2f} de altura,'
linha_3 = f'pesa {peso} quilos e seu imc é'
linha_4 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987