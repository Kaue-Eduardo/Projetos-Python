# Entrada de números infinitos

# Variáveis para armazenar dados
contador = 0
soma = 0

# Laço de repetição
while True:

    # Entrada dos dados
    dados = int(input('Digite um número para somar ou QUALQUER negativo para parar: '))

    # Condição para somar os valores e a quantidade de iterações
    if dados > 0:
        soma += dados
        contador += 1

    else:
        print(f'Foram digitados: {contador} números e a soma deles é: {soma}')
        break
