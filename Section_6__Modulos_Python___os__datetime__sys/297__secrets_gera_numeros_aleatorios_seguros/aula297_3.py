# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr


print()
print(s.ascii_letters)
print(s.digits)
print(s.punctuation, '\n')
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)), '\n')

# python -c "import string as s;from secrets import SystemRandom as Sr; print(
# ''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
