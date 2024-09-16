#Elevando ao quadrado
a = pow(4,2)
print(a,'\n')

b = 'a, b, c'
print(b)

#Definindo strings
nome = 'Kaue'
sobrenome = 'Eduardo'

#Concatenando e printando strings
fullname = nome + ' ' + sobrenome
print(fullname)
print(b.upper())

lista = [102, '102']
lista1 = [101, '101']

for item in lista:
    lista1.append(item)
print(lista1)

dic = {}
dic['teste'] = 10
dic['teste1'] = 20
sla = dic['teste'] + dic['teste1']
print(sla)

dic['teste2'] = ['picanha','fraldinha','alcatra']
print(dic['teste2'])
del dic["teste2"][2]
print(dic['teste2'])
print(dic['teste2'][0].capitalize())
dic['teste2'].append('alcatra')
print(dic['teste2'])