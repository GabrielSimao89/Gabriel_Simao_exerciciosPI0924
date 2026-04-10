# Exercício 9 - Processamento de requisição

metodo = input("Introduz o método (GET/POST): ").strip().upper()
conteudo = input("Introduz o conteúdo: ")

requisicao = {"metodo": metodo, "conteudo": conteudo}

match requisicao:
    case {"metodo": "GET", "conteudo": _}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")

        