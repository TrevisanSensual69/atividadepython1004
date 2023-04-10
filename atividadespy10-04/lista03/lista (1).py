capacidade_maxima = int(input("Digite a capacidade máxima do restaurante: "))
clientes = int(input("Informe a quantidade de clientes no local: "))

if clientes >= capacidade_maxima:
    print("Restaurante lotado, não há mais mesas disponíveis.")
else:
    print("Ainda há mesas disponíveis.")
