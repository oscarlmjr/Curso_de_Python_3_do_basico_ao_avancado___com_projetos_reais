"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funcões podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
#	   [012345678]
texto = 'Python s2'
#	  -[987654321]
print(len(texto))
print(texto[2])
url = 'www.google.com.br/'
print(url[:-1])
nova_string = texto[2:8]
print(nova_string)
nova_string = texto[:6]
print(nova_string)
print(texto[-9])  # negativos -[987654321]
nova_string = texto[-9:-6]
print(nova_string)
