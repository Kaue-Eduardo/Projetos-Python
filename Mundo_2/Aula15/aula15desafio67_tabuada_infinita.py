# O programa recebe uma entrada sendo feito a tabuada do número digitado

# Laço infinito
while True:
    # Entrada do usuário
    num = int(input('Digite o número que deseja saber a tabuáda ou QUALQUER negativo para encerrar: '))

    # Condição quer verifica se o número é positivo para continuar ou negativo para parar
    if num >= 0:

        # Variável para armazenar a quantidade de iterações
        iteracao = 1

        while iteracao <= 10:
            print(f'{num} x {iteracao} = {num * iteracao}')
            iteracao += 1
    else:
        print('Fim do programa!')
        break
