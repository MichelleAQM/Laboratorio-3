class Venta:
    def __init__(self,cliente, producto, cantidad):
        self.__cliente=cliente
        self.__producto=producto
        self.__cantidad=cantidad
        if cantidad<=producto.get_cantidad():
            self.__total=producto.get_precio()*cantidad
            producto.set_cantidad(producto.get_cantidad()-cantidad)
        else:
            self.__total=0
            print("No hay suficientes productos para esta venta")
    def get_cliente(self):
        return self.__cliente
    def get_producto(self):
        return self.__producto
    def get_cantidad(self):
        return self.__cantidad
    def get_total(self):
        return self.__total
    def mostrar(self):
        print(f"Cliente: {self.__cliente.get_nombre()}|"
              f"Producto: {self.__producto.get_nombre()}|"
              f"Cantidad: {self.__cantidad}|"
              f"Total: S/{self.__total}")