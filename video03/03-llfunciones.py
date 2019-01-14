def saludo():
	print ("Hola que tal")
def despedida ():
    print ("Adios")	 
def calculaSuma():
    num1 = 1
    num2 = 14
    suma = num1 + num2
    return suma
def calculaSuma2(num1):
    suma = num1 + 3
    return suma
def calculaSuma3(num1, num2):
    suma = num1 + num2
    return suma

saludo()
despedida ()
saludo ()
print (calculaSuma ()) 
print (calculaSuma2(23))
print (calculaSuma3(23,12)) 
print (calculaSuma3(int(input("Primer número ")), int(input("Segundo número ")))) 