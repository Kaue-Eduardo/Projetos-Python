# Nesse código faremos uma tabuada

# Recebe o número para fazer a tabuada dele
num = int(input('Digite o número que deseja saber a tabuada: '))

# Mostra o número ao qual a tabuada vai calcular
print('Tabuada do {}:'.format(num))

# Laço para imprimir e fazer os cálculos a cada iteração
for i in range(1, 11):
    # Cálculo
    resultado = num * i
    # Formatação para apresentar ao usuário
    print('{} * {} = {}'.format(num, i, resultado))
