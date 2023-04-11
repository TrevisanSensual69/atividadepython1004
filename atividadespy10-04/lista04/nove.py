candidatos = {
    1: "Branco",
    2: "Nulo",
    3: "Kiko",
    4: "Chaves",
    5: "Chiquinha"
}

votos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

while True:
    voto = int(input("Digite o número do candidato: "))
    if voto == 666:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("O candidato não existe")

print("O resultado da votação é:")
for candidato, votos_recebidos in votos.items():
    print(f"{candidatos[candidato]}: {votos_recebidos} votos")