# Mostra a tabuada de um número específico

num = int(input('Digite um número: '))
print('Tabela do: {}'.format(num))

for i in range(10):
    print('{} + {} = {}'.format(num, i, num + i))
print('-'*15)
for i in range(10):
    print('{} - {} = {}'.format(num, i, num - i))
print('-'*15)
for i in range(10):
    print('{} x {} = {}'.format(num, i, num * i))
print('-'*15)
for i in range(1, 10):
    print('{} / {} = {}'.format(num, i, num / i))
print('-'*15)
