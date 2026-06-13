class MyContextManager:

	def __init__(self):
		print('INIT')
	
	def __enter__(self):
		print('ENTER')
		return 1234

	def __exit__(self, class_exception, exception_, traceback_):
		print('EXIT')


# instancia = MyContextManager()

with MyContextManager() as alguma_coisa:
	print('WITH', alguma_coisa)
