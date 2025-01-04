# Funções são estruturas para fazer coisas rotineiras

# Declarando uma função
def printar():
    print('Opa')


def parametros(texto):
    print('-' * 30)
    print(texto)
    print('-' * 30)


def soma(a, b):
    print(f'A soma de {a} + {b} = {a + b}')


def contador(* num):
    print(f'A quantidade de números passados é: {len(num)}')


def dobrar(itens):
    i = 0
    while i < len(itens):
        itens[i] *= 2
        i += 1


# Chamando a função
printar()

# Passando parâmetro
parametros('Testando com parâmetros!')

# Dois parâmetros
soma(12, 34)

# Desempacotando
contador(1, 2, 3)
contador(2)

valores = [7, 2, 5, 0, 4]
dobrar(valores)
print(valores)
