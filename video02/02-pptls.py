import random 
contador = 3
while contador > 0:
    print ("Piedra, papel, tijeras, lagarto, spock!")
    #Para python 2 -> raw_input 
    #opcion = raw_input ("Introduce tu opcion: ")
    #Para python 3 -> input 
    opcion = input ("Introduce tu opcion: ")
    print ("Tu opcion es: ", opcion)
    oponente = random.randint(1,5)
    if oponente == 1:
         opcion_oponente = "piedra" 
    elif oponente == 2:
        opcion_oponente = "tijeras" 
    elif oponente == 3:
        opcion_oponente = "papel" 
    elif oponente == 4:
        opcion_oponente = "lagarto"
    elif oponente == 5:
        opcion_oponente = "spock"
    print (opcion, opcion_oponente)
    if opcion == opcion_oponente :
        print ("Has empatado")
    elif opcion == "piedra" :
        if opcion_oponente == "tijeras" :
            print ("Has ganado") 
            print ("Piedra rompe tijeras") 
        elif opcion_oponente == "papel" :
            print ("Has perdido")
            print ("Papel envuelve piedra")
        elif opcion_oponente == "lagarto" :
            print ("Has ganado")
            print ("Piedra aplasta Lagarto") 
        elif opcion_oponente == "spock" :
            print ("Has perdido")
            print ("Spock vaporiza piedra") 
    elif opcion == "tijeras" :
        if opcion_oponente == "papel" :
            print ("Has ganado")
            print ("Tijeras cortan papel") 
        elif opcion_oponente == "piedra" :
            print ("Has perdido")
            print ("Piedra rompe  tijeras")
        elif opcion_oponente == "lagarto" :
            print ("Has ganado")
            print ("Tijeras decapitan Lagarto") 
        elif opcion_oponente == "spock" :
            print ("Has perdido")
            print ("Spock rompe tijeras")
    elif opcion == "papel" :
        if opcion_oponente == "tijeras" :
            print ("Has perdido") 
            print ("Tijeras cortan papel") 
        elif opcion_oponente == "piedra" :
            print ("Has ganado") 
            print ("Papel envuelve piedra") 
        elif opcion_oponente == "lagarto" :
            print ("Has perdido")
            print ("Lagarto devora papel") 
        elif opcion_oponente == "spock" :
            print ("Has ganado")
            print ("Papel desautoriza Spock")
    elif opcion == "lagarto" :
        if opcion_oponente == "tijeras" :
            print ("Has perdido") 
            print ("Tijeras decapitan lagarto") 
        elif opcion_oponente == "piedra" :
            print ("Has perdido") 
            print ("Piedra aplasta lagarto") 
        elif opcion_oponente == "papel" :
            print ("Has ganado")
            print ("Lagarto devora papel") 
        elif opcion_oponente == "spock" :
            print ("Has ganado")
            print ("Lagarto envenena Spock")
    elif opcion == "spock" :
        if opcion_oponente == "tijeras" :
            print ("Has ganado") 
            print ("Spock rompe tijeras") 
        elif opcion_oponente == "piedra" :
            print ("Has ganado") 
            print ("Spock vaporiza piedra") 
        elif opcion_oponente == "lagarto" :
            print ("Has perdido")
            print ("Lagarto envenena Spock") 
        elif opcion_oponente == "papel" :
            print ("Has perdido")
            print ("Papel desautoriza Spock")
    else:
        print ("No has entendido el juego, Leonard") 
        print ("Banzingo")
    contador -= 1
    print ("Quedan ", contador, " intentos") 
print ("FIN del juego") 