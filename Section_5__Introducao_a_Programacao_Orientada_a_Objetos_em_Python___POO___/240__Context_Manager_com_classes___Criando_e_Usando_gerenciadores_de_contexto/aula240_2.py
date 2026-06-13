class MyContextManager:
	
	def __enter__(self):
		print('ENTER')

	def __exit__(self, class_exception, exception_, traceback_):
		print('EXIT')


instancia = MyContextManager()

with instancia as alguma_coisa:
	print('WITH', alguma_coisa)
