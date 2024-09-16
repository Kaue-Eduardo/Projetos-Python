import pandas as pd

arquivo = "\PythonDSA\Cap06\salarios.csv"

tabela = pd.read_csv(arquivo)

print(tabela)

#print(tabela['Name'].value_counts())