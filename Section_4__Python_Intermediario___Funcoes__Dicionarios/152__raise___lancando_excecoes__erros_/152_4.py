
def divide(n, d):
	try:
		return n / d
	except ZeroDivisionError:
		print('____')
		raise


print(divide(8, 0))
