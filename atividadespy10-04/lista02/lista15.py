idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
  categoria = "infantil A"
elif idade >= 0 and idade <= 4:
  categoria = "nenhuma, pois não há categoria para essa idade!"
elif idade >= 8 and idade <= 10:
  categoria = "infantil B"
elif idade >= 11 and idade <= 13:
  categoria = "juvenil A"
elif idade >= 14 and idade <= 17:
  categoria = "juvenil B"
else:
  categoria = "sênior"

print("O nadador tem {} anos e pertence à categoria {}".format(idade, categoria))
