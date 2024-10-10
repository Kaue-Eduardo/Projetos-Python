# O programa irá perguntar quantos jogos serão feitos
# e sortear 6 números para cada jogo

from random import sample

jogos = []

quantidade_jogos = int(input('Digite quantos jogos deseja fazer: '))

for i in range(quantidade_jogos):
    jogos.append(sample(range(1, 61), 6))

for indice, conteudo in enumerate(jogos):
    print(f'Jogo {indice + 1}: {conteudo}')
