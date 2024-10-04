# O programa lê vários números, se o número já tiver sido digitado ele não é adicionado,
# os valores serão apresentados em ordem crescente

# Estrutura do tipo lista
numeros = []

# Laço para a inserção de números ser infinita
while True:
    # Entrada do valor como uma string
    num = input('Digite um número para adicionar ou 0 para parar: ')

    # Condição de parada do código
    if num == '0' or num == '':
        # Função para organizar a lista
        numeros.sort()
        print(f'Número digitados, em ordem crescente: {numeros}')
        print('Código encerrado!')
        break

    # Verificando se o número já está na lista
    if int(num) in numeros:
        print('Esse número já foi digitado, digite outro número novo!')

    # Depois dos parâmetros verificados, adiciona o item à lista
    else:
        numeros.append(int(num))
