# Serão lidos os anos de nascimento de 7 pessoas, o programa mostrará quantos já são maior de idade
# e quantos ainda são menores de idade

# Importando biblioteca para pegar o ano atual
import datetime

# Iniciando variável para receber o resultado do cálculo de idade
maior_idade = 0
menor_idade = 0

# Definindo o ano atual com base no ano do sistema
ano_atual = datetime.date.today().year

for i in range(7):
    # Recebe o ano de nascimento da pessoa
    ano_nascimento = int(input('Pessoa {} digite o seu ano de nascimento: '.format(i)))
    # Calcula a idade da pessoa
    idade = ano_atual - ano_nascimento

    # Condição para verificar se a pessoa é maior de idade ou não, e contabiliza
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

# Exibe os resultados
print('{} pessoas já são maiores de idade!'.format(maior_idade))
print('{} pessoas não são maiores de idade!'.format(menor_idade))

