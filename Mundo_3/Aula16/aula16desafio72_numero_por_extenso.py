# O programa recebe um número pelo teclado e o mostra por extenso

# Tupla com os números por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Laço para caso o usuário digitar um número inválido
while True:

    # Variável para receber o valor que deseja por extenso
    num = int(input('Digite um número para tê-lo por extenso: '))

    # Validando se o número é válido
    if 0 <= num <= 20:
        print(f'O número {num} por extenso é: {extenso[num]}')

    else:
        print('Número inválido! Tente novamente!')
