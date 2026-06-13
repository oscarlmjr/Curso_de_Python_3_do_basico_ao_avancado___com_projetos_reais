def func(*args):
	args = list(args)
	print(args)
	print(*args)
func('12345')

def func(*args):
	args = (args)
	print(args)
	print(*args)
func('12345')

# a = 1, 2, 3, 4, 5
# a = [1, 2, 3, 4, 5]
# a = '1', '2', '3', '4', '5'
# b = ''
# for n in range(len(a)):
#	 b += str(a[n])
#	 print(b)

# a = '12345'
# a = [a]
# print(f'{a}\n')
#
# a = '1', '2', '3', '4', '5'
# b = '12345'
# print(f'{a}\n{b}')
# print(a == b)
# print(f'{list(a)}\n{list(b)}')
# print(list(a) == list(b))
