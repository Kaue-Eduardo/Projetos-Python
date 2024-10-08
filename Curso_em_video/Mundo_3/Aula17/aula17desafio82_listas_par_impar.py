# O programa irá ler um monte de números, colocá-los numa lista e depois separá-los
# em duas listas, uma par e outra ímpar

# listas
lista_geral = []
lista_par = []
lista_impar = []

while True:

    numeros = int(input('Digite um número para ser adicionado ou 0 para parar: '))

    if numeros == 0:
        print(f'Lista geral: {lista_geral}')
        print(f'Lista par: {lista_par}')
        print(f'Lista ímpar: {lista_impar}')
        print('Código encerrado!')
        break

    lista_geral.append(numeros)

    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

"""
lista_g = []
lista_p = []
lista_i = []

while True:

    num = int(input('Digite um número para ser adicionado ou 0 para parar: '))

    if num == 0:
        print('Todos os números foram adicionados com sucesso!')
        break
    else:
        lista_g.append(num)

for i in lista_g:
    if i % 2 == 0:
        lista_p.append(i)
    else:
        lista_i.append(i)

print(f'Lista geral: {lista_g}')
print(f'Lista par: {lista_p}')
print(f'Lista ímpar: {lista_i}')
"""
