quantcds = int(input("Quantos CDs você tem na sua coleção: "))
tinvestido = 0

for i in range(1, quantcds + 1):
    valor_cd = float(input("Digite o valor do CD {}: R$".format(i)))
    while valor_cd <= 0 or valor_cd > 1000:
        valor_cd = float(input("Digite um valor certo para o CD {}: R$".format(i)))
    tinvestido += valor_cd

mgasto = tinvestido / quantcds

print("O valor total investido na coleção de CDs é de R${:.2f}.".format(tinvestido))
print("O valor médio gasto nos CDs é de R${:.2f}.".format(mgasto))