# Recebimento do valor de uma compra, parcelado ou de uma vez

# Recebe o valor
valor = float(input('Digite o valor do produto, R$: '))

# Menu
print('Qual será a forma de pagamento?')
print('1 - Dinheiro ou cheque (Desconto 10%)')
print('2 - Cartão de 1x (Desconto 5%)')
print('3 - Crédito de 2x (Sem desconto nem Acréscimo)')
print('4 - Crédito de 3x ou mais (Acréscimo de 20%)')
opcao = int(input('Digite o número da opção selecionada: '))

valor_final = 0

# Dependendo o valor e do tipo de pagamento, dá desconto, faz apenas a divisão ou faz acréscimo
if opcao == 1:
    valor_final = valor - (valor * 0.1)

elif opcao == 2:
    valor_final = valor - (valor * 0.05)

elif opcao == 3:
    valor_final = valor
    print('O valor da parcela é: R${:.2f}'.format(valor / 2))

elif opcao == 4:
    valor_final = valor + (valor * 0.2)
    quantidade = int(input('Digite a quantidade de parcelas: '))
    print('O valor da parcela é: {:.2f}'.format(valor_final / quantidade))

# Mostra o valor a ser pago
print('\nValor a ser pago: {:.2f}'.format(valor_final))
