class Estudiant:
    def __init__(self,nombre="",edad=0,carrera=""):
        self._nombre=nombre
        self._edad=edad
        self._carrera=carrera
        self._matriculado=False
        self._pensionPa=False

    def getnombre(self):
        return self._nombre
    def setnombre(self,nombre=None):
        self._nombre = nombre

    def getedad(self):
        return self._nombre
    def setedad(self,nombre=None):
        self._nombre = nombre

    def getcarrera(self):
        return self._nombre
    def setcarrera(self,nombre=None):
        self._nombre = nombre
        
    def ingresarDatos(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
        self.carrera=input("Ingrese el nombre de su carrera: ")

    def imprimirDatos(self):
        print("DATOS DEL ESTUDIANTE")
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Carrera: ",self.carrera)
        if self.matriculado:
            print("Matriculado: Si")
        else:
            print("Matriculado: No")
        if self.pensionPa:
            print("Pensión pagada: Si")
        else:
            print("Pensión pagada: No")

    def matricular(self):
        self.matriculado=True
        print("Usted ha sido matriculado")

    def pagarPension(self):
        self.pensionPa=True
        print("Usted pagó la pensión")
