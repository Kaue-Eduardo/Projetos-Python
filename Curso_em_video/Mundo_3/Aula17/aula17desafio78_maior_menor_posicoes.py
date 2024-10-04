# O programa lê 5 valores e os coloca numa lista, no final mostra o maior, o menor e quais suas respectivas posições

# Variáveis de controle
minimo = 0
maximo = 0

# Criação Lista
lista = []

# Estrutura para receber os 5 valores
for i in range(0, 5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    lista.append(valor)

# Definindo os valores mínimo e máximo
minimo = min(lista)
maximo = max(lista)

# Mostrando o índice e o valor por um 'for' que percorre a lista
print(f'O menor número, que é {minimo}, está na(as) posição(ões): ', end='')
for indice, valor in enumerate(lista):
    if valor == minimo:
        print(f'{indice}', end=' ')

print(f'O maior número, que é: {maximo}, está na(as) posição(ões): ', end='')
for i, v in enumerate(lista):
    if maximo == v:
        print(f'{i}', end=' ')

