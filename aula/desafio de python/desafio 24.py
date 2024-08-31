valor = int(input("Informe um valor:> "))
#n = str(valor)
u = valor  // 1 % 10
d = valor  // 10 % 10
c = valor  // 100 % 10
m = valor  // 1000 % 10
dm = valor // 10000 % 10
cm = valor // 100000 % 10
ds = valor // 1000000 % 10
cmi = valor // 10000000 % 10
soma = u+d+c+m+dm+cm+ds+cmi
print (f"analizando numero {valor}\n Unidade: {u}\n dezena: {d}\n centena: {c}\n milhar: {m}\n desena de milhar: {dm}\n centena de milhar: {cm}\n dezena de milhão: {ds}\n centena de milhão {cmi}\n e a soma é {soma}")