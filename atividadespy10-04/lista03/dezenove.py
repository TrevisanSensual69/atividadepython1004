n = int(input("Digite um número inteiro N: "))

num = list(range(2, n+1))

numdiv = 0

for i in range(2, int(n**0.5)+1):
    if i in num:
        for j in range(i*i, n+1, i):
            numdiv += 1
            if j in num:
                num.remove(j)

print("Números primos encontrados:", num)
print("Número de divisões realizadas:", numdiv)