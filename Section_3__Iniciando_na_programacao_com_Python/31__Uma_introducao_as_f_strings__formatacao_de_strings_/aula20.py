nome = 'Luiz Otávio'; idade = 32; altura = 1.80; e_maior = idade > 18; peso = 80
imc = peso / (altura**2)
print(nome, 'tem', idade, 'de idade e seu imc é ', imc)
print(f'Luiz Otávio tem 32 de idade e seu imc é 24.69')
print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{2} tem {0} anos de idade e seu imc é {1}'.format(nome, idade, imc))
print('{i} tem {im} anos de idade e seu imc é {n}'.format(n=nome, i=idade, im=imc))
