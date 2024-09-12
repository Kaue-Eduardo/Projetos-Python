# Vão ser lidos 6 números inteiros, os pares serão somados

# Iniciando a variável pra receber o valor da soma dos números
soma = 0

# Laço que irá receber os 6 números inteiros
for i in range(0, 6):

    # Entrada do valor inteiro
    num = int(input('Digite o {}º número inteiro: '.format(i + 1)))

    # Verifica se o número é par ou ímpar, se for par ele passa para a soma
    if num % 2 == 0:
        soma += num

print('A soma dos valores pares é: {}'.format(soma))
