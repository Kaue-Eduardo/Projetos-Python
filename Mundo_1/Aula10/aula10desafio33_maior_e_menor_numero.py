# Define quais são os maior e menor números digitados

num = []
armazenador = 0.0

for i in range(3):
    num_recebido = float(input('Digite um número: '))
    num.append(num_recebido)

armazenador = num[0]

for i in range(1, 3):
    if num[i] > armazenador:
        armazenador = num[i]

print('O maior número digitado é: {}'.format(armazenador))

armazenador2 = num[0]

for i in range(1, 3):
    if num[i] < armazenador2:
        armazenador2 = num[i]

print('O menor número digitado é: {}'.format(armazenador2))
