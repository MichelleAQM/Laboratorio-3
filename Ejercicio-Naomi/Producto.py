class producto:
    def __init__(self,nombreProd,precio):
        self.__nombreProd=nombreProd
        self.__precio=precio
    def get_nombreProd(self):
        return self.__nombreProd
    def get_precio(self):
        return self.__precio
    def set_precio(self,precio2):
        if precio2>0:
            self.__precio=precio2
        else:
            print("Precio inválido")
    def set_cantidad(self,cantidad2):
        if cantidad2>=0:
            self.__cantidad=cantidad2
        else:
            print("Cantidad inválida")
    def mostrar(self):
        print(f"Producto: {self.__nombreProd} - Precio: S/{self.__precio}")
