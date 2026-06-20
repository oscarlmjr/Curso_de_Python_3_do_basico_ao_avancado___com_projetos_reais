x = 10
y = 'Luiz'
z = 'Otavio'
x = z  # variáveis na vertical
y = x
z = y
print(f'x={x} e y={y} e z={z}')

# necessário repetir as variáveis
x = 10
y = 'Luiz'
z = 'Otavio'
x, y, z = z, x, y  # variáveis na horizontal
print(f'x={x} e y={y} e z={z}')
