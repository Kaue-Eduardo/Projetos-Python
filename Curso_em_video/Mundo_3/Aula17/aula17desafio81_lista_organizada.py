# O programa lê vários números, mostra quantos foram digitados, organiza na forma decrescente
# e mostra se há o número 5 na lista

# Lista
num = []

while True:

    numero = input('Digite um número para adicionar ou * para parar: ')

    if numero == '*':
        print(f'Foram digitados {len(num)} números!')
        num.sort(reverse=True)
        print(f'A lista em ordem decrescente: {num}')
        if 5 in num:
            print('O número 5 está na lista!')
        else:
            print('O número 5 NÃO está na lista')
        break

    if numero == int(numero) and numero != '*':
        num.append(numero)
