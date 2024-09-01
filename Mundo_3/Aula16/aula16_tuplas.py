# Tuplas são variáveis compostas IMUTÁVEIS (uma vez criada, não pode ser alterada, apenas excluída e recriada)

# Inicializando uma tupla
tupla1 = ('Moto', 'Velocidade', 'Potência', 'Adrenalina')

# Mostrando um elemento específico
print(tupla1[2])

# O fatiamento pode ser aplicado à tupla
print(tupla1[:2])

# Fatiamento inverso, esse pode ser usado para mostrar os últimos elementos
print(tupla1[-2:])

# Possibilidade de ordenação de tupla, nesse caso alfabética, ele NÃO altera, apenas mostra na ordem
print(sorted(tupla1))

# Estrutura de repetição
# Tipo 1
for i in range(0, len(tupla1)):
    print(f'Vantagens de uma moto: {tupla1[i]}')
# Tipo 2
for comida in tupla1:
    print(f'Características de uma moto: {comida}')
# Tipo 3
for pos, pontos in enumerate(tupla1):
    print(f'Vantagens: {pontos}, posição na tupla: {pos}')
