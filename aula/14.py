n1 = float(input("valor: "))
n2 = float(input("outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
res = n1 % n2

print ("a soma é {},\n e o produto é {},\n e a divisão é {:.4}\n".format(s , m , d))

print ("a potenciação vale {:.5},\n e a divisão inteira vale {}\n".format(e , di))

print ("o resto da divição é {}".format(res))