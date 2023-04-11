num = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, num+1):
    soma += 2*i
print("A soma dos", num, "primeiros números pares é de:", soma)