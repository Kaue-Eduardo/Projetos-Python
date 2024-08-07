# Divide um número de 4 casas em suas unidades, dezenas, centenas e milhares

# Recebe o numero inteiro
numero = int(input('Digite um número de quantro casas: '))

# Faz o cálculo lógico para retirar apenas a casa desejada
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Configura as variáveis com os valores
print('O número {}, possui os dígitos:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar:{}'.format(numero, unidade, dezena, centena, milhar))
