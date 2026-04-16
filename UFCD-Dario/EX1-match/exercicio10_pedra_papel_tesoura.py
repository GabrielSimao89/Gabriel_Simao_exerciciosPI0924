j1 = input("Jogador 1: ").strip().lower()
j2 = input("Jogador 2: ").strip().lower()

match (j1, j2):
    case (a, b) if a == b:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")
