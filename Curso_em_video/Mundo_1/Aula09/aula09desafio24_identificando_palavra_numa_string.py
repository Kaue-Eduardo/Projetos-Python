# Recebe o nome de uma cidade e verifica se o nome da cidade começa a com a palavra "SANTO"

# Recebe a frase
frase = str(input('Digite o nome da sua cidade: ')).strip()

# Divide a frase e transforma ela em maiúscula
frase_dividida = frase.upper().split()

# Faz a comparação se o primeiro nome é "SANTO"
print(frase_dividida[0] == 'SANTO')
