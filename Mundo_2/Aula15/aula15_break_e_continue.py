# Como fazer um laço INFINITO

# Variável criada apenas para mostrar qual é o número da iteração
contador = 0

# Laço infinito até que haja uma interrupção interna
while True:

    # Bloco para mostrar qual o número da iteração, quantas vezes o laço foi executado!
    contador += 1
    print(f'Execução número: {contador}')

    # Interrupção do laço, aqui poderia ser alguma entrada específica pelo lado do usuário!
    if contador == 1000000:
        # INTERRUPÇÃO
        break
