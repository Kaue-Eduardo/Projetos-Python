# Verifica e um aluno tirou uma nota boa ou ruim

# Entrada nota 1 e nota 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Cálculo média
media = (n1 + n2) / 2

# Condição, se a média for maior ou igual a 6, o aluno teve uma boa nota, se não ele precisa estudar um pouco mais
if media >= 6:
    print('Sua média {} foi boa! Parabéns!'.format(media))
else:
    print('Sua média {} não foi boa! Estude mais!'.format(media))
