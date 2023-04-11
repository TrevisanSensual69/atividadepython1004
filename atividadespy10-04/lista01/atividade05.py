numero = int(input("Digite um número no formato CDU: "))
c = numero // 100
du = numero % 100
d = du // 10
u = du % 10
novo_numero = u * 100 + d * 10 + c
print(novo_numero)

