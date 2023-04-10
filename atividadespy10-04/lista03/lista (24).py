
fibonacci = [0, 1]
while fibonacci[-1] <= 500:
     proximo_valor = fibonacci[-1] + fibonacci[-2]
     fibonacci.append(proximo_valor)
print(fibonacci)
