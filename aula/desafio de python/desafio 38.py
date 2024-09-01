valor = int(input("Dijite um numero inteiro> "))
print ("=====================================")
print ("-------------------------------------")
print ("""--Dijite um numero para a conversão--
       [ 1 ] Binario
       [ 2 ] Octal
       [ 3 ] Hexadecimal""")
opção = int(input("Dijite sua opçâo> "))
if (opção == 1):
    print ("{} convertido para binario é {}".format(valor, bin(valor)[2:]))
elif (opção == 2):
    print (f"{valor} Convertido para octal é {oct(valor)[2:]} ")
elif (opção == 3):
    print (f"{valor} Convertendo para hexadecimal vai ser {hex(valor)[2:]}")
else:
    print ("Opção invalida")