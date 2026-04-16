# Exercício 5 - Ler 3 valores e exibir em ordem crescente e decrescente

num1 = int(input("Introduz o 1.º número: "))
num2 = int(input("Introduz o 2.º número: "))
num3 = int(input("Introduz o 3.º número: "))

valores = [num1, num2, num3]
valores.sort()

print("Crescente:", ", ".join(map(str, valores)))
print("Decrescente:", ", ".join(map(str, valores[::-1])))
