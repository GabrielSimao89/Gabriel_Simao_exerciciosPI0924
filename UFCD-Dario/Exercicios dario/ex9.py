# Exercício 9

while True:
    numero = int(input("Digite um número entre 1 e 100: "))
    
    if 1 <= numero <= 100:
        break
    else:
        print("Valor inválido. Tente novamente.")

print("Número válido:", numero)

