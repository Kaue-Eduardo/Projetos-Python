# O programa irá receber 7 valores em uma lista única, depois esses valores vão ser separados
# entre par ou ímpar e no final, imprimir os valores em ordem crescente

valores_gerais = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º número: '))

    if num % 2 == 0:
        valores_gerais[0].append(num)
    else:
        valores_gerais[1].append(num)

valores_gerais[0].sort()
print(f'Valores par: {valores_gerais[0]}')
valores_gerais[1].sort()
print(f'Valores ímpar: {valores_gerais[1]}')
