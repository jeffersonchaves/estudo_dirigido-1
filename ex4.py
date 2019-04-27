salario = float(input("Informe o salario: "))
aumento = float(input("Informe a % de aumento: "))

print ("Aumento de",aumento , "%")

aumento = (aumento /100)

print ("Novo salario sera", (salario * aumento) + salario, "reais" )
