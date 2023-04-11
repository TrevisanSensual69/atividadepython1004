menor = 1000
maior = 0
soma = 0

while True:
    num = int(input("Digite um número entre 0 e 1000: "))
    if num == -1:
        break
    elif num < 0 or num > 1000:
        print("Número inválido, digite um número entre 0 e 1000")
        continue
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
        soma += num

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
