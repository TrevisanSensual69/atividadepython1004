# pede ao usuário para informar a quantidade de turmas
n_turmas = int(input("Informe a quantidade de turmas: "))

# inicializa a variável de contagem de alunos com zero
total_alunos = 0

# pede ao usuário para informar a quantidade de alunos em cada turma e atualiza a variável de contagem de alunos
for i in range(n_turmas):
    print("Turma {}:".format(i+1))
    n_alunos = int(input("Informe a quantidade de alunos (até 40): "))
    if n_alunos <= 40:
        total_alunos += n_alunos
    else:
        print("Quantidade inválida de alunos, tente novamente")
        continue

# calcula a média de alunos por turma
if n_turmas > 0:
    media_alunos = total_alunos / n_turmas
else:
    media_alunos = 0

# mostra o resultado, exibindo o número médio de alunos por turma
print("O número médio de alunos por turma é: {:.2f}".format(media_alunos))
