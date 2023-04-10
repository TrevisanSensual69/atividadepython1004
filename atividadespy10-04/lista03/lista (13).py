# pede ao usuário para informar quantas pessoas serão incluídas na turma
n = int(input("Quantas pessoas serão incluídas na turma? "))

# inicializa a soma das idades com zero
soma_idades = 0

# pede ao usuário para informar a idade de cada pessoa e soma na variável 'soma_idades'
for i in range(n):
    idade = int(input("Informe a idade da pessoa {}: ".format(i+1)))
    soma_idades += idade

# calcula a média de idade da turma
media_idades = soma_idades / n

# verifica a faixa etária da turma de acordo com a média de idade e exibe a mensagem correspondente
if media_idades <= 25:
    print("A turma é jovem, com média de idade {:.1f} anos".format(media_idades))
elif media_idades <= 60:
    print("A turma é adulta, com média de idade {:.1f} anos".format(media_idades))
else:
    print("A turma é idosa, com média de idade {:.1f} anos".format(media_idades))
