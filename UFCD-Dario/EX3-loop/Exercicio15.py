cont = 0
for i in range(256):
    print(i, "=", chr(i))
    cont = cont + 1
    if cont == 20:
        op = input("Continuar? (s/n): ")
        if op == "n":
            break
        cont = 0
