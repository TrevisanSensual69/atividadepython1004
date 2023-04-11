line = int(input("Digite o total de linhas da matriz: "))
colum = int(input("Digite o total de colunas da matriz: "))

matriz = [[i+j for j in range(colum)] for i in range(line)]

for i in range(line):
    for j in range(colum):
        print("A{},{} = {}".format(i, j, matriz[i][j]), end="")
        if j == colum-1:
            print("#")
        else:
            print(",", end=" ")
