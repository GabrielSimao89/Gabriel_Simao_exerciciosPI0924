n = int(input("Número: "))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        cont = cont + 1
print("Divisores:", cont)
