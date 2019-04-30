kmPercorrido= float(input("Quantos Km percorridos? "))
diasAlugado= int(input("Quantos dias foi de aluguel do carro? "))

#R$0.15 km rodado
#R$60.0 dia alugado

precoPagar= (kmPercorrido * 0.15) + (diasAlugado * 60.00)

print("Preco a pagar sera R$", precoPagar)