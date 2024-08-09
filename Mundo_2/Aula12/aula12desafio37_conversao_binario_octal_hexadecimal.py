# Convertendo número na base decimal para as bases, binário, octal e hexadecimal

# Recebe o número na base decimal
numero = int(input('Digite um número inteiro: '))

# Menu de opções para conversão
print('Você quer converter o número {} para qual base?'.format(numero))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
escolha = int(input('Digite o índice da opção escolhida: '))

if escolha == 1:
    binario = bin(numero)
    print('O número {} convertido para binário é: {}'.format(numero, binario[2:]))

elif escolha == 2:
    octal = oct(numero)
    print('O número {} convertido para octal é: {}'.format(numero, octal[2:]))

elif escolha == 3:
    hexadecimal = hex(numero)
    print('O número {} convertido para hexadecimal é: {}'.format(numero, hexadecimal[2:]))
