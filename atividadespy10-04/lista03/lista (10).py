
num = int(input("Digite um número inteiro: "))

divisores = []
for i in range(2, num):
    if num % i == 0:
        divisores.append(i)

if len(divisores) == 0:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
    print(f"Ele é divisível pelos números {divisores}.")
