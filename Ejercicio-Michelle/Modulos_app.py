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
    def MostrarProductos(self):
        f
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

class Venta():
    def __init__(self,cliente,metodo_pago):
        self.cliente = cliente           
        self.metodo_pago = metodo_pago
        self.productos = []
    
    def agregar_producto(self, producto, cantidad_comprada):
        if cantidad_comprada <= Producto.cantidad:
            self.productos.append((producto, cantidad_comprada))
            Producto.cantidad -= cantidad_comprada  
        else:
            print(f"No hay suficiente stock de {Producto.getNombreP()}")

    def calcular_total(self):
        total = 0
        for prod, cant in self.productos:
            total += prod.precio * cant
        return total

    def mostrar_factura(self):
        print("===== FACTURA =====")
        print(f"Cliente: {self.cliente.getNombreC()}")
        print(f"DNI: {self.cliente.getDNI()}")
        print("Productos:")
        for prod, cant in self.productos:
            print(f"{prod.getNombreP()} - Cantidad: {cant} - Subtotal: S/{prod.precio*cant}")
        print(f"Total a pagar: S/{self.calcular_total()}")
        print(f"Método de pago: {self.metodo_pago}")
        print("==================")