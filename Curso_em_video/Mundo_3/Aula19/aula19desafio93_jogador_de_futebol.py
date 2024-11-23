# O programa irá ler o nome do jogador e quantas partidas o jogador jogou.
# Depois vai ler quantos gols foram feitos por partida e irá armazenar isso tudo
# em um dicionário, incluindo a quantidade de gols no campeonato.

jogador = {}
qnt_gols = 0

jogador['Nome'] = str(input('Digite o nome do Jogador: '))
jogador['Quantidade_de_partidas'] = int(input('Digite a quantidade de partidas jogadas: '))

for i in range(jogador['Quantidade_de_partidas']):
    jogador[f'Partida_{i + 1}'] = int(input(f'Digite a quantidade de gols da partida {i + 1}: '))
    qnt_gols += jogador[f'Partida_{i + 1}']

print(f'O Jogador {jogador['Nome']} jogou {jogador['Quantidade_de_partidas']} partidas!')
for i in range(jogador['Quantidade_de_partidas']):
    print(f'Na partida {i + 1}, ele fez {jogador[f'Partida_{i + 1}']} gols!')
print(f'Foi um total de {qnt_gols} gols!')
