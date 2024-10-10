# O programa irá ler o nome do aluno mais duas notas, colocará em uma lista composta
# no final mostrará uma média individual e permitirá ao usuário pesquisar por aluno

alunos = []

while True:

    opcao = int(input('Opções:\n1 - Cadastrar aluno\n2 - Pesquisar aluno\n3 - Encerrar o programa\nEscolha: '))

    if opcao == 1:

        nome = str(input('Digite o nome do aluno: ')).capitalize()
        nota1 = float(input('Digite a nota 1 do aluno: '))
        nota2 = float(input('Digite a nota 2 do aluno: '))

        alunos.append([nome, nota1, nota2])

    elif opcao == 2:

        nome_aluno = str(input('Digite o nome do aluno para saber suas notas e média: ')).capitalize()

        encontrado = False

        for linha in alunos:
            if linha[0] == nome_aluno:
                media = (linha[1] + linha[2]) / 2
                print(f'Nome: {linha[0]}, Nota 1: {linha[1]}, Nota 2: {linha[2]}, Média: {media:.2f}')
                encontrado = True
                break

        if not encontrado:
            print('Aluno não encontrado!')

    elif opcao == 3:
        for linha in alunos:
            media = (linha[1] + linha[2]) / 2
            print(f'Nome: {linha[0]}, Nota 1: {linha[1]}, Nota 2: {linha[2]}, Média: {media}')

        print('Programa encerrado!!!')
        break

    else:
        print('Opção inválida, tente novamente!')
