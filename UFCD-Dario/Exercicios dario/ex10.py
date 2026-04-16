# Exercício 10

numero = int(input("Digite um número: "))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

print("Quantidade de divisores =", contador)

