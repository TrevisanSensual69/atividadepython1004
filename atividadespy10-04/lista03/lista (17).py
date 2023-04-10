# solicita ao usuário o limite superior do intervalo e o incremento
limite_sup = float(input("Informe o limite superior do intervalo (em graus Fahrenheit): "))
incremento = float(input("Informe o incremento (em graus Fahrenheit): "))

# define o limite inferior
limite_inf = 10.0

# exibe o cabeçalho da tabela
print("Fahrenheit\tCelsius")

# exibe as conversões de temperatura, de acordo com o intervalo e o incremento informados
for f in range(int(limite_inf), int(limite_sup)+1, int(incremento)):
    c = (f - 32) * 5/9
    print("{:.1f}\t\t{:.1f}".format(f, c))
