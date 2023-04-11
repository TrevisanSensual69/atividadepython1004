n = int(input("Digite a quantidade de termos: "))

soma = 0

for i in range(1, n+1):
    numerador = i
    denominador = i**2
    termo = numerador / denominador
    soma += termo

print("S = {:.2f}".format(soma))
