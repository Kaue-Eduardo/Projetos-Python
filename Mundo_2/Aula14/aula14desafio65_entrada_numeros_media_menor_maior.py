# O programa pode receber vários números, no final da execução mostra a média deles
# e qual foi o menor e o maior valor digitado

# Variáveis de controle
loop = 1
quantidade_num = 0
soma_num = 0
# O valor 'None' pode ser usado quando vamos fazer comparação de valores, como não sabemos o primeiro valor, esse valor vai assumir o primeiro valor digitado
maior = None
menor = None

while loop != 0:
    # Entrada dos números
    numeros = int(input('Digite um número para somar ou 0 para parar: ').strip())

    # Verifica se a entrada é diferente de 0, se for ele executa normalmente
    if numeros != 0:
        # Variável que faz a soma dos valores digitados
        soma_num += numeros
        # Variável que faz a soma de quantos números foram digitados
        quantidade_num += 1

        # Condição para verificar o número maior
        if maior is None or numeros > maior:
            maior = numeros

        # Condição para verificar o número menor
        if menor is None or numeros < menor:
            menor = numeros
    # Se a entrada for igual a 0 a variável de controle do laço será definida como 0
    else:
        loop = numeros
        continue

# Essa condição imprime os resultados apenas se a quantidade de iterações forem válidas
if quantidade_num > 0:
    print('Essa é a média dos {} número digitados: {:.2f}'.format(quantidade_num, soma_num / quantidade_num))
    print('Maior e menor números digitados:\nMaior: {} || Menor: {}'.format(maior, menor))
else:
    print('Nenhum número válido foi digitado, portanto não foi possível estipular a média, o maior e o menor números!')
