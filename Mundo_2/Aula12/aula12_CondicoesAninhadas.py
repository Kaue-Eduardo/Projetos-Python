#####################################################
# Estrutura condicional SIMPLES

nome = str(input('Qual é o seu nome? '))

if nome == 'Kauê':
    print('Que nome bonito!')

print('Seja bem vindo(a), {}!'.format(nome))

#####################################################
# Estrutura condicional COMPOSTA

nome1 = str(input('Digite seu nome: '))

if nome1 == 'Kauê':
    print('Nossa! Que nome bonito!')
else:
    print('Parabéns pelo nome!')

print('Seja muito bem vindo(a), {}!'.format(nome1))

#####################################################
# Estrutura condicional ANINHADA

nome2 = str(input('Seu nome é: '))

if nome2 == 'Kauê':
    print('Uau! Que nome bonito!')
elif nome2 == 'Pedro' or nome2 == 'Maria' or nome2 == 'Paulo':
    print('Seu nome é popular na região do Brasil!')
else:
    print('Seu nome não é popular na região do Brasil!')

print('Seja muitíssimo bem vindo(a), {}'.format(nome2))
