class Producto():
    def __init__(self,nombreP,cantidad,precio):
        self._nombreP = nombreP
        self._cantidad = cantidad
        self._precio = precio
    
    def getNombreP(self):
        return self._nombreP
    def getCantidad(self):
        return self._cantidad
    def getPrecio(self):
        return self._precio
    
    def setCantidad(self,cantidad = 1):
        if cantidad <1:
            print("La cantidad no puede ser negativa")
        else:
            self._cantidad = cantidad
    def setPrecio(self,precio = None):
        if precio <0:
            print("El precio no puede ser negativo")
        else:
            self._precio = precio
    cantidad = property(fget = getCantidad,fset=setCantidad)
    precio = property(fget=getPrecio,fset=setPrecio)

class Cliente():
    def __init__(self,nombreC,edad,DNI):
        self._nombreC = nombreC
        self._edad = edad
        self._DNI = DNI
    
    def getNombreC(self):
        return self._nombreC
    def getEdad(self):
        return self._edad
    def getDNI(self):
        return self._DNI
    
    def setEdad(self,edad = None):
        if edad <0:
            print("Su edad no puede ser negativa")
        elif edad <18:
            print("Usted es menor de edad")
        else:
            self._edad = edad
    def setDNI(self,DNI = None):
        if len(DNI)==8 and DNI.isdigit() :
            print("Se ingreso correctamente su DNI")
            self._DNI = DNI
        else:
            print("Su DNI es incorrecto")
    edad = property(fget = getEdad,fset=setEdad)
    DNI = property(fget=getDNI,fset=setDNI)

class Venta(Cliente,Producto):
    def __init__(self, nombreC, edad, DNI,nombreP,cantidad,precio,total,metodoPago):
        Cliente().__init__(nombreC, edad, DNI)
        Producto().__init__(nombreP, cantidad, precio)
        self.total = total
        self.metodoPago = metodoPago    

    def getTotal(self):
        return self._edad
    def getmetodoPago(self):
        return self._DNI
    
    def setEdad(self,edad = None):
        if edad <0:
            print("Su edad no puede ser negativa")
        elif edad <18:
            print("Usted es menor de edad")
        else:
            self._edad = edad
    def setDNI(self,DNI = None):
        if len(DNI)==8 and DNI.isdigit() :
            print("Se ingreso correctamente su DNI")
            self._DNI = DNI

