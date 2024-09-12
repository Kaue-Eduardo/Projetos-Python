# randomiza um número e pede para o usuário adivinhar

import random

num_computador = random.randint(0, 5)

num_pessoa = int(input('Digite qual número inteiro de 0 a 5 que você acha que o computador pensou: '))

print('\nSeu número: {}\nNumero escolhido pelo computador: {}'.format(num_pessoa, num_computador))

if num_computador == num_pessoa:
    print('\nParabéns, você acertou o número!')
else:
    print('\nInfelizmente não foi dessa vez, tente novamente!')
