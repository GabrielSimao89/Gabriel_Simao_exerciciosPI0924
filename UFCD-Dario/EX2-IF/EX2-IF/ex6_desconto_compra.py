# Exercício 6 - Desconto de compra

nome = input("Introduz o nome do cliente: ")
compra = float(input("Introduz o valor da compra: "))

if compra <= 200:
    taxa_desconto = 0.10
elif compra <= 500:
    taxa_desconto = 0.15
else:
    taxa_desconto = 0.20

desconto = compra * taxa_desconto
total_pagar = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total_pagar:.2f}€")
