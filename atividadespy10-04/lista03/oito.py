capmaxima = int(input("Digite a capacidade máxima do restaurante: "))
clientesatual = 0

while clientesatual < capmaxima:
    clientes_chegaram = int(input("Digite a quantidade de clientes que chegou: "))
    clientesatual += clientes_chegaram
    if clientesatual >= capmaxima:
        print("Restaurante lotado, não tem mais espaço")