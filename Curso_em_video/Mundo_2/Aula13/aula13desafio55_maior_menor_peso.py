# Recebe 5 pesos de pessoas diferentes e mostra qual foi o maior e qual foi o menor

# Iniciando as variáveis para usar de comparação com as entradas
maior_peso = 0
menor_peso = 10000

# Laço para a entrada dos valores
for i in range(5):
    # Recebendo os valores
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(i + 1)))

    # Condição que verifica o maior e o menor peso
    if maior_peso < peso:
        maior_peso = peso
    if menor_peso > peso:
        menor_peso = peso

# Mostra os resultados na tela
print('O maior peso é: {}'.format(maior_peso))
print('O menor peso é: {}'.format(menor_peso))
