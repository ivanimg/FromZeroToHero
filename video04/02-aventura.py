def room 01 () :
    print ("En la habitación no hay nada, pero hay dos puertas") 
    print ("Una en el este y otra en el oeste") 
    direc = input ("¿norte o sur?") 
    if direc == "oeste":
        room02() 
    else:
        print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 

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
print ("¿Quieres entrar en la mazmorra?")

respuesta = input("(si/no)")
if respuesta == "si":
    entrada() 
else:
    print ("COBARDE, GALLINA, CAPITÁN DE LAS SARDINAS") 
