# Esse programa irá ler o nome e o preço de vários produtos e no fim mostrar
# qual o total gasto na compra, quantos produtos custam mais que mil reais
# e qual o nome do produto mais barato

# Variáveis de controle
valor_total = 0.0
mais_que_mil = 0
produto_mais_barato = ''
valor_mais_barato = None

while True:

    # Entrada para verificar se para ou continua o código
    opcao = str(input('Deseja adicionar um produto[S/N]: ')).lower()[0]

    if opcao == 's':
        nome_produto = str(input('Digite o nome do produto: '))
        preco_produto = float(input('Digite o valor do produto: R$ '))

        # Soma do valor total dos produtos
        valor_total += preco_produto

        # Contador de produtos mais caros que mil reais
        if preco_produto > 1000:
            mais_que_mil += 1

        # Verificando qual é o produto mais barato
        if valor_mais_barato is None or preco_produto < valor_mais_barato:
            produto_mais_barato = nome_produto
            valor_mais_barato = preco_produto

    # Condição de parada
    elif opcao == 'n':
        print(f'\n{valor_total:.2f} foi o valor total gasto!')
        print(f'{mais_que_mil} produtos custaram mais que R$ 1000,00!')
        print(f'{produto_mais_barato} é o nome do produto mais barato que custou: R$ {valor_mais_barato:.2f}')
        print('Programa encerrado!')
        break

    # Opção inválida
    else:
        print('Opção inválida, digite S para continuar ou N para parar o programa')
