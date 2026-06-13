"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
	- Se a letra digitada estiver na
	palavra secreta; exiba a letra;
	- Se a letra digitada não estiver
	na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = input('Digite uma palavra-secreta: ')

palavra_oculta = ''
palavra_oculta_erro = ''
letra_oculta_acerto = ''
contador = 0

while True:

	letra = input('Digite uma letra: ')

	if letra in palavra_secreta:
		if palavra_oculta == '':
			for n in palavra_secreta:
				if n == letra:
					palavra_oculta += letra
				else:
					palavra_oculta += '*'
		else:
			for l in palavra_secreta:
				if l == letra:
					letra_oculta_acerto += l
				elif l in palavra_oculta:
					letra_oculta_acerto += l				
				else:
					letra_oculta_acerto += '*'

			palavra_oculta = letra_oculta_acerto
			letra_oculta_acerto = ''

		if palavra_secreta == palavra_oculta: 
			os.system('cls')   
			print(f'Parabéns, você acertou: palavra-secreta = {palavra_oculta}')
			break
		else:			
			print(f'Você tem {len(palavra_secreta) - contador} chances.')
			print(f'Palavra-secreta = {palavra_oculta}')

	else:
		contador += 1
		if contador == len(palavra_secreta):
			print(f'Suas chances acabaram. A palavra-secreta é "{palavra_secreta}"')
		elif len(palavra_secreta) == len(palavra_oculta):			
			print(f'Você tem {len(palavra_secreta) - contador} chances.')
			print(f'Palavra-secreta = {palavra_oculta}')
		else:
			for p in palavra_secreta:
				palavra_oculta += '*'			
			print(f'Você tem {len(palavra_secreta) - contador} chances.')				
			print(f'Palavra-secreta_ = {palavra_oculta}')	
