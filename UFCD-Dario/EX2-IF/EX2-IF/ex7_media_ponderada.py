# Exercício 7 - Calcular média de notas com pesos

nota1 = float(input("Introduz a nota da 1.ª prova: "))
nota2 = float(input("Introduz a nota da 2.ª prova: "))
nota3 = float(input("Introduz a nota da 3.ª prova: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"Média: {media:.1f}")

if media >= 6:
    print("APROVADO")
else:
    print("REPROVADO")
