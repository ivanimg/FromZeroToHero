import random 
personaje = {} 

def printEstado() :
    print ("vida", personaje["vida"], "dinero", personaje["dinero"], "fuerza", personaje["fuerza"] ) 

#def lootbox() :
def lootbox (vida, fuerza) :
    #vida = 30
    print ("Una lootbox salvaje apareció") 
    print ("tiene", vida, "puntos de vida") 
    while vida >0:
        
        opción = input ("¿atacar o escapar? ") 
        if opción == "atacar" :
            vida = vida - personaje["fuerza"] 
            if vida <= 0:
                print ("Ganaste!!!") 
                print ("Tu premio es 2 monedas") 
                #personaje["dinero"] = personaje["dinero"] + 2
                personaje["dinero"] +=2
            else:
                print ("Quedan", vida, "vidas") 
                print ("Lootbox ataca!!!") 
                print ("Pierdes", fuerza, "monedas") 
                personaje["dinero"] -=fuerza
            printEstado() 
        else:
            print ("Escapaste") 
            return 
       
def creaLootbox() :
    loot = random.randint (1,5) 
    if loot % 2 == 0:
        lootVida = random.randint (1,20)
        lootFuerza = random.randint (1,4)
        #lootbox (30,3)
        lootbox (lootVida,lootFuerza)
        
def room03() :
    print ("room 03") 
    print ("Esta habitación está vacía") 
    #print ("¿oeste?") 
    direc = input ("¿oeste? ") 
    if direc == "oeste" :
        room01() 
    
def room02() :
    print ("room 02") 
    lootbox (30,4)
    direc = input ("¿Este o norte ") 
    if direc == "norte" 

def room01() :
    print ("En la habitación no hay nada, pero hay dos puertas")
    print ("una al este, otra al oeste") 
    direc = input ("¿este u oeste?")
    if direc == "este" :
        room02() 
    elif direc == "oeste" :
        room03() 
    else:
        entrada() 
        
def entrada() :
    print ("Has entrado")
    print ("Ves al norte una puerta") 
    print ("Al sur vuelves a la entrada") 
    
    creaLootbox() 
        
    direc = input ("¿norte o sur?" ) 
    if direc == "norte" :
        room01() 
    elif direc == "sur" :
        print("COBARDE, GALLINA, CAPITÁN DE LA SARDINA") 


print ("The quest for directasa")
print ("=======================") 
print ("") 
print ("La directasa la robó un mono mago")
print ("La ha escondido en el fondo de una mazmorra")
print ("¿Quien quieres ser?") 
opcion = input ("pazos, caliebre, enoc ") 
if opcion == "pazos" :
    personaje["nombre"] = "Pazos"
    personaje["vida"] = 5
    personaje["dinero"] = 5
    personaje["fuerza"] = 15
elif opcion == "caliebre" :
    personaje["nombre"] = "Caliebre "
    personaje["vida"] = 5
    personaje["dinero"] = 15
    personaje["fuerza"] = 5
elif opcion == "enoc" :
    personaje["nombre"] = "Enoc"
    personaje["vida"] = 5
    personaje["dinero"] = 10
    personaje["fuerza"] = 10
print ("¿Quieres entrar en la mazmorra,", personaje["nombre"], "?")
respuesta = input ("(si/no)")
if respuesta == "si" :
    entrada() 
else:
    print("COBARDE, GALLINA, CAPITÁN DE LA SARDINA") 