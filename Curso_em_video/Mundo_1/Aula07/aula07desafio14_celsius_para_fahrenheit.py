# Convertendo a temperatura de graus Celsius para Fahrenheit

temperatura = float(input('Digite a temperatura atual em ºC: '))
CparaF = (temperatura * 1.8) + 32
print('A temperatura atual em graus Celsius é de {:.2f}ºC e em Fahrenheit é de {:.2f}ºF'.format(temperatura, CparaF))