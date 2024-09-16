#criando o uma lista chamada "numeros" para receber os valores de 1 a 100
numeros = list(range(1, 101))

#criando estrutura de repetição que recebe os números da lista e pega o resto da divisão, se for 0 ele printa o número
for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num)