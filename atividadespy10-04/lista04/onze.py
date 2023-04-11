qtdalunosterceira = 0
qtdlivroquarta = 0
naogostaredacao = 0
qtdalunos = 0

while True:
    serie = int(input("Digite a série do aluno de 1 a 4: "))
    if serie == 0:
        break
    qtd_livros = int(input("Digite a quantidade de livros que o aluno lê por mês: "))
    gostar_redacao = int(input("O aluno gosta de fazer redação: 1 - sim, 0 - não: "))
    
    if serie == 3:
        qtdalunosterceira += 1
    
    if serie == 4 and qtd_livros > maior_qtd_livros_quarta:
        maior_qtd_livros_quarta = qtd_livros
    
    if serie == 3 and gostar_redacao == 0:
        naogostaredacao += 1
    
    qtdalunos += 1

if qtdalunosterceira > 0:
    porcentagem_nao_gosta_redacao_terceira = (naogostaredacao / qtdalunosterceira) * 100
else:
    porcnaogostared = 0

print("Quantidade de alunos na terceira série é de:", qtdalunosterceira)
print("A maior quantidade de livros lidos por um aluno da quarta série é de:", qtdlivroquarta)
print("A porcentagem de alunos que não gostam de fazer redação é de:", porcnaogostared, "%")