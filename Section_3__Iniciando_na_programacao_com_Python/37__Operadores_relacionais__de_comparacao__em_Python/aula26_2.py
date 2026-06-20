"""
Operadores Lógicos
and, or, not, in e not in
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')
usuario_bd = 'luiz'
senha_bd = '123456'
if usuario_bd == usuario and senha_bd == senha:
	print('Você está logado no sistema')
else:
	print('Usuário ou senha inválidos.')
