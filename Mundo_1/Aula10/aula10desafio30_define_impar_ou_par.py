# Define se um número é ímpar o par

# Recebe o número
num = int(input('Digite um número inteiro: '))

# Se o resto da divisão por 2 for 0 então o número é par, senão e ímpar
if num % 2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é ímpar!')
