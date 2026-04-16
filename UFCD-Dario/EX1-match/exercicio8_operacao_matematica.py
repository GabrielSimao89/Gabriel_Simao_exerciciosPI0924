operacao = input("Introduz a operação (soma, subtrai, multiplica, divide): ").strip().lower()
n1 = float(input("Introduz o primeiro número: "))
n2 = float(input("Introduz o segundo número: "))

match operacao:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        print("Erro: divisão por zero" if n2 == 0 else n1 / n2)
    case _:
        print("Operação inválida")
