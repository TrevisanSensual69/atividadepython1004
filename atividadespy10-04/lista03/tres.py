pares = 0
impares = 0

for i in range(6):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Foram digitados {} valores pares e {} valores ímpares.".format(pares, impares))