base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
result = 1

for i in range(expoente):
    result *= base

print(f"{base} elevado a {expoente} é igual a {result}")