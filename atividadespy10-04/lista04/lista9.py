votos_branco = 0
votos_nulo = 0
votos_kiko = 0
votos_chaves = 0
votos_chiquinha = 0

while True:
    print("VOTE 1 para votar em Branco")
    print("VOTE 2 para votar Nulo")
    print("VOTE 3 para votar Kiko")
    print("VOTE 4 para votar Chaves")
    print("VOTE 5 para votar Chiquinha")
    print("VOTE 666 para encerrar a votação")
    
    voto = int(input("Digite o número do seu voto: "))
    
    if voto == 666:
        break
    elif voto == 1:
        votos_branco += 1
    elif voto == 2:
        votos_nulo += 1
    elif voto == 3:
        votos_kiko += 1
    elif voto == 4:
        votos_chaves += 1
    elif voto == 5:
        votos_chiquinha += 1
    else:
        print("Voto inválido. Tente novamente.")
    
print("RESULTADO FINAL")
print(f"Votos em Branco: {votos_branco}")
print(f"Votos Nulos: {votos_nulo}")
print(f"Votos em Kiko: {votos_kiko}")
print(f"Votos em Chaves: {votos_chaves}")
print(f"Votos em Chiquinha: {votos_chiquinha}")
