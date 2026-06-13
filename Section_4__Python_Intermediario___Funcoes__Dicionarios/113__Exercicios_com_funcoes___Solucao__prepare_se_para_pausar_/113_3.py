# def par_impar(numero):
#	 return numero % 2 == 0
#
# print(par_impar(2))
# print(par_impar(3))
# print(par_impar(15))
# print(par_impar(16))


def par_impar(numero):
	multiplo_de_dois = numero % 2 == 0

	if multiplo_de_dois:
		return f'{numero} é par'
	return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)
print(dois_e_par is outro_par_impar)
