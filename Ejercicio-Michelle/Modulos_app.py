class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def getNombre(self):
        return self.nombre
    def getCantidad(self):
        return self.cantidad
    def getPrecio(self):
        return self.precio
    
    def setCantidad(self,cantidad = 1):
        if cantidad <1:
            print("La cantidad no puede ser negativa")
            return False
        else:
            self.cantidad = cantidad
        