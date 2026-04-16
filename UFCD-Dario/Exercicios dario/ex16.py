# Exercício 16

soma = 0
contador = 0

while contador < 30:
    numero = int(input(f"Digite o {contador+1}º número par entre 1 e 50: "))

    if 1 <= numero <= 50 and numero % 2 == 0:
        soma += numero
        contador += 1
    else:
        print("Número inválido.")

media = soma / 30
print("Média =", media)


