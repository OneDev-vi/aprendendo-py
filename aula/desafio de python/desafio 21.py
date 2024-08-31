from random import shuffle
# import random
aluno = str(input("Dijite o nome de um aluno: "))
aluno2 = str(input("outro nome: "))
aluno3 = str(input("mais um: "))
aluno4 = str(input("mais um: "))
list = [aluno, aluno2, aluno3, aluno4]
#random.shuffle(list)
shuffle(list)
print (f" a ordem sera de ")
print (list)