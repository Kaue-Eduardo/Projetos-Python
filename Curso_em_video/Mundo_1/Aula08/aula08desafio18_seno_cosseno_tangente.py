# Calculando seno, cosseno e tangente de um ângulo específico

import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo {:.3f} possui o seno: {:.3f}, o cosseno: {:.3f} e a tangente: {:.3f}'.format(angulo, seno, cosseno, tangente))