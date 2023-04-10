# pede ao usuário para informar quantas notas serão usadas no cálculo da média
n = int(input("Quantas notas serão usadas para o cálculo da média? "))

# inicializa a soma das notas com zero
soma = 0

# pede ao usuário para informar cada nota e soma na variável 'soma'
for i in range(n):
    nota = float(input("Informe a nota {}: ".format(i+1)))
    soma += nota

# calcula a média aritmética
media = soma / n

# mostra o resultado da média aritmética
print("A média aritmética das {} notas informadas é {:.2f}".format(n, media))
