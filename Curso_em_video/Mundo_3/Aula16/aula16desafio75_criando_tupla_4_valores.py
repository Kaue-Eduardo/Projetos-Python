# O programa lê 4 valores e faz uma tupla com eles, depois mostra quantas vezes o número 9 apareceu
# em qual posição está o primeiro número 3 e quais foram os números pares

# Lista que vai virar uma tupla
tupla = []


# Laço para receber os valores
for i in range(0, 4):
    digitado = int(input(f'Digite o {i + 1}º número: '))
    # Inserindo os valores digitados na lista
    tupla.append(digitado)

# Transformando a lista em uma tupla
tupla = tuple(tupla)

# Mostrando os valores encontrados
print(f'O número 9 apareceu {tupla.count(9)} vezes')

# Verificando se há o número 3 na tupla
if 3 in tupla:
    print(f'O primeiro 3 está na {(tupla.index(3) + 1)}ª posição !')
else:
    print('O número 3 não foi digitado!')

print('Números pares:', end=' ')

# Laço para identificar os números pares
for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i], end=' ')
