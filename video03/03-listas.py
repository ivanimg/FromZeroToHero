import random 
lista = ["uno", "dos", "tres", "cuatro"]
print (lista[3])
print (lista [0])
print (lista [random.randint(0,3)] )
juego = ["piedra", "papel", "tijeras"] 
contador = 3
while contador > 0:
    opcion = input ("Introduce tu opcion: ")
    print ("Tu opcion es: ", opcion)
    oponente = random.randint(0,2)
    opcion_oponente = juego [oponente] 
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
    contador -= 1
    print ("Quedan ", contador, " intentos") 
print ("FIN del juego")