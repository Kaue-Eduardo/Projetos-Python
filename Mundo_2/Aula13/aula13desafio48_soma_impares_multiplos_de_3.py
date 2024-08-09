# Somando todos os número ímpares e múltiplos de 3 no intervalo de 1 a 500

soma = 0

# Laço de repetição de 1 a 500
for i in range(1, 500):
    if i % 2 != 0:
        # Condição, múltiplo de 3
        if i % 3 == 0:
            # Somando os valores
            soma += i

# Imprime o resultado da soma
print('A soma de todos os números ímpares entre 1 e 500 é: {}'.format(soma))
