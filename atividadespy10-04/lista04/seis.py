linferior = float(input("Digite o limite inferior: "))
lsuperior = float(input("Digite o limite superior: "))
decremento = float(input("Digite o decremento: "))

print("Celsius\tFahrenheit")
celsius = linferior
while celsius <= lsuperior:
    fahrenheit = (celsius * 9/5) + 32
    print("{:.1f}\t{:.1f}".format(celsius, fahrenheit))
    celsius += decremento