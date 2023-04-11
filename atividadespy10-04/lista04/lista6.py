def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def print_conversion_table(lower_limit, upper_limit, decrement):
    print(f'Celsius\t Fahrenheit')
    celsius = upper_limit
    while celsius >= lower_limit:
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f'{celsius:.1f}C\t {fahrenheit:.1f}F')
        celsius -= decrement

lower_limit = float(input("Digite o limite inferior do intervalo em graus Celsius: "))
upper_limit = float(input("Digite o limite superior do intervalo em graus Celsius: "))
decrement = float(input("Digite o decremento a ser utilizado: "))

print_conversion_table(lower_limit, upper_limit, decrement)
