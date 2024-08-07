# Escolhendo um aluno específico utilizando a função de escolha aleatória 'choice' da biblioteca 'random'

import random

nome = []

for i in range(4):
    aluno = input('Digite o nome do {}º aluno: '.format(i + 1))
    nome.append(aluno)

escolha = random.choice(nome)

print('O aluno escolhido foi o: {}'.format(escolha))
