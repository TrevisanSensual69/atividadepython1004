soma = 0
contador = 0

for num in range(2, 101, 2):
    soma += num
    contador += 1
    
    if contador == 50:
        break

print("A soma dos 50 primeiros números pares é de:", soma)