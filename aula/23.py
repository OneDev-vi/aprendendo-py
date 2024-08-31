from random import shuffle
print ("O professor precisa numerar que dos qrupos vai apresentar primero")
aluno1 = str(input("grupo 1 dijite com virgula> ")).split(", ")#so 4
aluno2 = str(input("grupo 2 dijite com vingula> ")).split(", ")#so 4
aluno3 = str(input("grupo 3 dijite com virgula> ")).split(", ")#so 4
aluno4 = str(input("grupo 4 dijite com virgula> ")).split(", ")#so 4
list = [aluno1, aluno2, aluno3, aluno4]
shuffle(list)
print (f"o primeiro grupo escolhido foi {(list)}")