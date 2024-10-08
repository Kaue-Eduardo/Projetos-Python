# O programa irá ler o nome e o peso de várias pessoas, no fim mostrando quantas pessoas foram cadastradas
# uma lista com as pessoas mais pesadas e uma com as pessoas mais leves

qntd_pessoas = 0
pessoas = []
infos = []
pessoas_pesadas = []
pessoas_leves = []

while True:

    opcao = str(input('Deseja cadastrar? [s/n]: ')[0].lower())
    if opcao == 's':
        infos.append(str(input('Digite seu nome: ')).capitalize())
        infos.append(float(input('Digite seu peso: ')))
        # Fazendo uma cópia exata
        pessoas.append(infos[:])
        # Apagando conteúdos primeira lista
        infos.clear()

        qntd_pessoas += 1

    elif opcao == 'n':

        maior_peso = max(pessoa[1] for pessoa in pessoas)

        print(f'O maior peso foi {max(pessoas[][1])} da(as) pessoa(as): ')


        print(f'Foram cadastradas {qntd_pessoas} pessoas!')

        print('Programa encerrado!')
        break

    else:
        print('Opção inválida, tente novamente!')

