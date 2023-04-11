linferior = int(input("Digite o limite inferior: "))
lsuperior = int(input("Digite o limite superior: "))
incremento = int(input("Digite o incremento: "))

if incremento <= 0:
    print("O incremento deve ser um número positivo, não pode ser negativo")
else:
    i = linferior
    while i <= lsuperior:
        print(i)
        i += incremento