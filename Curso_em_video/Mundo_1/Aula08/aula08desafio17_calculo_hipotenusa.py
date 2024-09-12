# Usando biblioteca para calcular hipotenusa de um número

import math

cateto1 = float(input('Digite o tamanho do cateto adjacente: '))
cateto2 = float(input('Digite o tamanho do cateto oposto: '))
print('Esse é o tamanho da hipotenusa desse triângulo retângulo: {:.3f}'.format(math.hypot(cateto1, cateto2)))
