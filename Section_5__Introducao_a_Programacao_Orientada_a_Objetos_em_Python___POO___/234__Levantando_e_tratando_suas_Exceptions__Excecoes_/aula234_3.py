class MeuError(Exception):
	...


def levantar():
	exception_ = MeuError('a', 'b', 'c')
	# exception_ = MeuError('abc')
	raise exception_


try:
	levantar()
	
except MeuError as error:
	print(error)
	print(error.args)
	