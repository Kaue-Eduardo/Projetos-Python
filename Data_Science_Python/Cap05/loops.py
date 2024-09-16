lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
lista3 = lista1 + lista2
mn = 0

for num in lista3:
    if num > mn:
        mn = num
print(mn)

valor_sla_fds = 0
while valor_sla_fds <= 50:
    if valor_sla_fds % 2 == 1:
        print(valor_sla_fds)
    valor_sla_fds += 1


valor = 0
print('\n')
while valor < 10:
    if valor == 4:
        break
    else:
        print(valor)
    valor += 1