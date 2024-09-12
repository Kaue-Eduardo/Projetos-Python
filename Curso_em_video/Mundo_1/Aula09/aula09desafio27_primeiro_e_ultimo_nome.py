# Recebe um nome, divide ele em uma lista de nomes e mostra o primeiro e o último nome

# Recebe o nome
nome = str(input('Digite seu nome completo: ')).strip()

# Divide o nome em uma lista de strings a cada espaço
nome_dividido = nome.split()

# Printa o primeiro nome da lista de strings
print('Primeiro nome: {}'.format(nome_dividido[0]))

# Printa o último nome da lista de strings
# Modo alternativo para o código abaixo: nome_dividido[len(nome_dividido) - 1]
print('Último nome: {}'.format(nome_dividido[-1]))
