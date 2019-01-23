def entrada() :
    print ("Has entrado")
    print ("Ves al norte una puerta") 
    print ("Al sur vuelves a la entrada") 
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
print ("¿Quieres entrar en la mazmorra?")
respuesta = input ("(si/no)")
if respuesta == "si" :
    entrada() 
else:
    print("COBARDE, GALLINA, CAPITÁN DE LA SARDINA") 