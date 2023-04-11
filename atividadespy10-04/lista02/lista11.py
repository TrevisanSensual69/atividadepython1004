def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False

   
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29  
        else:
            max_day = 28  
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    if day < 1 or day > max_day:
        return False

    return True



data = input("Digite a data no formato DD MM AAAA: ").split()
dia, mes, ano = int(data[0]), int(data[1]), int(data[2])

if is_valid_date(dia, mes, ano):
    print(f"{dia}/{mes}/{ano} é uma data válida!")
else:
    print(f"{dia}/{mes}/{ano} não é uma data válida!")
  
