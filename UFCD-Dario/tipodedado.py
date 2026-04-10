# Exercício 4 - Tipo de dado

valor = input("Introduz um valor: ")

match valor:
    case _ if valor.startswith("[") and valor.endswith("]"):
        print("Lista")
    case _ if valor.isdigit():
        print("String numérica")
    case _:
        try:
            numero = int(valor)
            print("Número inteiro")
        except ValueError:
            try:
                numero = float(valor)
                print("Número decimal")
            except ValueError:
                print("String textual")