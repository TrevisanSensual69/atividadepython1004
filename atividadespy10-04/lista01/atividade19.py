conta = input("Digite o número da conta corrente: ")
inverso = conta[::-1] # Inverte a ordem dos dígitos
soma = 0
for i in range(len(conta)):
    soma += int(conta[i]) * (i+1)
    soma += int(inverso[i]) * (i+1)
digito_verificador = soma % 10
print("O dígito verificador da conta corrente {} é {}.".format(conta, digito_verificador))
