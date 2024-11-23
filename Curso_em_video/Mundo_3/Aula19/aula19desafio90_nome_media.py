# Esse programa recebe o nome e a média de um aluno, adicionando a
# situação do aluno de maneira automática e mostrando o resultado

aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: ').capitalize())
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'

elif aluno['media'] >= 4:
    aluno['situacao'] = 'Recuperação'

else:
    aluno['situacao'] = 'Reprovado'

print(aluno)

