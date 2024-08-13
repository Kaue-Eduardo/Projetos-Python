# O programa irá ler um número, depois sua razão da progressão aritmética e
# depois mostrar os 10 primeiros termos dessa progressão

# Entrada do número e da razão
num = int(input('Digite um número: '))
razao = int(input('Agora a sua razão da Progressão Aritmética: '))

# Variáveis de controle
soma = num
contador = 0

# Laço de repetição com 10 repetições
while contador < 10:
    # Somando os valores da programação
    soma += razao
    print(soma)

    # Contador que altera o valor a cada iteração para dar fim ao laço
    contador += 1
