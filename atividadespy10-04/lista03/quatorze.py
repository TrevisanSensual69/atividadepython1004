n = int(input("Quantidade de números: "))

menor = 10**9
maior = -10**9
soma = 0

for i in range(n):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num

print("O menor valor é:", menor)
print("O maior valor é:", maior)
print("A soma dos valores é:", soma)