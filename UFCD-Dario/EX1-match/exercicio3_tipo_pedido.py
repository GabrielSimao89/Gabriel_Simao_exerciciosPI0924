tipo = input("Introduz o tipo (compra/venda): ").strip().lower()
valor = float(input("Introduz o valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": v}:
        print(f"Compra de {v:.2f}€")
    case {"tipo": "venda", "valor": v}:
        print(f"Venda de {v:.2f}€")
    case _:
        print("Pedido desconhecido")
