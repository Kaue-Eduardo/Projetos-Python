# Define o valor de uma multa de acordo com a velocidade de um veículo

# Recebe a velocidade
velocidade = int(input('Qual a velocidade do carro? '))

# Condicional, se for menor ou igual a 80Km/h o carro não recebe multa
if velocidade <= 80:
    print('Você está numa velocidade boa, continue assim!')

# Se for maior que a velocidade máxima, faz o cálculo da multa de acordo com a velocidade ultrapassada
else:
    valor = (velocidade - 80) * 7
    print('Você foi multado em R${}!'.format(valor))
