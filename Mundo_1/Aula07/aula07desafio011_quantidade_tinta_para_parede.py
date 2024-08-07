# Calcula o m² de uma parede e calcula a quantidade de tinta, a tinta faz 2m²/L

larg = float(input('Digite a largura da parede: '))
altu = float(input('Digite a altura da parede: '))

print('A parede tem: {}m² e vão ser necessários {}L de tinta para pintá-la!'.format(larg * altu, (larg * altu) / 2))
