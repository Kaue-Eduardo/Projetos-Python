# Aprimoramento do desafio 93, agora deverá aceitar vários jogadores e ter um detalhamento de cada jogador.
jogador = {}
jogadores = []

while True:
    opcao = str(input('Deseja fazer um cadastro? [s/n]: '))[0].lower()

    if opcao == 's':
        jogador['Nome'] = str(input('Digite o nome do Jogador: '))
        jogador['Quantidade_de_partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
        jogador['Gols'] = []
        jogador['Total_de_gols'] = 0

        for i in range(jogador['Quantidade_de_partidas']):
            gols = int(input(f'Digite a quantidade de gols da partida {i + 1}: '))
            jogador['Gols'].append(gols)
            jogador['Total_de_gols'] += gols

        jogadores.append(jogador.copy())
        jogador.clear()

    elif opcao == 'n':
        print("\nResumo dos Jogadores:")

        for idx, jogador in enumerate(jogadores, start=1):
            print(f"Jogador {idx}: Nome: {jogador['Nome']}, Gols: {jogador['Gols']}, Total de Gols: {jogador['Total_de_gols']}")

        opcao2 = int(input('\n1 - Mostrar mais detalhes\n2 - Encerrar código\nOpção: '))
        if opcao2 == 1:

            num_jogador = int(input('Digite o número do jogador para detalhes: '))

            if 1 <= num_jogador <= len(jogadores):
                jogador_detalhado = jogadores[num_jogador - 1]
                print(f"\nDetalhes do Jogador {num_jogador} - {jogador_detalhado['Nome']}:")

                for partida, gols in enumerate(jogador_detalhado['Gols'], start=1):
                    print(f"  Partida {partida}: {gols} gols")
                print(f"Total de Gols: {jogador_detalhado['Total_de_gols']}\n")

            else:
                print("Número de jogador inválido!")

        elif opcao2 == 2:
            print('Código encerrado!')
            break
        else:
            print("Opção inválida, tente novamente!")

    else:
        print('Entrada inválida, tente novamente!')
