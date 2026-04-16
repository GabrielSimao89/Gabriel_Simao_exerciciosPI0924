cont = 0
num = 2
while cont < 10:
    div = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div = div + 1
    if div == 2:
        print(num)
        cont = cont + 1
    num = num + 1
