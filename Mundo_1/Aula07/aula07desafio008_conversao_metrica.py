# Conversão de métricas de tamanho

valor = float(input('Digite um valor em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('Esse é número que você digitou em: \nQuilômetro: {} km \nHectômetro: {} hm \nDecâmetro: {} dam \nMetros: {} m \nDecímetros: {} dm \nCentímetros: {} cm \nMilímetros: {} mm'.format(km, hm, dam, valor, dm, cm, mm))
