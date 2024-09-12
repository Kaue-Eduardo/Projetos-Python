# Esse programa simula um caixa eletrônico, recebe um valor de saque do usuário
# e faz os cálculos de quantas cédulas de 50, 20, 10 e 1 reais serão necessárias

# Variáveis de controle
qnt_notas = 0
valor_da_nota = 50

# Valor que deseja sacar
saque = int(input('Digite o valor que deseja sacar: R$ '))

# Laço de repetição infinito
while True:
    # Enquanto o valor que desejar sacar 'couber' no valor da nota
    if saque >= valor_da_nota:
        # Vão ser feitas subtrações para verificar quantas vezes cabem a nota no valor total
        saque -= valor_da_nota
        # A cada nota que 'couber' no valor total vai ser somada a quantidade
        qnt_notas += 1

    # Se não 'couber' mais notas maiores, os valores das notas vão sendo diminuídos até 'caber'
    # se não 'couber' mais nenhuma nota o programa encerra
    else:
        if qnt_notas > 0:
            print(f'{qnt_notas} cédulas de R$ {valor_da_nota}')
        elif valor_da_nota == 50:
            valor_da_nota = 20
        elif valor_da_nota == 20:
            valor_da_nota = 10
        elif valor_da_nota == 10:
            valor_da_nota = 1
        if saque == 0:
            break
