n1 = float(input("qual a nota do primeiro aluno?> "))
n2 = float(input("qual a nota do segundo aluno?> "))
so = (n1 + n2)/2

if (so >= 7.0):
    print ("sua media foi boa!!")
    print ("parabens!!")
elif (so <= 5.0):
    print ("sua media foi ruim!!")
    print ("tente novamente!!")
elif (so >= 6.5):
    print ("sua media foi mediana!!")
    print ("continue assim!!")