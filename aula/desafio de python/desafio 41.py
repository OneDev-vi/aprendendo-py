nota1 = float(input("qual a nota do primeiro aluno> "))
nota2 = float(input("qual a nota do segumdo aluno> "))
media = (nota1 + nota2) / 2
print (f"tirando {nota1} e {nota2} é media do aluno é {media}")
if (7 > media >= 5):
    print ("o aluno esta de recuperaçaõ")
elif (media < 5):
    print ("esta reprovado")
elif (media >= 7):
    print ("esta aprovado")