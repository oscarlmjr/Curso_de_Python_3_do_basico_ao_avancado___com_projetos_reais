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
texto = 'Python s2'  # positivos [012345678]
nova_string = texto[0:6:2]
print(nova_string)
nova_string = texto[0::3]
print(nova_string)
nova_string = texto[:]
print(nova_string)
