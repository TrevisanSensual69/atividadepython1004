num = int(input("Digite o número de pessoas da turma: "))
idades = []

for i in range(num):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

media = sum(idades) / num

if media >= 0 and media <= 25:
    print("A turma é jovem")
elif media >= 26 and media <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")