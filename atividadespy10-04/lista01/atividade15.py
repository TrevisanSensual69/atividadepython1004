PI = 3.1416 # constante PI com 4 casas decimais
raio = float(input("Digite o valor do raio da lata: "))
altura = float(input("Digite o valor da altura da lata: "))

volume = PI * (raio**2) * altura

print("O volume da lata de óleo é de {:.2f} unidades de volume.".format(volume))
