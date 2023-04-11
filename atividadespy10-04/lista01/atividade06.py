salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts consumidos: "))
valor_quilowatt = salario_minimo / 700
valor_total = valor_quilowatt * quilowatts
valor_com_desconto = valor_total * 0.9
print(f"O valor em reais de cada quilowatt é R${valor_quilowatt:.2f}")
print(f"O valor em reais a ser pago é R${valor_total:.2f}")
print(f"O valor com desconto de 10% é R${valor_com_desconto:.2f}")
