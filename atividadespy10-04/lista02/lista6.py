num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"{num1} é o maior!")
elif num2 > num1:
    print(f"{num2} é o maior!")
else:
    print("Os números são iguais.")
