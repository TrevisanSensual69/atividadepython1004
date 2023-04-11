# pede ao usuário para informar o número total de eleitores
n = int(input("Informe o número total de eleitores: "))

# inicializa as variáveis de contagem de votos com zero
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

# pede ao usuário para cada eleitor votar em um dos três candidatos e atualiza as variáveis de contagem de votos
for i in range(n):
    print("Eleitor {}:".format(i+1))
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do candidato escolhido: "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido, tente novamente")
        continue

# mostra o resultado da eleição, exibindo o número de votos de cada candidato
print("Resultado da eleição:")
print("Candidato 1 - {} votos".format(votos_candidato1))
print("Candidato 2 - {} votos".format(votos_candidato2))
print("Candidato 3 - {} votos".format(votos_candidato3))
