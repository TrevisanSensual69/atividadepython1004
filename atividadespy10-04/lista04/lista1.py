numero = int(input("Digite um número inteiro: "))
maior = numero
menor = numero

while numero >= 0:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    numero = int(input("Digite outro número inteiro: "))

print("O maior número lido foi:", maior)
print("O menor número lido foi:", menor)
