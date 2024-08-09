# Jogo pedra, papel ou tesoura, JOKENPÔ

# Importando a biblioteca para o código selecionar uma opção
import random
escolha = str

# Escolha do código
computador = random.choice(['Pedra', 'Papel', 'Tesoura'])

# Menu
print('VAMOS JOGAR JOKENPÔ!\nEscolha uma das opções abaixo:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
opcao = int(input('Digite o número da opção selecionada: '))

# Definindo entrada do usuário
if opcao == 1:
    escolha = 'Pedra'
elif opcao == 2:
    escolha = 'Papel'
elif opcao == 3:
    escolha = 'Tesoura'

# Mostra a escolha do computador e a do usuário antes do resultado do jogo
print('\nSua escolha: {}\nEscolha do computador: {}'.format(escolha, computador))

# Define o ganhador da rodada
if computador == escolha:
    print('Deu empate!')

if computador == 'Pedra':
    if escolha == 'Papel':
        print('Você ganhou!')
    elif escolha == 'Tesoura':
        print('Você perdeu!')

if computador == 'Papel':
    if escolha == 'Pedra':
        print('Você perdeu!')
    elif escolha == 'Tesoura':
        print('Você ganhou!')

if computador == 'Tesoura':
    if escolha == 'Pedra':
        print('Você ganhou!')
    elif escolha == 'Papel':
        print('Você Perdeu!')
