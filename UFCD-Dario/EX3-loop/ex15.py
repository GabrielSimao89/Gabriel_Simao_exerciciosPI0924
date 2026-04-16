# Exercício 15

contador = 0

for i in range(256):
    print(i, "=", chr(i))
    contador += 1

    if contador == 20:
        opcao = input("Continuar? (s/n): ").lower()
        if opcao != "s":
            break
        contador = 0



        