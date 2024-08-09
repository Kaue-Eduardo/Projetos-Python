# Esse código irá ler o nome, idade e sexo de 4 pessoas e no final mostrar
# média da idade, quem é o homem mais velho e quantas mulheres têm menos de 20 anos

# Iniciando as variáveis para serem trabalhadas dentro do laço e utilizadas para imprimir os resultados
soma_idade = 0
idade_maior = 0
homem_mais_velho = ''
qntd_mulheres = 0

# O laço pega as informações das 4 pessoas escolhidas
for i in range(4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite a letra "m" se seu sexo for masculino e "f" se for feminino: ')).lower()

    # Soma de todas as idades
    soma_idade += idade

    # Condição para descobrir o nome do homem mais velho pelo sexo e pela idade
    if sexo == 'm' and idade_maior < idade:
        # Armazena a maior idade a cada iteração
        idade_maior = idade
        # Atualiza o nome do homem mais velho a cada iteração
        homem_mais_velho = nome

    # Condição que define quantas mulheres têm menos de 20 anos pelo sexo e idade
    if sexo == 'f' and idade < 20:
        # Contador
        qntd_mulheres += 1

    # Informando ao usuário que o cadastro foi concluído e qual o número do cadastro
    print('Cadastro {} concluído!'.format(i + 1))

# Mostra os resultados correspondentes aos parâmetros
print('A idade média entre os participantes é: {:.2f}'.format(soma_idade / 4))
print('O nome do homem mais velho é: {}'.format(homem_mais_velho))
print('{} pessoa têm menos de 20 anos!'.format(qntd_mulheres))
