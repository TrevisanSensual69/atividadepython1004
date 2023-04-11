# pede ao usuário para informar a quantidade de CDs
n_cds = int(input("Informe a quantidade de CDs: "))

# inicializa as variáveis de contagem de CDs e de valor total investido com zero
total_cds = 0
total_valor = 0

# pede ao usuário para informar o valor investido em cada CD e atualiza as variáveis de contagem
for i in range(n_cds):
    print("CD {}:".format(i+1))
    valor_cd = float(input("Informe o valor investido: "))
    total_cds += 1
    total_valor += valor_cd

# calcula o valor médio investido em cada CD
if total_cds > 0:
    media_valor = total_valor / total_cds
else:
    media_valor = 0

# mostra o resultado, exibindo o valor total investido e o valor médio gasto em cada CD
print("O valor total investido em {} CDs é: R$ {:.2f}".format(total_cds, total_valor))
print("O valor médio gasto em cada CD é: R$ {:.2f}".format(media_valor))
