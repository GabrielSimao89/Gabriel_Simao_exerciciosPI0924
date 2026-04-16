categoria = input("Introduz a categoria: ").strip().lower()
preco = float(input("Introduz o preço: "))

match categoria:
    case "eletrônico" | "eletronico":
        if preco > 1000:
            print("Produto de luxo")
        else:
            print("Produto comum")
    case "alimento":
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")
