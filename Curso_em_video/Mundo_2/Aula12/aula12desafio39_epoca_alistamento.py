# Define se um homem já está na época de se alistar, se já passou, ou quanto tempo está faltando

# Biblioteca para importar a data
import datetime

# Entrada do ano pelo usuário
ano_usuario = int(input('Digie o seu ano de nascimento: '))

# Variável que armazena o ano atual automaticamente
ano_sistema = datetime.date.today().year

# Cálculo da diferença de anos
calculo_ano = ano_sistema - ano_usuario

# Condições
if calculo_ano > 18:
    print('Já se passaram {} anos do tempo de alistamento!'.format(calculo_ano - 18))
elif calculo_ano == 18:
    print('Está na hora de se alistar!')
elif calculo_ano < 18:
    print('Ainda faltam {} anos para o alistamento militar!'.format(18 - calculo_ano))
