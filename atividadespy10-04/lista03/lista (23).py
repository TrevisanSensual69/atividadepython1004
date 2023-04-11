nome = input("Digite seu nome: ")
while len(nome) <= 4:
    nome = input("Digite um nome válido (maior que 4 caracteres): ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite uma idade válida (entre 0 e 150): "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    salario = float(input("Digite um salário válido (maior que zero): "))

sexo = input("Digite seu sexo (f/m): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("Digite um sexo válido (f/m): ").lower()

estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Digite um estado civil válido (s/c/v/d): ").lower()

print("Informações validadas com sucesso!")
