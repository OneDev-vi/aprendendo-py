from colorama import init, Fore, Style, Back
import pygame
pygame.init()
init()
print (Fore.BLUE + "==========Lojas Mangas e dollylinhos!!!==========")
print (Fore.GREEN + "-------------------------------------------------")
pedido = float(input(Fore.LIGHTGREEN_EX + "Qual o valor da compra?? R$"))
print (Fore.MAGENTA + "-----FORMAS DE PAGAMENTO-----")

print ("""
    [1] Á vista dinheiro/cheque
    [2] Á vista no cartão
    [3] 2x no cartão
    [4] 3x no cartão""")
op = int(input(Fore.YELLOW + "Qual a forma de pagamento desajado?> "))
if (op == 1):
    total = pedido - (pedido * 10 /100)
elif (op == 2):
    total = pedido - pedido * 5 /100
elif (op == 3):
    total = pedido
    parcela = total / 2
    print (f"sua compra vai ser parcela em 3x de R${parcela} SEM JURUS")
elif (op == 4):
    total = pedido + (pedido * 20 / 100)
    parc = int(input("quantas vezes no cartão?> "))
    parcela = total / parc
    print (f"a parcelando na quantidade que voçê desejou era de {parc} e com o parcelamento vai ser de {parcela} com juros")
print (Fore.LIGHTWHITE_EX + f"a sua compra de R${pedido:.2f} e vai ser de {total:.2f}")