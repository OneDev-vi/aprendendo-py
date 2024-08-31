import random
a = random.randint(0 , 5)
#print (a)
seila = int(input("dijite o valor> "))
if (seila == a):
    print ("voçê venceu")
else:
    print ("voçê perdeu")
    print ("o numero secreto era {}".format(a))
    print ("o computador vençeu")