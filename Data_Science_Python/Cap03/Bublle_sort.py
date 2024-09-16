print('Esse código organiza números em ordem crescente!')

#vetor com os números a serem colocados em ordem
numeros = [7, 3, 10]
n = len(numeros)

#criação da função para colocar os números em ordem
def ordem_crescente(numeros):

    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros[j] > numeros[ j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

#   for 0 in range(3):
#       for 0 in range(0, 3 - 0 - 1):
#          if numeros[0] > numeros[ 0 + 1]:
#              numeros[0], numeros[0 + 1] = numeros[0 + 1], numeros[0]

#   for 0 in range(3):
#       for 1 in range(0, 3 - 0 - 1):
#          if numeros[1] > numeros[ 1 + 1]:
#              numeros[1], numeros[1 + 1] = numeros[1 + 1], numeros[1]

    return numeros

#atuação da função "ordem_crescente" no vetor "numeros"
print(ordem_crescente(numeros))