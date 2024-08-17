# Esse programa executa a sequência de Fibonacci

# Quantidade de termos desejada
qntd_termos = int(input('Digite a quantidade de termos que deseja: '))

# Primeira e segunda posições
t1 = 0
t2 = 1

# Variável de controle, começa com 3, pois as 3 primeiras posições estão como obrigatórias
contador = 3

# Imprime os valores 1 e 2 da sequência
print('{} -> {}'.format(t1, t2), end='')

while contador <= qntd_termos:
    # definindo a terceira posição
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    # Define a t1 com o valor de t2 para pular para o próximo número
    t1 = t2
    # Define a t2 com o valor de t3 para pular para o próximo número
    t2 = t3

    # Um contador para finalizar o loop
    contador += 1
