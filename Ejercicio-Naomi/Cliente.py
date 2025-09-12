class cliente:
    def __init__(self,dni,nombre):
        self.__dni=dni
        self.__nombre=nombre
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre2):
        self.__nombre=nombre2
    def mostrar(self):
        print(f"{self.__nombre} DNI: {self.__dni}")

