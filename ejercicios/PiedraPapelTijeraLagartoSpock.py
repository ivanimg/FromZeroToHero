import random 
contador = 3
opciones = ["piedra", "papel", "tijeras", "lagarto" , "spock"] 
while contador > 0:
    print ("Piedra, papel, tijeras, lagarto, spock!")
    opcion = input ("Introduce tu opcion: ")
    print ("Tu opcion es: ", opcion)
    oponente = random.randint(1,5) 
    print (opcion, opciones[oponente])
    if opcion == opciones(oponente):
        print ("Has empatado")
    elif opcion == "piedra" :
        if oponente == 2 :
            print ("Has ganado") 
            print ("Piedra rompe tijeras") 
        elif oponente == 1 :
            print ("Has perdido")
            print ("Papel envuelve piedra")
        elif oponente == 3 :
            print ("Has ganado")
            print ("Piedra aplasta Lagarto") 
        elif opcion_oponente == 4 :
            print ("Has perdido")
            print ("Spock vaporiza piedra") 
    elif opcion == "tijeras" :
        if opcion_oponente == 1 :
            print ("Has ganado")
            print ("Tijeras cortan papel") 
        elif opcion_oponente == 0 :
            print ("Has perdido")
            print ("Piedra rompe  tijeras")
        elif opcion_oponente == 3 :
            print ("Has ganado")
            print ("Tijeras decapitan Lagarto") 
        elif opcion_oponente == 4 :
            print ("Has perdido")
            print ("Spock rompe tijeras")
    elif opcion == "papel" :
        if opcion_oponente == 2 :
            print ("Has perdido") 
            print ("Tijeras cortan papel") 
        elif opcion_oponente == 0 :
            print ("Has ganado") 
            print ("Papel envuelve piedra") 
        elif opcion_oponente == 3 :
            print ("Has perdido")
            print ("Lagarto devora papel") 
        elif opcion_oponente == 4 :
            print ("Has ganado")
            print ("Papel desautoriza Spock")
    elif opcion == "lagarto" :
        if opcion_oponente == 2 :
            print ("Has perdido") 
            print ("Tijeras decapitan lagarto") 
        elif opcion_oponente == 0 :
            print ("Has perdido") 
            print ("Piedra aplasta lagarto") 
        elif opcion_oponente == 1 :
            print ("Has ganado")
            print ("Lagarto devora papel") 
        elif opcion_oponente == 4 :
            print ("Has ganado")
            print ("Lagarto envenena Spock")
    elif opcion == "spock" :
        if opcion_oponente == 2 :
            print ("Has ganado") 
            print ("Spock rompe tijeras") 
        elif opcion_oponente == 0 :
            print ("Has ganado") 
            print ("Spock vaporization piedra") 
        elif opcion_oponente == 3 :
            print ("Has perdido")
            print ("Lagarto envenena Spock") 
        elif opcion_oponente == 1 :
            print ("Has perdido")
            print ("Papel desautoriza Spock")
    else:
        print ("No has entendido el juego, Leonard") 
        print ("Banzingo")
    contador -= 1
    print ("Quedan ", contador, " intentos") 
print ("FIN del juego") 