# Exercício 1 - Converter segundos em horas, minutos e segundos

segundos_total = int(input("Introduz o total de segundos: "))

horas = segundos_total // 3600
resto = segundos_total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
