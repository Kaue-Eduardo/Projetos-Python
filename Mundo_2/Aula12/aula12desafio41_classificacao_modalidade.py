# Colhe o ano de nascimento e calcula a idade, se dependendo da idade configura a categoria no esporte

# Biblioteca usada para coletar o ano atual do sistema
import datetime

# Entrada ano de nascimento
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Difinição de ano de acordo com a data do sistema
ano_atual = datetime.date.today().year

# Calculando a idade do usuário
idade = ano_atual - ano_nascimento

# Condições para a classificação de acordo com a idade
if idade <= 9:
    print('MIRIM')

if (idade > 9) and (idade <= 14):
    print('INFANTIL')

if (idade > 14) and (idade <= 19):
    print('JUNIOR')

if (idade > 19) and (idade <= 20):
    print('SÊNIOR')

if idade >= 20:
    print('MASTER')
