# Exercício 4 - Verificar se o cheque pode ser descontado

saldo = float(input("Introduz o saldo inicial: "))
cheque = float(input("Introduz o valor do cheque: "))

if cheque > saldo:
    print("O cheque não pode ser descontado.")
else:
    saldo -= cheque
    print(f"Cheque descontado, saldo atualizado: {saldo:.2f}€")
