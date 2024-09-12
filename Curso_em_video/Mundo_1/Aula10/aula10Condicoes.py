tempo = int(input('Digite quantos anos sua moto tem: '))

if tempo <= 3:
    print('Sua moto é nova!')
else:
    print('Sua moto é velha')
print('-- FIM --')

print('Seu carro é novo' if tempo <= 3 else 'Seu carro é velho')
print('-- FIM --')
