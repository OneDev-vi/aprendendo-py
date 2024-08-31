vel = float(input("qual a velocidade do carro> "))
if (vel > 80):
    print ("você foi multado")
    multa = vel - 80
    print (f"sua multa é de {multa} reais")
else:
    print ("ta de boanes")