# Exercício Loop - Identificar números pares e ímpares

pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Introduz o {i + 1}.º número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
