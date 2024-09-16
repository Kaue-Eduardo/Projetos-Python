print('Bem vindo(a) à calculadora\n')

#menu de opções
escolha = int(input('Qual operação você deseja executar agora? \n'
      '1 - Soma (+)\n'
      '2 - Subtração (-)\n'
      '3 - Multiplicação (*)\n'
      '4 - Divisão (/)\n'
      'Sua escolha: '))

if(escolha >= 1 and escolha <= 4):
    #entrada de valores
    num1 = float(input('\nDigite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    #equações com o valores definidos pelo usuário
    if(escolha == 1):  
        resultado = num1 + num2
        print(f'O resultado da soma dos números ({num1}) e ({num2}) é igual a:', resultado)

    elif(escolha == 2):
        resultado = num1 - num2
        print(f'O resultado da subtração dos números ({num1}) e ({num2}) é igual a:', resultado)

    elif(escolha == 3):
        resultado = num1 * num2
        print(f'O resultado da multiplicação dos números ({num1}) e ({num2}) é igual a:', resultado)

    elif(escolha == 4):
        resultado = num1 / num2
        print(f'O resultado da divisão dos números ({num1}) e ({num2}) é igual a:', resultado)

else:
    print("!! Opção Inválida !!")