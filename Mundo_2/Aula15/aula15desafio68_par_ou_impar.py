# Esse programa irá jogar par ou impar com o usuário, quando o usuário perder o programa será encerrado

# Biblioteca para o computador escolher par ou ímpar
from random import choice

# Variáveis de controle
vitorias = 0

# Laço de repetição
while True:

    # Escolha do computador
    computador = choice(['par', 'impar'])

    # Escolha do usuário
    usuario = int(input('\nOpções:\n1 - Par\n2 - Ímpar\nSua escolha: '))

    # Condição de vitória se for par
    if usuario == 1:
        if computador == 'par':
            print('\nVocê: Par\nComputador: Par')
            print('Você ganhou!!!')
            vitorias += 1

        elif computador == 'impar':
            print('\nVocê: Par\nComputador: Impar')
            print('Você perdeu!!!')
            print(f'Você teve {vitorias} vitorias consecutivas')
            break

    # Condição de vitória se for ímpar
    if usuario == 2:
        if computador == 'par':
            print('\nVocê: Impar\nComputador: par')
            print('Você perdeu!!!')
            print(f'Você teve {vitorias} vitorias consecutivas')
            break

        elif computador == 'impar':
            print('\nVocê: Impar\nComputador: Impar')
            print('Você ganhou!!!')
            vitorias += 1

