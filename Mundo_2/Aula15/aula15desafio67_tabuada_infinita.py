# O programa recebe uma entrada sendo feito a tabuada do número digitado

# Laço infinito
while True:
    # Entrada do usuário
    num = int(input('Digite qual número deseja saber a tabuáda ou QUALQUER negativo para encerrar: '))

    # Condição quer verifica se o número é positivo para continuar ou negativo para parar
    if num >= 0:

        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')

    else:
        print('Fim do programa!')
        break
