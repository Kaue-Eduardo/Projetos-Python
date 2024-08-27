# Esse programa receberá a entrada da idade e sexo de várias pessoas
# e perguntar sempre se quer parar ou continuar os cadastros

# Variáveis de controle
quantidade_maior_18 = 0
quantidade_h = 0
quantidade_m_menor_20 = 0

while True:

    # Entrada de dados
    continuar = str(input('Deseja fazer um cadastro[S/N]: ')).lower()[0]

    # Condição se desejar fazer um cadastro
    if continuar == 's':
        idade = int(input('Digite a sua idade: '))
        sexo = str(input('Digite seu sexo[M/F]: ')).lower()[0]

        # Contador que soma a quantidade de pessoas acima de 18 anos
        if idade > 18:
            quantidade_maior_18 += 1

        # Contador que soma a quantidade de pessoas do sexo masculino
        if sexo == 'm':
            quantidade_h += 1

        # Contador que soma a quantidade de mulheres com menos de 20 anos
        if sexo == 'f' and idade < 20:
            quantidade_m_menor_20 += 1

    # Condição se não desejar fazer um cadastro
    elif continuar == 'n':
        print(f'{quantidade_maior_18} pessoas têm mais de 18 anos!')
        print(f'{quantidade_h} homens foram cadastrados!')
        print(f'{quantidade_m_menor_20} mulheres possuem menos de 20 anos!')
        print('Programa encerrado!')
        break

    # Opção inválida
    else:
        print('Opção inválida, digite S para continuar ou N para parar o programa')
