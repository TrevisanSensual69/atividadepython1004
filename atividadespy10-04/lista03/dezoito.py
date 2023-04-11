num = int(input("Digite um número inteiro: "))

div = []

for i in range(2, num):
    if num % i == 0:
        div.append(i)

if len(div) == 0:
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")
    print("Divisores:", div)