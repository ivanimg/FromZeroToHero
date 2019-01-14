import random
"""print ("Piedra, papel, tijeras!")
#Para python 2 -> raw_input 
opcion = raw_input ("Introduce tu opcion: ")
#Para python 3 -> input 
#opcion = input ("Introduce tu opcion: ")
print ("Tu opcion es: ", opcion)
oponente = random.randint(1,3)
if oponente == 1:
     opcion_oponente = "piedra" 
if oponente == 2:
    opcion_oponente = "tijeras" 
if oponente == 3:
    opcion_oponente = "papel" 
print (opcion, opcion_oponente) 
if opcion == "piedra" :
    if opcion_oponente == "tijeras" :
        print ("Has ganado") 
    if opcion_oponente == "papel" :
        print ("Has perdido") 
    if opcion_oponente == "piedra" :
        print ("Empate") 
elif opcion == "tijeras" :
    if opcion_oponente == "tijeras" :
        print ("Empate") 
    if opcion_oponente == "papel" :
        print ("Has ganado") 
    if opcion_oponente == "piedra" :
        print ("Has perdido")
if opcion == "papel" :
    if opcion_oponente == "tijeras" :
        print ("Has perdido") 
    if opcion_oponente == "papel" :
        print ("Empate") 
    if opcion_oponente == "piedra" :
        print ("Has ganado")"""
contador = 3
while contador > 0:
    print ("Piedra, papel, tijeras!")
    #Para python 2 -> raw_input 
    #opcion = raw_input ("Introduce tu opcion: ")
    #Para python 3 -> input 
    opcion = input ("Introduce tu opcion: ")
    print ("Tu opcion es: ", opcion)
    oponente = random.randint(1,3)
    if oponente == 1:
         opcion_oponente = "piedra" 
    elif oponente == 2:
        opcion_oponente = "tijeras" 
    elif oponente == 3:
        opcion_oponente = "papel" 
    print (opcion, opcion_oponente)
    if opcion == opcion_oponente :
        print ("Has empatado")
    elif opcion == "piedra" :
        if opcion_oponente == "tijeras" :
            print ("Has ganado") 
        elif opcion_oponente == "papel" :
            print ("Has perdido") 
    elif opcion == "tijeras" :
        if opcion_oponente == "papel" :
            print ("Has ganado") 
        elif opcion_oponente == "piedra" :
            print ("Has perdido")
    elif opcion == "papel" :
        if opcion_oponente == "tijeras" :
            print ("Has perdido") 
        elif opcion_oponente == "piedra" :
            print ("Has ganado") 
    #contador = contador-1
    contador -= 1
    print ("Quedan ", contador, " intentos") 
print ("FIN del juego") 