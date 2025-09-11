class Estudiante:
    def __init__(self,nombre="",edad=0,carrera=""):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        self.matriculado=False
        self.pensionPa=False

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
