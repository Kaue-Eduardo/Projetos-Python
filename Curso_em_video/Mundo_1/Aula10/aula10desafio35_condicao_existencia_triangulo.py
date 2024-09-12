# Decide se possível fazer um triângulo com as retas definidas

lado = []
lado_medio = 0

# Entrada de dados
for i in range(3):
    ladin = float(input('Digite o tamanho do lado {}: '.format(i)))
    lado.append(ladin)

# Define o maior lado
maior_lado = max(lado)

# Define o menor lado
lado_pequeno = min(lado)

# Define o lado médio
for i in range(3):
    if (lado[i] != lado_pequeno) and (lado[i] != maior_lado):
        lado_medio = lado[i]

# Condição de existência de um triângulo, a soma dos lados menores deve ser menor que o maior lado
if (lado_pequeno + lado_medio) < maior_lado:
    print('Essas 3 retas PODEM formar um triângulo!')
else:
    print('Essas 3 retas NÃO PODEM formar um triângulo!')
