n = int(input("Digite a quantidade de termos: "))
soma = 0
for i in range(1, n+1):
    termo = i / (i**2)
    soma += termo
print(f"O valor de S é: {soma}")