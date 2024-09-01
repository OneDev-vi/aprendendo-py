from datetime import date
atual = date.today().year
nasc = int(input("ano de nacimento: "))
idade = atual - nasc
print (f"quem naceu em {nasc} tem {idade} em {atual}")
if (idade == 18):
    print ("tem que alistar imediatamente")
elif (idade > 19):
    print ("tem que se alistar")
else:
    print ("Não precisa se alistar")
    print (f"fauta {nasc}")
print ()