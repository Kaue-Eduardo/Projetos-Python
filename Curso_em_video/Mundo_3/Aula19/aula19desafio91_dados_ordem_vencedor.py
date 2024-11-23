# O programa vai gerar 4 valores automáticos correspondentes às faces de um dado
# cada valor vai pertencer a um usuário e vai ser guardado num dicionário
# no final o vencedor será o usuário com o maior número, que será colocado em ordem

from random import randint

jogadores = {}

for i in range(0, 4):

    jogadores[f'Jogador_{i + 1}'] = randint(1, 6)

for jogador, num in jogadores.items():
    print(f'{jogador}, número sorteado: {num}')

ordenados_jogadores = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

print('\nOrdem dos jogadores:')
for jogador, numero in ordenados_jogadores:
    print(f'{jogador}, Número sorteado: {numero}')

print(f'\nVencedor: {ordenados_jogadores[0][0]}, número: {ordenados_jogadores[0][1]}')
