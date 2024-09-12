frase = 'Curso em Vídeo Python'

# Fatiamento da Frase, começando no índice 9 e terminando no 14(exclusivo), pulando de 2 em 2
print(frase[9:14:2])

# Contando quantidade de índices
print(len(frase))

# Contando quantidade de 'o' da posição inicial até a última da string
print(frase.count('o', 0, len(frase)))

# Substituindo o item 'Python' por 'de Python' sem alterar a string
print(frase.replace('Python', 'de Python'))

# Setando a string inteira em maiúsculo
print(frase.upper())

# Setando a string inteira em minúsculo
print(frase.lower())

# Definindo apenas a primeira letra a String como maiúsculo e as outras como minúsculo
print(frase.capitalize())

# Definindo todas as palavras da String com as iniciais em maiúsculo
print(frase.title())

frase2 = '  Aprenda Python  '

# Tirando os primeiros e últimos espaços
print(frase2.strip())

# Tirando os últimos espaços
print(frase2.rstrip())

# Tirando os primeiros espaços
print(frase2.lstrip())

# Dividindo uma string a cada espaço, transformando em uma lista
print(frase2.split())

# Unindo uma lista, com o junção desejada
frase2modificada = frase2.split()
print('-'.join(frase2modificada))
