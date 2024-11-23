# O programa irá ler o nome, ano de nascimento e carteira de trabalho,
# em um dicionário, se a CTPS (Carteira de Trabalho de Previdência Social)
# for diferente de zero, o dicionário também receberá o ano de contratação
# e o salário, no final calcule quantos anos faltará para a pessoa se aposentar

from datetime import datetime

ano_atual = datetime.now().year

dados = {}

dados['Nome'] = str(input('Digite o nome: '))
dados['Idade'] = (ano_atual - (int(input('Digite o ano de nascimento: '))))
ctps = int(input('Digite o número da sua carteira de trabalho (0 se não tiver):'))

if ctps == 0:
    dados['CPTS'] = 'Não se aplica'
else:
    dados['Contratação'] = (int(input('Digite o ano da contratação: ')))
    dados['Salário'] = float(input('Digite o salário recebido: '))
    dados['Aposentadoria'] = ((35 - (ano_atual - dados['Contratação'])) + dados['Idade'])

for info, cont in dados.items():
    print(f'{info} tem o valor: {cont}')
