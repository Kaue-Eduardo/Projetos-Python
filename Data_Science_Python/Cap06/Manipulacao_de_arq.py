frase = open("/PythonDSA/Cap06/teste.txt", "r")
print(frase.read())
frase.close

frase2 = open("/PythonDSA/Cap06/teste2.txt", "w")
aql = 'Aquele teste maroto. '
frase2.write(f"{aql}")
frase2.close()
frase2 = open("/PythonDSA/Cap06/teste2.txt", "r")
print(frase2.read())
frase2.close()

########################################################################################
#Método atualizado

with open('/PythonDSA/Cap06/teste2.txt', "r") as arq:
    conteudo = arq.read()
print(len(conteudo))

texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira'
with open('/PythonDSA/Cap06/teste3.txt', "w") as teste1:
    teste1.write(texto[:18] + '\n' + texto[19:].capitalize())

with open('/PythonDSA/Cap06/teste3.txt', "r") as teste1:
    teste2 = teste1.read()

print(teste2)