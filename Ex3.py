valor = int(input("Digite uma nota entre 0 a 10: "))
while True:
    if (valor < 10 and valor > 0): 
        print ("Parabens!")
        break
    else:
        print("Valor invalido tente novamente")
        valor = int(input('Digite uma nota entre 0 a 10: '))
    