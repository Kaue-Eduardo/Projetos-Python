# Calcula se um ano é bissexto ou não

# Entrada do ano
ano = int(input('Digite em qual ano você está: '))

# Se o ano for divisível por 400 ou divisível por 4 e não divisível por 100
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))
