# Exercício 12

numero = int(input("Digite um número: "))

soma = 0
subtracao = numero
multiplicacao = 1
divisao = numero
operacoes = 0

for i in range(1, numero):
    soma += i
    operacoes += 1

    subtracao -= i
    operacoes += 1

    multiplicacao *= i
    operacoes += 1

    divisao /= i
    operacoes += 1

print("Soma =", soma)
print("Subtração =", subtracao)
print("Multiplicação =", multiplicacao)
print("Divisão =", divisao)
print("Total de operações =", operacoes)

