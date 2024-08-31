dis = float(input("qual a distancia> "))
print (f"voce esta ppestes a começar uma viagem de {dis}km")
if (dis <= 200):
    preço = dis * 50
else:
    print ("voce tem que pagar mais")
    print (f"o preço do passagem é de {dis * 0.45}")