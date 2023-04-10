
def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat
while True:
 
    num = None
    while num is None:
        try:
            num = int(input("Digite um número inteiro positivo e menor que 16 (ou digite 0 para encerrar): "))
            if num < 0 or num > 15:
                print("Número inválido! Informe um número entre 0 e 15.")
                num = None
        except ValueError:
            print("Valor inválido! Informe um número inteiro positivo e menor que 16.")
    if num == 0:
        break
    fat = fatorial(num)
    print(f"O fatorial de {num} é {fat}.")
