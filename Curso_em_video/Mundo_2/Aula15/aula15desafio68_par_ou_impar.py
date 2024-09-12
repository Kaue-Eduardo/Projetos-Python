# Esse programa irá jogar par ou impar com o usuário, quando o usuário perder o programa será encerrado

# Biblioteca para o computador escolher par ou ímpar
from random import randint

# Variáveis de controle
vitorias = 0

# Laço de repetição
while True:

    # Escolha do computador
    computador = randint(0, 10)

    # Escolha do usuário
    valor_usuario = int(input('\nDigite o valor que deseja jogar: '))
    usuario = int(input('Opções:\n1 - Par\n2 - Ímpar\nSua escolha: '))

    # Condição de vitória se for par
    if usuario == 1:
        if (valor_usuario + computador) % 2 == 0:
            print('Você ganhou!!!')
            vitorias += 1

        else:
            print('Você perdeu!!!')
            print(f'Você teve {vitorias} vitorias consecutivas')
            break

    # Condição de vitória se for ímpar
    if usuario == 2:
        if (valor_usuario + computador) % 2 != 0:
            print('Você ganhou!!!')
            vitorias += 1

        else:
            print('Você perdeu!!!')
            print(f'Você teve {vitorias} vitorias consecutivas')
            break
