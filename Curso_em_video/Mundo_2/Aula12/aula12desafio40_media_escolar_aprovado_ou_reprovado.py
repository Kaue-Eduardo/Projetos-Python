# Média escolar de duas notas

# Recebe as notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Faz a média das notas
media = (nota1 + nota2)/2

# Mostra a média para o usuário
print('Sua média: {:.2f}'.format(media))

# Condições, se estiver igual ou maior a 7, o aluno está aprovado, se estiver maior que 5 ou menos que 7 o aluno
# estará de recuperação, já se for menor que 5 ele irá reprovar direto
if media >= 7.0:
    print('Você está APROVADO!')

elif (media >= 5.0) and (media <= 6.9):
    print('Você está de RECUPERAÇÃO!')
    
elif media < 5.0:
    print('Você está REPROVADO!')
