num = int(input("Digite um número inteiro: "))

if num < 2:
    print("O número não é primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break
    if primo:
        print("O número é primo")
    else:
        print("O número não é primo")