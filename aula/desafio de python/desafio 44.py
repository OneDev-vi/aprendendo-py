peso = float(input("Qual o seu peso?> "))
altura = float(input("E qual a sua altura em (m)> "))
imc = peso / (altura ** 2)
print (f"o imc dassa pessoa é de {imc:.1f}")
if (imc < 18.5):
    print ("Voçê esta abaixo do texto")
elif (18.5 <= imc < 25):
    print ("Voçê esta no peso ideal")
elif (25 <= imc < 30):
    print ("Voçê esta sobre peso")
elif (30 <= imc < 40):
    print ("Voçê esta obeso")
elif (imc >= 40):
    print ("Voçê esta obeso morbido")