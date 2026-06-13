t1 = 1, 2, 'a', 'b'
print(t1, type(t1))

t1 = 1,
print(t1, type(t1))

t1 = 1, 2, 3, 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2
n1, n2, n3, *_, n10 = t3
print(n10)

t1 = (1, 2, 'Luiz', 4, 5) * 5
print(t1)

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
print(t1)
t1 = tuple(t1)
print(t1)
