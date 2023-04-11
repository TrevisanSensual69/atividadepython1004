altura = float(input("Informe a altura em metros: "))
sexo = input("Informe o sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Para um homem com altura {altura:.2f}m, o peso ideal é {peso_ideal:.2f}kg.")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Para uma mulher com altura {altura:.2f}m, o peso ideal é {peso_ideal:.2f}kg.")
else:
    print("Sexo inválido. Informe M para masculino ou F para feminino.")
