full_data = []

arq = open('\PythonDSA\Cap06\salarios.csv', 'r')
data = arq.read()
div_linhas = data.split("\n")

for item in div_linhas:
    user = item.split(",")
    full_data.append(user)

print(full_data)

#for linha in open('\PythonDSA\Cap06\salarios.csv'):
#    print(linha)

first_row = full_data[0]

i = 0
for item in full_data:
    i += 1

print(i)
ii = 0
for item in first_row:
    ii += 1

print(ii)