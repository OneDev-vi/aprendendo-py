from datetime import date
atual = date.today().year
nacimento = int(input("que ano voçê naceu "))
idade = atual - nacimento
print (f"o atleta tem {idade} anos")
if idade <= 9:
    print ("voçê é um mirin")
elif idade <= 14:
    print ("infantil")
elif idade <= 19:
    print ("juvenil")
elif idade <= 25:
    print ("senior")
else:
    print ("master")