import random 
contador = 3
jugador = 99
opciones = ["piedra", "papel", "tijeras", "lagarto" , "spock"]
sheldon = ["mandinga", "varsovia", "Calista", "batista", "heitinga"] 
def elec_jugador (elección) :
    if elección == "piedra" :
        jugador = 0
    elif elección == "papel" :
        jugador = 1
    elif elección == "tijeras" :
        jugador = 2
    elif elección == "lagarto" :
        jugador = 3
    elif elección == "spock" :
        jugador = 4
while contador > 0:
    print ("Piedra, papel, tijeras, lagarto, spock!")
    opcion = input ("Introduce tu opcion: ")
    #elec_jugador(opcion) 
    #print ("Tu opcion es: ", opciones[jugador] )
    print ("Tu opcion es: ", opcion) 
    oponente = random.randint(1,5) 
    #print (opciones[jugador], opciones[oponente])
    print (opcion, opciones[oponente])
    if jugador == oponente:
        print ("Has empatado")
    elif opcion == "piedra" :
        if oponente == 2 | 3:
            print ("Has ganado") 
        elif oponente == 1 | 4 :
            print ("Has perdido") 
    elif opcion == "tijeras" :
        if opcion_oponente == 1 | 3 :
            print ("Has ganado") 
        elif opcion_oponente == 0 | 4 :
            print ("Has perdido") 
    elif opcion == "papel" :
        if opcion_oponente == 2 | 3:
            print ("Has perdido")
        elif opcion_oponente == 0 | 4:
            print ("Has ganado") 
    elif opcion == "lagarto" :
        if opcion_oponente == 2 | 0:
            print ("Has perdido") 
        elif opcion_oponente == 1 | 4 :
            print ("Has ganado")
    elif opcion == "spock" :
        if opcion_oponente == 2 | 0:
            print ("Has ganado")
        elif opcion_oponente == 3 | 1:
            print ("Has perdido")
    else:
        print ("No has entendido el juego, Leonard") 
        print (sheldon[oponente] )
    contador -= 1
    print ("Quedan ", contador, " intentos") 
print ("FIN del juego") 