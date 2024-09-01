from colorama import init, Fore, Back, Style
import pygame
pygame.init()
init()
print ("===========================================")
print ("-------------------------------------------")
print ("-------------PREÇOS DE CASAS---------------")
print (Fore.BLUE + "o valor da casa pequena é 10000.50") #obivio é brasil ne se acha que uma casa grande vai ser 10000 não ne kkkkkk
print (Fore.WHITE + "O VALOR DA CASA MEDIA É 20000.36")
print (Fore.LIGHTWHITE_EX + "O VALOR DA CASA GRANDE È 35000.50")
print ("---------ESCOLHA UMA CASA DEZEJADA---------")
print ("-------------------------------------------")
print ("===========================================")
qualacasa = str(input("Qual a casa desejada?> "))
quanto = float(input(Fore.LIGHTRED_EX + "Qual qual o valor que voçê ira pagar na casa???> "))

if (qualacasa.upper() == "PEQUENA"):
    print (Fore.YELLOW + "A casa escolhida foi pequena")
    if (quanto >= 10000.50):
        pygame.mixer.music.load("din.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.GREEN + "comprada")
    elif (quanto <= 10000.49):
        pygame.mixer.music.load("nao.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.RED + "Voçê não pode comprar a casa")
if (qualacasa.upper() == "MEDIA"):
    print (Fore.YELLOW + "Voçê escolheu a casa media")
    if (quanto >= 20000.36):
        pygame.mixer.music.load("din.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.GREEN + "Casa comprada meu chefia")
    elif (quanto <= 20000.35):
        pygame.mixer.music.load("nao.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.RED + "Voçê não pode comprar a casa")
if (qualacasa.upper() == "GRANDE"):
    print (Fore.YELLOW + "Voçê escolheu a casa grande")
    if (quanto >= 35000.50):
        pygame.mixer.music.load("din.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.GREEN + "Obrigada por comprar a casa meu nobre")
    elif (quanto <= 35000.49):
        pygame.mixer.music.load("nao.mp3")
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print (Fore.RED + "Shipa daqui seu pobre kkkkkkk")