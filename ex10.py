import math

metropinta = int(input('Qual o tamanho a pintar em m²? '))
litrosncesse = (metropinta / 6)

#a
#comprando apenas latas de 18 litros
latasnecesse = (math.ceil(litrosncesse / 18))
if latasnecesse <= 1:
    print("a) Sera necessario", latasnecesse, "lata.")
else:
    print("a) Sera necessario", latasnecesse, "latas.")

#b
#comprando apenas galoes de 3.6 litros
galoesnecesse = math.ceil(litrosncesse / 3.6)
if galoesnecesse <= 1:
    print("b) Sera necessario", galoesnecesse, "galao.")
else:
    print("b) Sera necessario", galoesnecesse, "galoes.")

#c
#cXb por latas e galoes
latasnecesse = int(litrosncesse / 18)
faltou = litrosncesse % 18
galoesnecesse = math.ceil(faltou / 3.6)

if latasnecesse <= 1:
    print("c) Compre", latasnecesse, "lata,")
else:
    print("c) Compre", latasnecesse, "latas,")
if galoesnecesse <=1:
    print(" e compre", galoesnecesse, "galao.")
else:
    print(" e compre", galoesnecesse, "galoes.")
