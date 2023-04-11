fitas = int(input("Digite a quantidade de fitas na locadora: "))
valor_aluguel = float(input("Digite o valor de aluguel por fita: "))

# Faturamento anual da locadora
terco_alugadas = fitas / 3
faturamento_anual = (terco_alugadas * valor_aluguel) * 12
print("O faturamento anual da locadora é de R$ {:.2f}.".format(faturamento_anual))

# Valor ganho com multas por mês
decimo_alugadas_atraso = terco_alugadas / 10
valor_multas_mes = (decimo_alugadas_atraso * valor_aluguel) * 0.1
print("O valor ganho com multas por mês é de R$ {:.2f}.".format(valor_multas_mes))

# Quantidade de fitas no final do ano
fitas_estragadas = fitas -  (fitas * 0.02)
fitas_reposicao = fitas_estragadas + (fitas_estragadas / 10)

fitas_finais = fitas - fitas_reposicao
print("A quantidade de fitas no final do ano é de {}.".format(int(fitas_finais)))





