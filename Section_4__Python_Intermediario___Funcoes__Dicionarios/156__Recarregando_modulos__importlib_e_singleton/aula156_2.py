import importlib
import aula156_m


print(aula156_m.variavel)


for i in range(7):
	importlib.reload(aula156_m)
	print(i)

print('Fim')
