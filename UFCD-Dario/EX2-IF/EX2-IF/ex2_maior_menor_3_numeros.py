# Exercício 2 - Encontrar o maior e o menor valor entre 3 números

num1 = int(input("Introduz o 1.º número: "))
num2 = int(input("Introduz o 2.º número: "))
num3 = int(input("Introduz o 3.º número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"Maior: {maior}")
print(f"Menor: {menor}")
