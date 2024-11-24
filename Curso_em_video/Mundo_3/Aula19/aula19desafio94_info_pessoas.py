# O programa irá ler o nome, sexo e idade de várias pessoas, guardando todos em um dicionário e depois em uma lista.
# Depois irá mostrar quantas pessoas foram cadastradas, a média de idade no grupo, uma lista com todas as mulheres
# e uma lista com todas as pessoas com a idade acima da média

info = {}
pessoa = []
mulheres = []
qntd_pessoas = 0
idades = 0

while True:

    opcao = str(input('Deseja fazer um cadastro? [s/n]: '))[0].lower()

    if opcao == 's':
        info['Nome'] = str(input('Nome: ')).capitalize()
        info['Sexo'] = str(input('Sexo [m/f]: '))[0].lower()
        info['Idade'] = int(input('Idade: '))

        pessoa.append(info.copy())
        info.clear()
        qntd_pessoas += 1

    elif opcao == 'n':

        print(f'Foram cadastradas {qntd_pessoas} pessoas!')

        if qntd_pessoas > 0:

            for i in range(qntd_pessoas):
                idades += pessoa[i]['Idade']
                if pessoa[i]['Sexo'] == 'f':
                    mulheres.append(pessoa[i])

            media_idades = idades/qntd_pessoas

            print(f'A média da idade das pessoas do grupo é: {media_idades:.2f}')
            print(f'Mulheres do grupo: {mulheres}')

            print('Pessoas com idade acima da média: ')
            for i in range(qntd_pessoas):
                if pessoa[i]['Idade'] > media_idades:
                    print(pessoa[i])

        print('Programa encerrado!')
        break

    else:
        print('Entrada inválida, tente novamente!')