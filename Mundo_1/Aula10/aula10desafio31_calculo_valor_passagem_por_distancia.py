# Calcula o valor da viagem de acordo com a distância viajada, se for menor ou igual a 200Km
# o valor é de 50 centavos por quilômetro, se a distância for maior o quilômetro sai por 45 centavos

distancia = float(input('Digite a distância da viagem em quilômetros: '))

if distancia <= 200:
    valor = distancia * 0.5
    print('O valor a ser pago pela viagem é de: R${:.2f}!'.format(valor))

else:
    valor = distancia * 0.45
    print('O valor a ser pago pela viagem é de: R${:.2f}!'.format(valor))

