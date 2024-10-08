# O programa lê 5 números e os organiza em ordem crescente em tempo real

# lista
num = []

for i in range(0, 5):
    numero = input(f'Digite o {i + 1}º número: ')
    # Verifica se o número digitado é o primeiro ou é maior que o último da lista
    if i == 0 or numero > num[-1]:
        num.append(numero)
    else:
        posicao = 0
        # Passa por todas as posições começando pela primeira
        while posicao < len(num):
            # Se o número for menor ou igual ao que está na posição/iteração da lista, insere na posição
            if numero <= num[posicao]:
                # Inserindo pela posição na lista
                num.insert(posicao, numero)
            # Variável de controle da posição da lista
            posicao += 1
