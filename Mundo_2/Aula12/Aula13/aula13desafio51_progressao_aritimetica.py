# O programa irá ler um número, depois sua razão da progressão aritmética e
# depois mostrar os 10 primeiros termos dessa progressão

# Entrada do número e da razão
num = int(input('Digite um número: '))
razao = int(input('Agora a sua razão da Progressão Aritmética: '))

# Atribuindo o número digitado a uma variável que vai ser usada para o cálculo
calculo = num

# Mostrando o valor digitado
print('Número digitado: {}'.format(num))

# Fazendo o cálculo com base no valor informado e a cada iteração soma-se a razão
for i in range(0, 10):
    calculo += razao
    print(calculo)
