qtd_exelente = 0
qtd_ruim = 0
entrevistados = 50
for i in range(entrevistados):
    print("entrevistado:", i + 1)
    nome = input("digite seu nome:")
    idadde = int(input("digite sua idade:"))
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opiniao = int(input("digite sua opinião (1/2/3): "))
        if opiniao in [1,2,3]:
            break
        else:
            print("opção invalida.\n")
    if opiniao == 1:
        qtd_exelente +=1
    elif opiniao == 3:
        qtd_ruim +=1
print("\n1-_-resultado da pesquisa-_-")
print("quantidade de exelente:", qtd_exelente)
print("quantidade de ruim:", qtd_ruim)