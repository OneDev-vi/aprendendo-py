vel = int(input("qual a sua velocidade> "))
if (vel > 80):
    print ("voçê foi multado!!!")
    multa  = vel * 7
    print (f"voçê devera pagar {(vel-80) * 7}")
    
else:
    print ("voçê não foi multado.")