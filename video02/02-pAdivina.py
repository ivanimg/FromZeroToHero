import random
print ("Adivina el numero")
#salir = False
seguir = True
#while not salir:
numero = random.randint(1,10)
contador = 0
while seguir:
    seguir = True
    solucion = int(input ("Que numero es? ")) 
    if numero == solucion:
        print ("Has ganado") 
        #salir = True
        seguir = False
    elif numero > solucion:
        print ("Es mayor") 
    elif numero < solucion:
        print ("Es menor") 
    if seguir:
        contador += 1
        if contador == 3:
            print ("Paga para seguir jugando")
            contador = 0



