soma = 0
cont = 0
while cont < 30:
    n = int(input("Número entre 1 e 50: "))
    if n >= 1 and n <= 50 and n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print("Média:", soma / 30)
