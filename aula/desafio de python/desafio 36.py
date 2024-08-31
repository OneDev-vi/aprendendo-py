print ("-=-"*20)
print ("TRIANGULO")
print ("-=-" * 20)
r1 = float(input("primeiro segimento> "))
r2 = float(input("segundo segmento> "))
r3 = float(input("terceiro segmento> "))
if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r1):
    print ("Os segmentos acima PODEM FORMAR triangulo")
else:
    print ("Os segmentos acima NÃo PODEM FORMAR triagulo")