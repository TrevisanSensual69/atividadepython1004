candi = [0, 0, 0] #lista com o número de votos de cada candidato

neleitores = int(input("Digite o número total de eleitores: "))

for i in range(neleitores):
    voto = int(input(f"Eleitor {i+1}, vote em um candidato (1, 2 ou 3): "))
    candi[voto-1] += 1

print("Número de votos de cada candidato:")
print(f"Candidato 1: {candi[0]} votos")
print(f"Candidato 2: {candi[1]} votos")
print(f"Candidato 3: {candi[2]} votos")