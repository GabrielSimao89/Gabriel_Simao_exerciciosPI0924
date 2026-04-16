# Exercício 3

soma = 0

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / 10
print("Média =", media)

