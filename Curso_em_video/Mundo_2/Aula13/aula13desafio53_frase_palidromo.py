# Recebe uma frase e verifica se ela é palíndromo (a frase é a mesma de trás para frente)

# Entrada da frase já retirando os espaços inicias e dividindo a frase em strings a cada espaço
frase = str(input('Digite uma frase: ')).strip().split()

# Unindo as strings(a palavras) em uma única palavra
frase_sem_espaco = ''.join(frase)

# Confere se a frase sem espaços é igual a mesma frase invertida
if frase_sem_espaco == frase_sem_espaco[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
