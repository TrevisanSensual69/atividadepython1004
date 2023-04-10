while True:
    lados = int(input("Digite o número de lados do polígono: "))
    medida = float(input("Digite a medida do lado do polígono: "))

    if lados == 3:
        perimetro = lados * medida
        print("TRIANGULO perímetro={:.2f}".format(perimetro))
    elif lados == 4:
        area = medida ** 2
        print("QUADRADO área={:.2f}".format(area))
    elif lados == 5:
        print("PENTAGONO")
    elif lados < 3:
        print("não é polígono")
    else:
        print("polígono não identificado")
    resposta = int (input("Deseja realizar de novo?\n 1 - sim \n 2 - não \n"))
            
    if resposta == 2:
                break