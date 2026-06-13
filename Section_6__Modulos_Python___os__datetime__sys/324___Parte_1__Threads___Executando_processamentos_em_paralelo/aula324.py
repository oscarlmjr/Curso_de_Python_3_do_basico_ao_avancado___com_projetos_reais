# (Parte 1) Threads - Executando processamentos em paralelo
from time import sleep


print('Hello')

for i in range(10):
    print(i)
    sleep(.5)

print('World!')
