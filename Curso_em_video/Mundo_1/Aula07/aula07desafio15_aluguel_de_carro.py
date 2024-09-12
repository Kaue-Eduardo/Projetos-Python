# Aluguel de um carro com base no tempo usado e a quilometragem usada
# Cobra 60 reais por dia e 15 centavos por quilômetro rodado

dia = int(input('Digite a quantidade de dias que você ficou com o carro: '))
km = float(input('Digite a quantidade de KM que você rodou com o carro: '))
dia = dia * 60
km = km * 0.15
print('O valor a ser pago corresponde a: R$ {:.2f}'.format(dia + km))
