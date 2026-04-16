# Exercício 8 - Calcular a média de 10 notas e informar quantas são iguais ou acima da média

notas = []

for i in range(10):
    nota = float(input(f"Introduz a nota do aluno {i + 1} (0 a 20): "))
    notas.append(nota)

media = sum(notas) / 10
acima_ou_igual = 0

for nota in notas:
    if nota >= media:
        acima_ou_igual += 1

print(f"Média: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_ou_igual}")
