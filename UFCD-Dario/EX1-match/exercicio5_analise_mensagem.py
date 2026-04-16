mensagem = input("Introduz uma mensagem: ").strip().lower()

match mensagem:
    case "olá" | "ola" | "bom dia":
        print("Saudação")
    case _ if mensagem.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in mensagem or "adeus" in mensagem:
        print("Despedida")
    case _:
        print("Mensagem genérica")
