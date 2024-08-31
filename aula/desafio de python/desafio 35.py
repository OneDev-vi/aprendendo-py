salario = float(input("qual o salario do funcionario> "))
if salario <= 1450.50:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print ("quem ganhava R${:.2f} passa a gangar R${:.2f} agora".format(salario, novo))