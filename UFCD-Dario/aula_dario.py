import requests as rex

perg = int(input("Queres inserir o nome COMPLETO insira 1 se queres inserir NOME e SOBRENOME insira 2: "))

if perg == 1:
    nome = input("Digite o Nome Completo: ")
elif perg == 2:
    nome1 = input("Digite o Nome: ")
    sobrenome = input("Digite o Sobrenome: ")

sessao = int(input("Desejas achar um Formando (digite '1') ou Formador (digite '2')? "))
comeco = int(input("Onde desejas começar a busca? "))
fim = int(input("Onde desejas acabar a busca? "))

for i in range(comeco, fim, 1):

    request = rex.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={i}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600")

    if sessao == 1 and perg == 1:
        if nome in request.text and "Sessão como Formando" in request.text:
            print(f"Nome encontrado para o id {i}: {nome}")
            print(request.text)
            break
        else:              
            print(f"ID {i}: Nome não encontrado.")

    elif sessao == 1 and perg == 2:
        if nome1 in request.text and sobrenome in request.text and "Sessão como Formando" in request.text:
            print(f"Nome encontrado para o id {i}: {nome1} {sobrenome}")
            print(request.text)
            break
        else:              
            print(f"ID {i}: Nome não encontrado.")

    if sessao == 2 and perg == 1:
        if nome in request.text and "Sessão como Formador" in request.text:
            print(f"Nome encontrado para o id {i}: {nome}")
            print(request.text)
            break
        else:              
            print(f"ID {i}: Nome não encontrado.")
    elif sessao == 2 and perg == 2:
        if nome1 in request.text and sobrenome in request.text and "Sessão como Formador" in request.text:
            print(f"Nome encontrado para o id {i}: {nome1} {sobrenome}")
            print(request.text)
            break
        else:              
            print(f"ID {i}: Nome não encontrado.")

