# Será lido um número e decidido se ele é primo ou não

# Entrada do número
num = int(input('Digite um número inteiro: '))
# Contador que irá receber quantas vezes o número foi dividido
contador = 0

# Laço que percorre todos os número do 1 ao número digitado
for i in range(1, num + 1):
    # Condição que divide o número digitado pelo número da iteração do laço
    if num % i == 0:
        # Contador que armazena quantas vezes o número foi divisível
        contador += 1

# Condição que determina se o número digitado é primo ou não,
# se for primo ele só pode ser divisível por 1 e por ele mesmo
if contador == 2:
    print('O número digitado é primo!')
else:
    print('O número digitado não é primo!')
