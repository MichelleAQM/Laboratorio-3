class Estudiant:
    def __init__(self,nombre="",edad=0,carrera=""):
        self._nombre=nombre
        self._edad=edad
        self._carrera=carrera
        self.matriculado=False
        self._ensionPa=False

    def getnombre(self):
        return self._nombre
    def setnombre(self,nombre=None):
        self._nombre = nombre
    nombre = property(fget = getnombre,fset=setnombre,doc=None)
    
    def getedad(self):
        return self._edad
    def setedad(self,edad=None):
        self._edad = edad
    edad = property(fget = getedad,fset=setedad,doc=None)

    def getcarrera(self):
        return self._carrera
    def setcarrera(self,carrera=None):
        self._carrera = carrera
    carrera = property(fget = getcarrera,fset=setcarrera,doc=None)

    def ingresarDatos(self,nombre=None, edad=None, carrera=None):
        if nombre == None:
            self._nombre=input("Ingrese su nombre: ")
        else: 
            self._nombre=nombre
        if edad == None:
            self._edad=int(input("Ingrese su edad: "))
        else:
            self._edad=edad
        if carrera == None:
            self._carrera=input("Ingrese el nombre de su carrera: ")
        else:
            self._carrera=carrera
        
    def imprimirDatos(self):
        print("DATOS DEL ESTUDIANTE")
        print("Nombre: ",self._nombre)
        print("Edad: ",self._edad)
        print("Carrera: ",self._carrera)
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
