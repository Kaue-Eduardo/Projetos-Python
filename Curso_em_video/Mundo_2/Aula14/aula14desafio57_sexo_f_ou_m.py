# Esse programa irá ler o sexo de uma pessoa, se for diferente de Masculino ou Feminino
# o programa irá pedir para repetir até que uma das opções seja digitada

# Variável de controle
controle = 'm'

while controle != 'm' or controle != 'f':

    # Entrada da informação
    controle = str(input('Digite o seu sexo [M/F] ou 0 para sair: ')).lower().strip()

    # Mostra ao usuário que a entrada foi aceita
    if controle == 'm' or controle == 'f':
        print('Aceito!')
        break

    # Condição se a entrada não for compatível
    if controle != 'm' and controle != 'f' and controle != '0':
        print('Tente novamente!')

    # Condição para encerrar o programa
    if controle == '0':
        print('Saindo')
        break
