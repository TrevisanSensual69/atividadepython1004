pares = 0
impares = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("A quantidade de números pares é de:", pares)
print("A quantidade de números ímpares é de:", impares)