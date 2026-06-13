"""
1 - Crie uma funcao1 que receba uma funcao2 como parâmetro
e retorne o valor da funcao2 executada.
"""

def func():
	return 'func'

def func2(var):
	return var()

var = func2(func)
print(var)


# def func(*args):
#	 print(*args)
#
# def func2(*args):
#	 return func(*args)
#
# func2(1, 2)

# def func(*args):
#	 print(*args)
#
# def func2():
#	 func(1, 2)
#	 return func()
#
# func2()

# def func():
#	 print('func()')
#
# def func2():
#	 return func()
#
# func2()

# def func(*args):
#	 print(*args)
#
# func(1, 2)
