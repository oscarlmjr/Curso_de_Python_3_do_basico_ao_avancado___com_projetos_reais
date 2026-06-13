"""
Operador ternário em Python
"""
logged_user = True
if logged_user:
	msg = 'Usuário logado.'
else:
	msg = 'Usuário precisa logar.'
print(msg)

msg = 'Usuario logado.' if logged_user else 'Usuário precisa logar.'
print(msg)
