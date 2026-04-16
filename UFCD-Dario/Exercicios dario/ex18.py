# Exercício 18

limite = int(input("Digite um número: "))

contador_perfeitos = 0

for numero in range(1, limite + 1):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        print(numero, "é perfeito")
        contador_perfeitos += 1

print("Quantidade de números perfeitos =", contador_perfeitos)



