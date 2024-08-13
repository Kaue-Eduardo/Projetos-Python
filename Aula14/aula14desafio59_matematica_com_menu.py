# O programa irá ler 2 valores e em seguida o usuário irá escolher o que deseja fazer com essas números

# Variáveis de controle
opcao = 0

while opcao != 5:
    # Entrada dos valores
    valor1 = float(input('Digite o primeiro número: '))
    valor2 = float(input('Digite o segundo número: '))

    # Menu de opções
    escolha = int(input('''1º número: {:.2f} || 2º número: {:.2f}
Opções:
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair
Digite a opção desejada: '''.format(valor1, valor2)))

    if escolha == 1:
        print('A soma dos valores digitados é: {:.2f}'.format(valor1 + valor2))

    elif escolha == 2:
        print('A multiplicação dos valores é: {:.2f}'.format(valor1 * valor2))

    elif escolha == 3:
        if valor1 > valor2:
            print('O primeiro número ({:.2f}) é maior!'.format(valor1))
        elif valor2 > valor1:
            print('O segundo número ({:.2f}) é maior!'.format(valor2))
        else:
            print('Os números digitados são iguais!')

    elif escolha == 4:
        print('Vamos recomeçar!')

    elif escolha == 5:
        print('Você escolheu sair!')
        break
