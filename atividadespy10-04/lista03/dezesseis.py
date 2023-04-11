while True:
    n = int(input("Digite um número inteiro positivo menor que 16: "))
    if n < 0 or n >= 16:
        print("Número inválido, escreva denovo")
    else:
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        print(f"{n}! = {fatorial}")
        
    r = input("Deseja calcular outro fatorial? (s/n): ")
    if r.lower() == "n":
        break