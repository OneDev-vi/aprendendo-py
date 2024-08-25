print('-------Calculo de descontos abaixo-------')
Val = float(input("Escolha um valor para ser usado: "))
Des = float(input("Agora escolha o desconto desejado: "))

fn = float((Val*Des)/100)
fn2 = float(Val - fn)

print(f'Os {Des}% de desconto equivalem a R${fn:.2f} subtraídos do seu valor de R${Val:.2f}. Logo você pagará R${fn2:.2f}')