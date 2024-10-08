# Lista
lista1 = []
lista1.append('Kauê')
lista1.append(21)

lista2 = lista1[:]
lista2.append('Moto')
lista2.append(21)

print(lista1)
print(lista2)

# Integrando listas
info = []
dados = []

for i in range(0, 2):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    info.append(dados[:])
    dados.clear()

print(info)
