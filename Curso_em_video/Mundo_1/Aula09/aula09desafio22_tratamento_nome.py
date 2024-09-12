# O código recebe um nome, o deixa em maiúsculo, depois minúsculo,
# Retira os espaços e calcula a quantidade de letras do nome

# Recebe o nome
nome = str(input('Digite seu nome completo: '))

# Todas as letras maiúsculas
print(nome.upper())

# Todas as letras minúsculas
print(nome.lower())

# Tirando os espaços inicias e finais e depois separando a frase por palavra
letras = nome.strip().split()
# Juntando a frase por palavra sem os espaços
letras_sem_espaco = ''.join(letras)
print('Quantidade de letras: {}'.format(len(letras_sem_espaco)))

# Quantidade de letras no primeiro nome
print('Quantidade de letras no primeiro nome: {}'.format(len(letras[0])))
