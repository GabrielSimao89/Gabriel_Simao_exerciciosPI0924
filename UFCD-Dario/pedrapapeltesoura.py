# Exercício 10 - Pedra, Papel ou Tesoura

jogador1 = input("Jogador 1: ").strip().lower()
jogador2 = input("Jogador 2: ").strip().lower()

match (jogador1, jogador2):
    case (j1, j2) if j1 == j2:
        print("Empate")
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")



        