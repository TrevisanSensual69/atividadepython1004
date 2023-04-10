valor_produto = float(input("Digite o valor do produto: "))
desconto = 0.09 # 9% de desconto

novo_valor = valor_produto * (1 - desconto)

print("O novo valor do produto com desconto é de R$ {:.2f}".format(novo_valor))

