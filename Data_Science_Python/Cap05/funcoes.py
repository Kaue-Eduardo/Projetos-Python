sla = 'teStE 01'

def caixabaixa(texto):
    return texto.lower().capitalize()

print(caixabaixa(sla))

frase_grande = 'Esse teste é para ver a funcionalidade da função split'

def dividindo_frases(texto):
    return texto.split(' ')

token = dividindo_frases(frase_grande)

print(token)

teste_lambda = lambda fg: fg.upper()

print(teste_lambda(frase_grande))