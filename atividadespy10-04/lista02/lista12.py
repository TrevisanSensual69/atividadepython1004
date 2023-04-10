codigo = input("Digite o código do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maior_nota = max(nota1, nota2, nota3)
media = (4*maior_nota + 3*(nota1+nota2+nota3-maior_nota))/10

print(f"código={codigo} nota1={nota1:.2f} nota2={nota2:.2f} nota3={nota3:.2f} media={media:.2f} {'APROVADO' if media >= 5 else 'REPROVADO'}")
