qntCigDia= int(input("Informe a quantidade de cigarros fumados por dia: "))
anosFumando= float(input("Quantos anos fumando? "))

# 1 ano = 365 dias

totalDiasFumando= (qntCigDia) * ((anosFumando)*365)

# tempo perdido por cigarro = 10 minutos
# 1440 minutos = 1 dia

tempoPerdido= (totalDiasFumando * 10)/1440
print(tempoPerdido, "dias")
