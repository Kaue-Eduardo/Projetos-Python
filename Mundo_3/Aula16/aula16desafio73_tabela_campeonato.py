# O programa possui os 20 colocados da tabela do campeonato de futebol 'brasileirão'
# traz os 5 primeiros colocados, os 4 últimos, os times em ordem alfabética e a posição do time "Cruzeiro"

# Tabela dos 20 colocados do brasileirão 10-09-2024
times = ['Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama',
         'Atlético-MG', 'Internacional', 'Bragantino', 'Athletico-PR', 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense',
         'Corinthians', 'EC Vitória', 'Cuiaba', 'Atlético-GO']

# Primeiros 5 colocados
print(f'Os primeiros 5 colocados são: {times[:5]}')

# Últimos 4 colocados
print(f'Os 4 últimos colados são: {times[-4:]}')

# Os times em ordem alfabética
print(sorted(times))

# Posição do time desejado
print(f'O time "Cruzeiro" está na posição: {(times.index('Cruzeiro') + 1)}')
