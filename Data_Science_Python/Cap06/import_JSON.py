import json as js

dict_guido = {'nome':'Kaue Eduardo',
              'linguagem':'Python',
              'similar':['c','Modula-3','lisp'],
              'user':1000000}

for k,v in dict_guido.items():
    print(k,v)

js.dumps(dict_guido)

with open("\PythonDSA\Cap06\dados.json", "w") as arq:
    arq.write(js.dumps(dict_guido))

with open("\PythonDSA\Cap06\dados.json", "r") as arq:
    texto = arq.read()
    dados = js.loads(texto)

print("\n")

print(dados["nome"])

open("\PythonDSA\Cap06/aquelewithopen.txt", "w").write(open("\PythonDSA\Cap06\dados.json", "r").read())

with open("\PythonDSA\Cap06/aquelewithopen.txt", "r") as leitura:
    texto1 = leitura.read()
    print(texto1)