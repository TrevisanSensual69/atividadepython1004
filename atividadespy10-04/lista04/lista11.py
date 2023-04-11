quantidade_alunos_terceira_serie = 0
maior_quantidade_livros_quarta_serie = 0
quantidade_alunos_nao_gostam_redacao_terceira_serie = 0
total_alunos = 0

while True:
    serie = int(input("Digite a série do aluno (1 a 4) ou 0 para sair: "))
    if serie == 0:
        break
    
    livros_por_mes = int(input("Digite a quantidade de livros que o aluno lê por mês: "))
    gostam_redacao = int(input("O aluno gosta de fazer redação? (sim - 1, não - 0): "))
    
    if serie == 3:
        quantidade_alunos_terceira_serie += 1
        if gostam_redacao == 0:
            quantidade_alunos_nao_gostam_redacao_terceira_serie += 1
    
    if serie == 4 and livros_por_mes > maior_quantidade_livros_quarta_serie:
        maior_quantidade_livros_quarta_serie = livros_por_mes
        
    total_alunos += 1

    continuar = int(input("Deseja continuar? (sim - 1, não - 0): "))
    if continuar == 0:
        break

if quantidade_alunos_terceira_serie == 0:
    print("IMPOSSIVEL CALCULAR % NENHUM ALUNO NA 3a SERIE!")
else:
    porcentagem_alunos_nao_gostam_redacao_terceira_serie = (quantidade_alunos_nao_gostam_redacao_terceira_serie / quantidade_alunos_terceira_serie) * 100
    print("ALUNOS 3a SERIE: " + str(quantidade_alunos_terceira_serie))
    print("MAIOR QTD LIVROS 4a SERIE: " + str(maior_quantidade_livros_quarta_serie))
    print("NAO GOSTAM REDACAO 3a SERIE: {:.1f}%".format(porcentagem_alunos_nao_gostam_redacao_terceira_serie))
