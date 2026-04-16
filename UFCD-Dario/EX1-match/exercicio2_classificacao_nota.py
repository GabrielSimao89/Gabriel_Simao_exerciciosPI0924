nota = int(input("Introduz uma nota (0 a 100): "))

match nota:
    case n if 90 <= n <= 100:
        print("Excelente")
    case n if 70 <= n <= 89:
        print("Bom")
    case n if 50 <= n <= 69:
        print("Suficiente")
    case n if 0 <= n < 50:
        print("Insuficiente")
    case _:
        print("Nota inválida")
