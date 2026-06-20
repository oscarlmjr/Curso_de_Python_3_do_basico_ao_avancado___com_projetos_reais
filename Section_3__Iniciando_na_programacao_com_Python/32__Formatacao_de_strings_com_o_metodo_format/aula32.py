a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'a={} b={} c={}'

formato = string.format(a, b, c)

print(formato)

print()

string = 'b={1} a={0} a={0} c={nome3:.2f}'

formato = string.format(a, b, nome3=c)

print(formato)

print()

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)

