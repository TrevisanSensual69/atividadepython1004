
n = int(input("Digite a quantidade de números a serem informados: "))
menor = None
maior = None
soma = 0

for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num
    soma += num


print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
