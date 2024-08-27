city = str(input("aonde voçê mora?:> ")).strip()
sabo = city.split()
#print (f"analizando sua resposta.....\n {"santo" in city}")
print (f"analizando sua resposta...\n {sabo[0].title() == "Santo"}")