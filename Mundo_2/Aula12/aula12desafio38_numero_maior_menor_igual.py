# Define se dois números são iguais, se não forem define o maior e o menor número

# Entrada dos números
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

# Condições
if n1 > n2:
    print('O primeiro número "{}" é maior que o segundo "{}"'.format(n1, n2))
elif n2 > n1:
    print('O segundo número "{}" é maior que o primeiro "{}"'.format(n2, n1))
elif n1 == n2:
    print('Os números digitados são iguais!')
