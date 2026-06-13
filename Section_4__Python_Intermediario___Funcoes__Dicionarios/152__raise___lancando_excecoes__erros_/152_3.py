
def divide(n, d):
	try:
		return n / d
	except ZeroDivisionError:
		raise


print(divide(8, 0))


# def divide(n, d):
#		 return n / d
#
#
# print(divide(8, 0))
