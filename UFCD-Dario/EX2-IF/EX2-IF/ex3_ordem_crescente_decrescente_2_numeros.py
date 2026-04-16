# Exercício 3 - Mostrar 2 números em ordem crescente e decrescente

num1 = int(input("Introduz o 1.º número: "))
num2 = int(input("Introduz o 2.º número: "))

if num1 < num2:
    crescente = f"{num1}, {num2}"
    decrescente = f"{num2}, {num1}"
else:
    crescente = f"{num2}, {num1}"
    decrescente = f"{num1}, {num2}"

print(f"Crescente: {crescente}")
print(f"Decrescente: {decrescente}")
