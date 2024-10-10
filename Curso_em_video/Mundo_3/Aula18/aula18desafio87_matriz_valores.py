# O programa vai criar uma matriz 3x3, mostrar a soma dos números pares
# a soma da terceira coluna e o maior valor da segunda linha

valores_pares = 0
soma_terceira_coluna = 0

# Estrutura para criar a matriz, 3 colunas primeiro e depois 3 linhas
matriz = [[0 for i in range(0, 3)] for i in range(0,  3)]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            valores_pares += matriz[i][j]

maior_valor_segunda_linha = max(matriz[1])

for i in range(3):
    soma_terceira_coluna += matriz[i][2]

for linha in matriz:
    print(linha)

print(f'Maior valor da segunda linha: {maior_valor_segunda_linha}')
print(f'Soma da terceira coluna: {soma_terceira_coluna}')
print(f'Valores pares: {valores_pares}')
