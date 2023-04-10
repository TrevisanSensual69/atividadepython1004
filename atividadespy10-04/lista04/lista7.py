altura_lucas = 1.50
altura_apricocildo = 1.10
anos = 0

while altura_apricocildo <= altura_lucas:
    anos += 1
    altura_lucas += 0.02
    altura_apricocildo += 0.03
    print(f"Ano {anos}: Lucas tem {altura_lucas:.2f}m e Apricoçildo tem {altura_apricocildo:.2f}m")

print(f"Foram necessários {anos} anos para que Jonas alcançasse ou ultrapassasse Josberanilson.")
