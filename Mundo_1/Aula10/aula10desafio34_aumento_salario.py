# De acordo com o salário do trabalhador define o valor do aumento

salario_aumentado = 0.0

# recebe o valor do salário atual
salario = float(input('Digite o valor do seu salário: R$ '))

# se o salário for menor ou igual a 1250 reais, o aumento vai ser de 15%, se for maior vai ser de 10%
if salario >= 1.250:
    salario_aumentado = salario + (salario * 0.1)
    print('Seu salário teve um aumento de 10%, o novo valor é: R$ {}'.format(salario_aumentado))
else:
    salario_aumentado = salario + (salario * 0.15)
    print('Seu salário teve um aumento de 15%, o novo valor é: R$ {}'.format(salario_aumentado))
