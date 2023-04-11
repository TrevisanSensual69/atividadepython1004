n = int(input("Quantas notas você deseja calcular a média: "))
soma = 0

for i in range(n):
    nota = float(input("Digite a {}ª nota: ".format(i+1)))
    soma += nota

media = soma / n

print("A média das notas é de: {:.2f}".format(media))
