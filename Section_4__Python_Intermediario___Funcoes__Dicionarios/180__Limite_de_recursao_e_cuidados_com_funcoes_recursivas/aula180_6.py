import sys


# sys.setrecursionlimit(1004)


def factorial(n):
	if n <= 1:
		return 1

	return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))
# print(factorial(1000))  # [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
