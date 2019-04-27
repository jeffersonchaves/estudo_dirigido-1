preco = float(input("Informe o preco: "))
desc = float(input("Informe o % do desconto: "))

print ("Desconto de",desc,"%")

desc = (desc /100)

print ("Preco a pagar:", preco - (preco * desc) , "reais" )
