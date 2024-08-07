# Esse programa recebe uma frase e conta a quantidade de "a" na frase
# Dividindo a frase em uma lista de strings, mostrando quando foi encontrado
# Tanto o primeiro quanto o último "a"

# Recebe a frase
frase = str(input('Digite uma frase: ')).strip().lower()

# Conta a quantidade de "a" na String
print('Essa é a quantidade de "a" na frase: {}'.format(frase.count('a', 0, len(frase))))

# Começa a procurar a letra "a"
print('Primeira posição de "a": {}'.format(frase.find('a') + 1))

# Começa a procurar a letra "a" da direita "right" pra esquerda
print('A última posição de "a": {}'.format(frase.rfind('a') + 1))
