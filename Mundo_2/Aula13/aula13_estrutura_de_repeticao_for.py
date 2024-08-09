moeda = True

# Estrutura básica de repetição
for i in range(0, 10):
    print('Opa! {}'.format(i + 1))

# Ideia de um mini game, toda vez que encontrar uma moeda vai ser notificado
for c in range(0, 3):
    if moeda:
        print('Pegou uma moeda')
    print('Andou uma casa')
    print('Pulou uma casa\n')
if moeda:
    print('Pegou uma moeda')
print('Andou uma casa')
print('Chegou ao seu destino')

# For para iterar ao contrário, o primeiro dígito é quando começa, o segundo é onde termina
# o ÚLTIMO número se fere a como ele vai reagir a cada iteração
for i in range(6, 0, -1):
    print(i)

# É possível utilizar uma entrada no teclado nos parâmetros dos laços
inicio = int(input('Digite um número inteiro para começar: '))
fim = int(input('Digite o fim do laço: '))
iteracao = int(input('Digite de quanto em quanto quer os números: '))

for i in range(inicio, fim, iteracao):
    print(i + 1)
print('Fim')

# É possível utilizar uma repetição para ter entrada de múltiplos números
quantidade = int(input('Digite a quantidade de números que quer digitar: '))
for i in range(0, quantidade):
    num = int(input('Digite o {}º número: '.format(i + 1)))
print('Fim')
