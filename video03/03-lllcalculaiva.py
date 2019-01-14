factura = 100
iva = 0.21
factura_iva = factura + factura*iva
print (factura_iva) 
def calculaIVA() :
    lootbox = 100
    iva = 0.21
    lootbox_iva = lootbox + lootbox*iva
    return lootbox_iva
print (calculaIVA())
def calculaIVA2(lootbox) :
    iva = 0.21
    lootbox_iva = lootbox + lootbox*iva
    return lootbox_iva
print ("El iva de la lootbox es ", calculaIVA2(120)) 