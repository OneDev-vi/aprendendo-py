from colorama import init, Fore, Back, Style
init()
import random
a = random.randint(0 , 5)
#print (a)
print (Fore.YELLOW + "-=-"*10)
seila = int(input(Fore.BLUE + "dijite o valor> "))
if (seila == a):
    print (Fore.LIGHTBLUE_EX + "voçê venceu")
else:
    print (Fore.RED + "voçê perdeu")
    print (Style.DIM + "o numero secreto era {}".format(a))
    print (Style.BRIGHT + "o computador vençeu")
    
print (Back.CYAN + "=-="*10)