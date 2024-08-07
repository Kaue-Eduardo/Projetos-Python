# Identificando tipos

dado = input('Digite algo: ')
print('Tipo: {}'.format(type(dado)))
print('Numérico: {}'.format(dado.isnumeric()))
print('Letras e números: {}'.format(dado.isalnum()))
print('Apenas espaços: {}'.format(dado.isspace()))
