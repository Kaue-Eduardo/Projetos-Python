# Definindo ordem de lista com a função 'shuffle' da biblioteca 'random'

import random

ordem = []

for i in range(4):
    alunos = str(input('Digite o nome do {}º aluno: '.format(i + 1)))
    ordem.append(alunos)

random.shuffle(ordem)

print('A ordem dos alunos é essa: {}!'.format(ordem))
