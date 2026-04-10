# Exercício 7 - Classificação de produto

categoria = input("Introduz a categoria: ").strip().lower()
preco = float(input("Introduz o preço: "))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preco": _}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")