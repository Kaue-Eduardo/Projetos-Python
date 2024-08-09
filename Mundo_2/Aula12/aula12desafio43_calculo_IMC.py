# Cálculo IMC

# Recebe o peso e a altura
peso = float(input('Digite o seu peso em QUILOS: '))
altura = float(input('Digite a sua altura em METROS: '))

# Faz o cálculo do IMC e printa o resultado
imc = peso / pow(altura, 2)
print('Seu IMC corresponde a: {:.2f}'.format(imc))


# Condições para enquadrar o paciente
print('Seu diagnóstico:')
if imc < 18.5:
    print('Abaixo do peso!')
elif (imc >= 18.5) and (imc < 25):
    print('Peso ideal!')
elif (imc >= 25) and (imc < 30):
    print('Acima do peso!')
elif (imc >= 30) and (imc <= 40):
    print('Obesidade!')
elif imc > 40:
    print('Obesidade Mórbida')
