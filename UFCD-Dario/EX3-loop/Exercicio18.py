n = int(input("Número: "))
cont = 0
for num in range(1, n + 1):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma = soma + i
    if soma == num:
        cont = cont + 1
print("Números perfeitos:", cont)
