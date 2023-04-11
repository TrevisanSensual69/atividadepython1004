while True:
    num = int(input("Informe um número: "))

    if num < 10 :
        print ("É menor que 10!")
        
    if num > 10 :
        print("É maior que 10!")
    resposta = int (input("Deseja realizar de novo?\n 1 - sim \n 2 - não \n"))
        
    if resposta == 2:
            break