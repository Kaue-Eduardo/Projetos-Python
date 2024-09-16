primos =[]

for num in range(2,51):
    eh_primo = True

    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
    
    if eh_primo:
        primos.append(num)

print(primos)

primos = []

for num in range(2, 51):
    eh_primo = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        primos.append(num)

print(primos)