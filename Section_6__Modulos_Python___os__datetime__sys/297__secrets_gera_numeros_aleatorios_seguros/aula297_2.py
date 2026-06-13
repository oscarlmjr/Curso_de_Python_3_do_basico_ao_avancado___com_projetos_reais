# secrets gera números aleatórios seguros
import secrets


print(secrets.randbelow(100))
print(secrets.choice([10, 11, 12]))


random = secrets.SystemRandom()

# Funções:
# seed
#   -> NÃO FAZ NADA
random.seed(10)


# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
