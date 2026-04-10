# Exercício 6 - Estado do servidor

status = input("Introduz o status (ok/erro): ").strip().lower()
tempo_resposta = int(input("Introduz o tempo de resposta em ms: "))

servidor = {"status": status, "tempo_resposta": tempo_resposta}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok", "tempo_resposta": t}:
        print("Servidor ativo")
    case {"status": "erro", "tempo_resposta": _}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")