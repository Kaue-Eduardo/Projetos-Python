# O programa recebe uma expressão matemática com parênteses e verifica se está correta

# Variáveis de Controle
parenteses = []

exp = input('Digite a expressão: ')

for i in exp:
    if i == '(':
        parenteses.append('(')
    if i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida')
