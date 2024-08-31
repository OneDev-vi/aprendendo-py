nome = str(input("Dijite seu nome completo> ")).strip()
dividindo = nome.split()
print (f"{nome.upper()}\n {nome.lower()}\n {len(nome)}\n e seu primeiro nome tem {dividindo[0]}")