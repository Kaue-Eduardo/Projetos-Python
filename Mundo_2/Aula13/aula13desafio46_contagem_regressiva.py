# Contagem regressiva de 10 a 0, 1 segundo de espera a cada número para soltar fogos de artifício

# Biblioteca para trabalhar com o tempo
import time

# Laço que faz a contagem regressiva, começa em 10 e vai decaindo até 0
for i in range(10, 0, -1):
    # Imprime na tela o número da contagem regressiva
    print(i)
    # Utiliza a função 'sleep' da biblioteca time para atrasar a execução em 1 segundo
    time.sleep(1)

# Imprime na tela a liberação dos fogos após o fim da contagem
print('FOGOS!!!')
