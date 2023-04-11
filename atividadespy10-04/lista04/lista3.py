soma = 0
cont = 0
num = 0

while cont < 50:
    if num % 2 == 0:
        soma += num
        cont += 1
    num += 1

print("A soma dos 50 primeiros números pares é:", soma)
