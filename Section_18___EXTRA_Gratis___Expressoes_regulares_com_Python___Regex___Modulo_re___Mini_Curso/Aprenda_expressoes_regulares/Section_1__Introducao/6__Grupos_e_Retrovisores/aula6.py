# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação
import re


cpf = '147.852.963-12'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9a-azA-Z.-]+', cpf))
# print(re.findall(r'[0-9^]+', cpf))
# print(re.findall(r'[^a-z]+', cpf))
# print(re.findall(r'[^a-z]', cpf))


# # cpf = 'a 147.852.963-12'
# cpf = '147.852.963-12    qualquer'


# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
