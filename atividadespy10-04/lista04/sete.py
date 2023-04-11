altj = 1.50 
alta = 1.10 
taxacrescj = 0.02 
taxacresca = 0.03  
anos = 0 

while alta <= altj:
    anos += 1
    altj += taxacrescj
    alta += taxacresca
    print(f"Ano {anos}: Josberanilson tem {altj:.2f}m e Apricoçildo tem {alta:.2f}m")

print(f"Apricoçildo ultrapassou Josberanilson após {anos} anos.")