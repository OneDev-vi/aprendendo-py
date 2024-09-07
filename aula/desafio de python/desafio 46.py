from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0,2)
print ("""Suas opçoes
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    """)
jogador = int(input("Qual a sua jogada?> "))
print ("-="*11)
print (f"computador jogou {(itens[pc])}")
print (f"jogador jogou {(itens[pc])}")
