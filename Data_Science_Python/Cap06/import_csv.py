########################################################################################
#Arquivo CSV

import csv

with open('/PythonDSA/Cap06/numeros.csv', "w", newline = '\n') as arq:
    #Linha que lê o arquivo com o pacote csv e armazena na variável "wt"
    wt = csv.writer(arq)

    wt.writerow(['nota1', 'nota2', 'nota3'])
    wt.writerow([63,87,92])
    wt.writerow([61,79,76])
    wt.writerow([72,64,91])

with open('/PythonDSA/Cap06/numeros.csv', "r", encoding = 'utf8') as arquivo:
    #Linha que lê o arquivo com o pacote csv e armazena na variável "wt"
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

with open('/PythonDSA/Cap06/numeros.csv', 'r') as arq1:
    conteudo = csv.reader(arq1)
    dados = list(conteudo)

#for linha in dados[1:]:
#    print(linha)