# O programa irá ler o nome e o peso de várias pessoas, no fim mostrando quantas pessoas foram cadastradas
# uma lista com as pessoas mais pesadas e uma com as pessoas mais leves

qntd_pessoas = 0
pessoas = []
infos = []

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
        menor_peso = min(pessoa[1] for pessoa in pessoas)

        pessoas_pesadas = [pessoa[0] for pessoa in pessoas if pessoa[1] == maior_peso]
        pessoas_leves = [pessoa[0] for pessoa in pessoas if pessoa[1] == menor_peso]

        print(f'O maior peso foi {maior_peso} Kg da(as) pessoa(as): {pessoas_pesadas}')
        print(f'O maior peso foi {menor_peso} Kg da(as) pessoa(as): {pessoas_leves}')

        print(f'Foram cadastradas {qntd_pessoas} pessoas!')

        print('Programa encerrado!')
        break

    else:
        print('Opção inválida, tente novamente!')
