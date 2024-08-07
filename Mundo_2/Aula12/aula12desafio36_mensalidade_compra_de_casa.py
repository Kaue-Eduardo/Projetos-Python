# Calula se é possível fazer a compra de uma casa com relação ao salário do comprador

# Recebe as informações da compra
casa = float(input('Digite o valor da casa a ser comprada: '))
salario = float(input('Digite o valor do seu salário: R$'))
anos_totais = int(input('Digite em quantos anos deseja pagar o valor da casa: '))

# Cálculo mensalidade
mensalidade = casa / (anos_totais * 12)

# Se a mensalidade for maior que 30% do salário do comprador, não será possível fazer a compra
if mensalidade > (salario * 0.3):
    print('Infelizmente essa casa não pode ser financiada!')
else:
    print('Parabéns! O financiamento foi aprovado!')
    print('Sua mensalidade ficou no valor de R$ {:.2f}'.format(mensalidade))

