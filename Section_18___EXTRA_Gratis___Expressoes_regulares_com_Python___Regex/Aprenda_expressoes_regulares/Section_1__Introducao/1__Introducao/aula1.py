import re

# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
# print(re.findall(r'teste2', string))
print(re.sub(r'teste', 'ABCD', string))
# print(re.sub(r'teste', 'ABCD', string, count=1))
# print(re.sub(r'teste', 'ABCD', string, count=0))
# print(re.sub(r'Teste', 'ABCD', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
