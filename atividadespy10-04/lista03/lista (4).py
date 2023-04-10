n = int(input("Digite o valor de n: "))
a, b = 1, 1
contador = 2
if n == 1:
    print("1")
elif n == 2:
    print("1, 1")
else:
    fib = [a, b]
    while contador < n:
        a, b = b, a + b
        fib.append(b)
        contador += 1
    print(", ".join(str(x) for x in fib))
