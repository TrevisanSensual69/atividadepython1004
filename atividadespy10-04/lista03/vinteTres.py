turmas = int(input("Quantidade de turmas: "))
talunos = 0

for i in range(1, turmas+1):
    while True:
        qtdalunos = int(input(f"Quantidade de alunos na turma {i}: "))
        if qtdalunos > 0 and qtdalunos <= 40:
            talunos += qtdalunos
            break
        else:
            print("A quantidade de alunos não está certo, digite um número entre 1 e 40")

media = talunos / turmas
print(f"Média de alunos por turma é: {media:.2f}")