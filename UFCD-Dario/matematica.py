# Exercício 8 - Operação matemática

operacao = input("Introduz a operação (soma, subtrai, multiplica, divide): ").strip().lower()
numero1 = float(input("Introduz o primeiro número: "))
numero2 = float(input("Introduz o segundo número: "))

match operacao:
    case "soma":
        print(numero1 + numero2)
    case "subtrai":
        print(numero1 - numero2)
    case "multiplica":
        print(numero1 * numero2)
    case "divide":
        if numero2 != 0:
            print(numero1 / numero2)
        else:
            print("Erro: não é possível dividir por zero")
    case _:
        print("Operação inválida")

        