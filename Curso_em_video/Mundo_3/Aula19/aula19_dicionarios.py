# Estruturas básicas dicionários

# Criando
dicionario_1 = {}
dicionario_2 = dict()

# Estrutura --- chave - conteúdo - chave - conteúdo
dicionario_1 = {'nome': 'Kauê', 'idade': 21}

print(dicionario_1['nome'])

# -------------------------------------------------------------------- #

# Adicionar item
dicionario_1['sexo'] = 'M'

print(dicionario_1)

# -------------------------------------------------------------------- #

# Remover item
del dicionario_1['idade']

print(dicionario_1)

# -------------------------------------------------------------------- #

# Printar conteúdo
print(dicionario_1.values())
# Printar chave
print(dicionario_1.keys())

# -------------------------------------------------------------------- #

# Tipo de enumerate
for key, value in dicionario_1.items():
    print(f'O {key} é {value}')

# -------------------------------------------------------------------- #

# Inserindo dicionários numa lista
info = {}
pessoa = []

for i in range(0, 3):
    info['nome'] = str(input(f'Digite o {i + 1}º nome: ').capitalize())
    info['idade'] = int(input(f'Digite a idade: '))
    pessoa.append(info.copy())

print(pessoa)

for e in pessoa:
    for dicio in e.values():
        print(dicio, end=' ')

# -------------------------------------------------------------------- #

# Printando por posições
print(pessoa[0]['nome'])

# -------------------------------------------------------------------- #
