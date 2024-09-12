# O 'while' (enquanto) é uma estrutura de repetição versátil

# Variáveis de Controle
item = 0
opcao = 1
soma = 0

# Condição para a estrutura funcionar
while item < 10:
    item += 1
    print('Item = {}'.format(item))
print('Acabou!')

# Condição para a estrutura funcionar infinitamente
while opcao != 0:
    # Entrada do valor para somar ou interrupção
    valor = int(input('Digite um número para somar ou 0 para parar: '))

    # Condição, se for diferente de 0 irá somar, se for igual irá parar
    if valor != 0:
        soma += valor
    else:
        opcao = 0

# Mostra o resultado da soma
print('Resultado da soma: {}'.format(soma))
