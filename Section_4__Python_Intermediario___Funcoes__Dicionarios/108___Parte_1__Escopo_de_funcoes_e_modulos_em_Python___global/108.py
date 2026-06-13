'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
'''

def escopo():
	x = 1
	print(x)


# print(x)   # NameError: name 'x' is not defined
escopo()
