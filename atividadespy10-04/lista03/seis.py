while True:
    nome = input("Digite o seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de 3 caracteres!")
        
while True:
    idade = int(input("Digite a sua idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print("A idade deve estar entre 0 e 150!")
        
while True:
    salario = float(input("Digite o seu salário: "))
    if salario > 0:
        break
    else:
        print("Digete um número maior que 0")
        
while True:
    sexo = input("Digite o seu sexo (f/m): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("O sexo deve ser 'f' ou 'm'!")
        
while True:
    estado_civil = input("Digite o seu estado civil (s/c/v/d): ").lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print("O estado civil deve ser 's', 'c', 'v' ou 'd'!")
        
print("Todas as informações foram registradas")