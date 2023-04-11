numeros = []
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Entre os números {numeros}, há {pares} pares e {impares} ímpares.")
