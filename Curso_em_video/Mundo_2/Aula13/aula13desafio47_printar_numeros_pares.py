# Imprimindo todos os número pares do intervalo entre 1 e 50

# Laço de repetição que inicia em 1 e vai até 50
for i in range(1, 50):
    # Condição que usa o resto da divisão para verificar se o número é par
    if i % 2 == 0:
        print(i)

print('Fim')
