nota1 = float(input("qual a nota do primeiro aluno> "))
nota2 = float(input("qual a nota do segumdo aluno> "))
media = (nota1 + nota2) / 2
if (media < 5.0):
    print ("Reprovado!!!")
elif (media >= 5.0 and 6.9):
    print ("RECUPERAÇÃO!!!")
elif (media > 7.0):
    print ("APROVADO!!!")