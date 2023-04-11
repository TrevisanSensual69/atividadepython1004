
limite_superior = int(input("Digite o limite superior do intervalo desejado: "))
incremento = float(input("Digite o incremento desejado: "))

limite_inferior = 10

print("Fahrenheit  Celsius")

for fahrenheit in range(limite_inferior, limite_superior+1, incremento):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}F\t\t{celsius:.2f}C")   