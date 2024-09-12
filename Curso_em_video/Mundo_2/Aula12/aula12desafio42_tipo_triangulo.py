# Verifica se é possível criar um triângulo e qual o tipo dele

lado = []
lado_medio = 0.0

# Entrada dos valores dos lados do triângulo
for i in range(3):
    ladin = float(input('Digite o tamanho do lado {}: '.format(i + 1)))
    lado.append(ladin)

# Maior lado
maior_lado = max(lado)

# Menor lado
lado_pequeno = min(lado)

# Lado médio
for i in range(3):
    if (lado[i] >= lado_pequeno) and (lado[i] <= maior_lado):
        lado_medio = lado[i]

# Condições se é possível ter um triângulo e se for possível, de qual tipo ele é
if ((lado_pequeno + lado_medio > maior_lado) and (lado_pequeno + maior_lado > lado_medio) and (lado_medio + maior_lado > lado_pequeno)) or (maior_lado == lado_medio == lado_pequeno):
    print('Essas 3 retas PODEM formar um triângulo!')
    if maior_lado == lado_medio == lado_pequeno:
        print('O triângulo vai ser equilátero!')
    elif (lado_pequeno == lado_medio) or (lado_pequeno == maior_lado) or (lado_medio == maior_lado):
        print('O triângulo vai ser isósceles!')
    elif (maior_lado != lado_medio != lado_pequeno):
        print('O triângulo vai ser escaleno!')
else:
    print('Essas 3 retas NÃO PODEM formar um triângulo!')
