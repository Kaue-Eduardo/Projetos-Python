# Criar uma matriz 3x3, preencher com os valores do teclado e no final
# printar na tela com a formatação 3x3

# Estrutura para criar a matriz, 3 colunas primeiro e depois 3 linhas
matriz = [[0 for i in range(0, 3)] for i in range(0,  3)]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}][{j}]: '))

for linha in matriz:
    print(linha)

