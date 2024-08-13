# O programa vai ler vários números até que o usuário digite '999' e no fim vai mostrar quantos números foram digitados
# e a soma desses números

# Variáveis de controle
num = 0
soma = 0
quantidade_numeros = 0

# Laço de repetição
while num != 999:
    # Entrada dos valores
    num = int(input('Digite um número para somar ou 999 para parar: '))

    # Condição que impossibilita que a condição de parada (número 999) seja somado ao restante
    if num != 999:
        # Variável que armazena a soma dos números digitados
        soma += num
        # Variável que armazena quantos números foram digitados
        quantidade_numeros += 1

# Mostrando os resultados
print('\nForam digitados {} números!'.format(quantidade_numeros))
print('A soma dos números digitados é: {}'.format(soma))
