limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))
incremento = int(input("Digite o incremento: "))

for num in range(limite_inferior, limite_superior+1, incremento):
    print(num)
