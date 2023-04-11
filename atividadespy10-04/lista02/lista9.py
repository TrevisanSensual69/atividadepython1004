salario_bruto = float(input("Informe o salário bruto do funcionário: "))
proventos = float(input("Informe os proventos do funcionário: "))

if salario_bruto <= 5000:
    desconto = salario_bruto * 0.05
else:
    desconto = salario_bruto * 0.1

salario_liquido = salario_bruto + proventos - desconto

print("O salário líquido do funcionário é R$%.2f" % salario_liquido)

