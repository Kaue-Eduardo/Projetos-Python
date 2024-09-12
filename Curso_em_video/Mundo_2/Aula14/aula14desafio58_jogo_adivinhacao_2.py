# Jogo da adivinhação, o computador irá escolher um número e o usuário irá tentar até acertar

# Importando biblioteca para obter aleatoriedade
from random import randint

# Número 'escolhido' pelo computador
computador = randint(0, 10)

# Variáveis de controle
usuario = -1
contador = 1

while usuario != computador:
    # Entrada do usuário
    usuario = int(input('Tente adivinhar o número de 0 a 10 que pensei: '))

    # Condição que verifica se o usuário acertou o número escolhido pelo computador
    if usuario != computador:
        print('Não foi dessa vez, tente novamente!')
        # Contador que mostra quantas vezes o usuário tentou acertar
        contador += 1
    else:
        print('\nSeu número: {}\nNumero escolhido pelo computador: {}'.format(usuario, computador))
        print('Você acertou!')
        print('Quantidade de tentativas: {}'.format(contador))

