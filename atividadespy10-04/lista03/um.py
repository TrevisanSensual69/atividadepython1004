lsuperior = float(input("Digite o limite superior: "))
incremento = float(input("Digite o incremento: "))

print("Fahrenheit\tCelsius")

for f in range(10, int(lsuperior) + 1, int(incremento)):
    c = (f - 32) * 5/9
    print(f"{f}\t\t{c:.2f}")