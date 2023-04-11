while True:
    nome_usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if senha == nome_usuario:
        print("Erro: a senha não pode ser igual ao nome de usuário.")
    else:
        print("Nome de usuário e senha aceitos.")
        break
