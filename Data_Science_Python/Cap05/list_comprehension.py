frutas = ['melao','caqui','melancia','limao','maracuja','cereja','morango']

ft_sel = input('Digite uma letra para filtrar os tipos de frutas: ')

#Eu fiz essa versão mas eu quero uma versão melhorada que pegue as frutas com a primeira letra comparável a que eu digitar
#frutas_selecionadas = [x for x in frutas if ft_sel in x]

#Esse aqui pega a primeira letra da lista 'frutas' por conta da função "starswtich() em comparação com a primeira letra doq for digitado"
frutas_selecionadas = [x for x in frutas if x.startswith(ft_sel[0].lower())]

print(frutas_selecionadas)

##########################################################################################################################################
# ---- DICT COMPREHENSION ---- #

dicio_alunos = {'Kauê' : 84, 'Thiago' : 68, 'Ana' : 86, 'João' : 57, 'Pablo' : 93}

dicio_alunos_status = {k:'Aprovado' if v > 70 else 'Reprovado' for (k,v) in dicio_alunos.items()}

print(dicio_alunos_status)