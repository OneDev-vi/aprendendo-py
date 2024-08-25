import math
'''co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adigecente: "))
hr = (co ** 2 + ca ** 2) ** (1/2)
print (f"a hipotenusa vai ser {(co ** 2 + ca ** 2) ** (1/2)}")'''


#outra forma

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adigecente: "))
h1 = math.hypot(co , ca)
print (f"e o que voçê dijitou foi cateto oposto {co} e cateto adigecente {ca} a hipotenusa vai ser {math.hypot(co , ca)}")
