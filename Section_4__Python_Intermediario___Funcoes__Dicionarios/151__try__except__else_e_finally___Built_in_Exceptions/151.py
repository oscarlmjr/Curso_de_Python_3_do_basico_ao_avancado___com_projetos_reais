# (Parte 3) try, Except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
	print('Abrir arquivo', '\n')
	8 / 0

except ZeroDivisionError as e:
	print(e.__class__.__name__)
	print(e)
	print('divisão por zero\n')

except IndexError as error:
	print('IndexError')
except (NameError, ImportError):
	print('NameError, ImportError')

else:
	print('Não deu erro')

finally:
	print('Fechar arquivo')
