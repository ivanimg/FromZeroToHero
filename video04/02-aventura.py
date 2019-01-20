personaje = [] 

def lootbox ():
    vida = 30
    print ("!Una lootbox salvaje apareció¡")
    while vida > 0:
    	   acción = input("atacar o escapar: ") 
    	   if acción == "atacar":
        	   vida = vida - personaje["fuerza"]
        	   if vida <= 0:
            	     print("Ganaste!!")
            	     print ("Tu premio es 2 monedas") 
            	     #personajes["dinero"] = personajes["dinero"] +2
            	     personajes["dinero"] =+ 2
            	#else:
                	 #print ("La lootbox ataca!!" )
        else:
            print ("Escapaste") 
            return
            	   
def room01 () :
    print ("En la habitación no hay nada, pero hay dos puertas") 
    print ("Una en el este y otra en el oeste") 
    direc = input ("¿oeste o este?") 
    if direc == "oeste":
        room02() 
    elif direc == "este" : 
        room03()
    elif direc == "sur":
        entrada() 

        
def room02 () :
    lootbox() 
    if direc == "oeste":
        room02() 
    elif direc == "este" :
        print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 
        room0
    
        
def room03 () :"""
    print ("En la habitación no hay nada, pero hay dos puertas") 
    print ("Una en el este y otra en el oeste") 
    direc = input ("¿oeste o este?") 
    if direc == "oeste":
        room02() 
    elif direc == "este" :
        print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 
        room03()"""

def entrada ():
    print ("Has entrado") 
    print ("En el norte una puerta") 
    print ("En el sur vuelves a la entrada") 
    direc = input ("¿norte o sur?") 
    if direc == "norte":
        room01() 
    else:
        print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 


print ("The quest for directasa. ")
print ("=======================")
print ("") 
print ("LA DIRECTASA LA ROBÓ UN MONO MAGO")
print ("La ha escondido en el fondo de una mazmorra")
print ("¿Quien quieres ser?") 
opcion = input("pazos, caliebre, enoc") 
if opcion == "pazos" :
    personaje ["nombre"] = "Pazos64" 
    personaje ["vida"] = 5
    personaje ["dinero"] = 10
    personaje ["fuerza"] = 10
elif opcion == "caliebre" :
    personaje ["nombre"] = "TheCaliebre" 
    personaje ["vida"] = 5
    personaje ["dinero"] = 15
    personaje ["fuerza"] = 5
elif opcion == "enoc" :
    personaje ["nombre"] = "Pazos" 
    personaje ["vida"] = 5
    personaje ["dinero"] = 5
    personaje ["fuerza"] = 15

print ("¿Quieres entrar en la mazmorra ", personaje["nombre"], "?")

respuesta = input("(si/no)")
if respuesta == "si":
    entrada() 
else:
    print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 
