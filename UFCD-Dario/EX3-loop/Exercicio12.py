n = int(input("Número: "))
cont = 0
for i in range(1, n):
    print(n, "+", i, "=", n + i)
    print(n, "-", i, "=", n - i)
    print(n, "*", i, "=", n * i)
    print(n, "/", i, "=", n / i)
    cont = cont + 4
print("Operações feitas:", cont)
