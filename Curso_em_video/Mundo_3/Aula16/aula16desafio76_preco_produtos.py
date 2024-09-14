# O programa imprime uma lista de produtos-preços que estão listados em uma tupla

# Tupla com os dados
tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
         'Estojo', 25, 'Compasso', 120, 'Mochila', 147.86,
         'Caneta', 2.25, 'Dicionário', 23.5, 'Lapiseira', 18.99)

# Laço que imprime cada posição da tupla a cada iteração
for i in range(0, len(tupla)):

    # Se for par (a primeira 'coluna') é impresso o seu conteúdo
    if i % 2 == 0:
        # Imprime a posição da tupla de acordo com a iteração, configura para esquerda e não quebra a linha
        print(f'{tupla[i]:.<30}', end='')

    # Imprime na mesma linha do anterior o conteúdo ímpar (segunda 'coluna')
    if i % 2 == 1:
        # Imprime a posição da tupla de acordo com a iteração, configura para direita com duas casas decimais
        print(f'R$ {tupla[i]:>6.2f}')
