# Manipulação de Listas

# Maneira alternativa de criar lista
lista = list(range(0, 11))

# Criando a lista para manipulação
Lista = ['para_teste']

# ADICIONAR

# Para adicionar um item no final da lista
# Entrada de dados
item = str(input('Digite seu nome: ')).capitalize()
# Método 'append' para adicionar algo à lista
Lista.append(item)
# Mostrando o resultado
print(Lista)

# Para adicionar um item no início ou em uma posição específica
# Entrada de dados
item = str(input('Digite seu nome: ')).capitalize()
# Método 'insert' para adicionar algo à lista
Lista.insert(0, item)
# Mostrando o resultado
print(Lista)

# Copiar lista
# Nova variável = método para copiar, usar a lista como parâmetro com o símbolo '[:]'
recebendo_lista = Lista[:]


# DELETAR
del Lista[1] # básico

Lista.pop(1) # função por índice
Lista.pop() # elimina a última posição

recebendo_lista.remove('para_teste') # função pelo conteúdo

print(recebendo_lista)

# ORGANIZAR

# Função que a cada iteração traz tanto o conteúdo quanto o índice
for indice, valor in enumerate(recebendo_lista):
    print(f'{indice, valor}')

# Ordem crescente ou alfabética
lista.sort()

# Ordem decrescente ou inversa
lista.sort(reverse=True)

