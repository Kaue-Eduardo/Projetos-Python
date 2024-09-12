# Esse programa o fatorial de um número

# Variáveis de controle
resultado = 0

# Entrada do número
numero = int(input('Digite um número para descobrir o seu fatorial: '))
contador = numero

# Laço de repetição
while contador >= 0:

    resultado += numero * (numero - 1)

    contador -= 1

print('O fatorial do número {} é: {}'.format(numero, resultado))
