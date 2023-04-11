while True:
    nomeu = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == nomeu:
        print("A senha não pode ser igual ao nome de usuário, escreva denovo")
    else:
        print("Login realizado")
        break 