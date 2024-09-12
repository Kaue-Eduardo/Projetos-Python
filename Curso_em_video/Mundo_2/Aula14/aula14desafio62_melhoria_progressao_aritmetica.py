# O programa irá ler um número, depois sua razão da progressão aritmética e
# depois mostrar 10 ou mais termos dessa progressão

# Entrada do número e da razão
num = int(input('Digite um número: '))
razao = int(input('Agora a sua razão da Progressão Aritmética: '))

# Variáveis de controle
soma = num
contador = 0
mais_termos = 1

# Laço de repetição com 10 repetições
while contador < 10:
    # Somando os valores da programação
    soma += razao
    print(soma, end=' ')

    # Contador que altera o valor a cada iteração para dar fim ao laço
    contador += 1

    # Condição para ter mais termos
    if contador == 10:
        mais_termos = int(input('\nDigite a quantidade de termos a mais ou 0 para finalizar: '))
        contador = contador - mais_termos
        # Se o termo digitado for 0 o programa encerra
        if mais_termos == 0:
            print('Encerrando!')
            break
