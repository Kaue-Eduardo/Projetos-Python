# O programa irá gerar 5 números aleatórios, criar uma tupla com eles
# e depois mostrar o maior e o menor

# Importando biblioteca para gerar os números
from random import randint

# Estrutura que vai receber os números aleatórios
tupla = []

# Laço para criar um novo número a cada iteração
for i in range(0, 5):
    # Estrutura para criar um novo número a cada iteração
    aleatorio = randint(0, 1000)
    # Adicionando cada número gerado à lista
    tupla.append(aleatorio)

# Transformando a lista em tupla
tupla = tuple(tupla)
print(tupla)

# Maior número da tupla
print(f'O maior número gerado na tupla é: {max(tupla)}')

# Menor número da tupla
print(f'O menor número gerado na tupla é: {min(tupla)}')
