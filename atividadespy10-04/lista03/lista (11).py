# Solicita que o usuário informe um número inteiro
n = int(input("Digite um número inteiro: "))

# Variável para contar o número total de divisões
divisoes_totais = 0

# Loop que percorre todos os números de 1 a N
for num in range(1, n+1):

    # Verifica se o número é primo
    divisores = []
    for i in range(2, num):
        divisoes_totais += 1
        if num % i == 0:
            divisores.append(i)

    # Imprime o resultado
    if len(divisores) == 0:
        print(num, "é um número primo.")

# Imprime o total de divisões realizadas
print("Número total de divisões realizadas:", divisoes_totais)
