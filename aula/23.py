from random import shuffle
print ("O professor precisa numerar que dos qrupos vai apresentar primero")
aluno1 = str(input("qual o nome do aluno> "))
aluno2 = str(input("qual o nome do aluno> "))
aluno3 = str(input("qual o nome do aluno> "))
aluno4 = str(input("qual o nome do aluno> "))
list = [aluno1, aluno2, aluno3, aluno4]
shuffle(list)
print (f"o primeiro grupo escolhido foi {(list)}")