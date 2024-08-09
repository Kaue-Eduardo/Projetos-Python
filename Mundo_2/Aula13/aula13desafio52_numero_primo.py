# Será lido um número e decidido se ele é primo ou não

# Entrada do número
num = int(input('Digite um número inteiro: '))

if num < 2:
    print('O número {} não é primo!'.format(num))
if num == 2:
    print('O número {} é primo!'.format(num))
elif num % num == 0 and num % 2 != 0:
    print('O número {} é primo!'.format(num))
else:
    print('O número {} não é primo!'.format(num))
