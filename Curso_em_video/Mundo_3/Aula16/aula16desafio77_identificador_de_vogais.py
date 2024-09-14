# O programa irá identificar se há vogais dentro de cada item da tupla

# Iniciação da tupla
tupla = ('Estou', 'aprendendo', 'Python', 'para', 'me', 'tornar', 'um',
         'cientista', 'de', 'dados')

# Laço para 'andar' nas posições da tupla
for i in tupla:
    # Imprime a palavra
    print(f'\nVogais da palavra "{i}": ', end='')
    # Rodando letra por letra
    for vogal in i:
        # Verificando letra por letra se há alguma vogal
        if vogal.lower() in 'aeiou':
            # Imprime suas vogais
            print(vogal.lower(), end=' ')
