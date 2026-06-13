class MeuError(Exception):
	...


def levantar():
	raise MeuError('A mensagem do meu erro')


try:
	levantar()
	
except MeuError as error:
	print(error)
	...
