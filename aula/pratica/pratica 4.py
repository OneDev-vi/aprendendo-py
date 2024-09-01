casa = float(input("Qual o valor da casa: R$"))
salário = float(input("salario do comprador: R$"))
anos = int(input("Quantos anos de financiamento?: "))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print (f"para pagar uma casa de R${casa} em {anos}")
print (f"a prestação sera de R${prestação:.2f}")
if (prestação <= minimo):
    print ("emprestimo pode ser consedido")
else:
    print ("emprestimo nao pode ser concedido")