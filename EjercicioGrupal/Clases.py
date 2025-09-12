class Personaje():
    def __init__(self,nombreJugador,salud,fuerza):
        self.nombreJugador = nombreJugador
        self.salud = salud
        self.fuerza = fuerza
        self.equipo = None
        self.habilidades = []

    def getNombre(self):
        return self.nombreJugador
    def getSalud(self):
        return self.salud
    def getfuerza(self):
        return self.fuerza
    
    def setNombre(self,nombreJugador = None):
        self.nombreJugador=nombreJugador
    def setSalud(self,salud = None):
        self.salud=salud
    def setFuerza(self,fuerza = None):
        self.fuerza=fuerza
    
    def agregar_habilades(self,habilidad):
        self.habilidades.append(habilidad)
    
    def vivo_o_muerto(self):
        if self.salud > 0:
            return True
        else:
            print(self.nombreJugador,"ha sido derrotado.")
            return False
    #def atacar:

class equipo():
    def __init__(self,nombre,bonificacion):
        self.nombre = nombre
        self.bonificacion = bonificacion

    def pantalla(self):
        print(self.nombre,"recibio una bonificacion de",self.bonificacion,"fuerza")

class enemigosBrainrots():
    def __init__(self,nombreEnemigo,salud,fuerza):
        self.nombreEnemigo = nombreEnemigo
        self.salud = salud
        self.fuerza = fuerza
        self.habilidades = []
    def vivo_o_muerto(self):
        if self.salud > 0:
            return True
        else:
            print("¡Felicidades derrotaste a",self.nombreEnemigo,"!")
            return False
    # def atacar

class habilidades():
    def __init__(self,nombre,daño):
        self.nombre = nombre
        self.daño = daño

class Batalla():
    def __init__(self,personaje,brainrot):
        self.personaje = personaje
        self.brainrot = brainrot
    
    def inicia(self):
        print("Empieza la batalla")
        print(self.personaje.getNombre(),"VS",self.brainrot.nombreEnemigo)
        while self.personaje.vivo_o_muerto() and self.brainrot.vivo_o_muerto():
            print(self.personaje.getNombre,"ataco a",self.brainrot.nombreEnemigo)
            self.brainrot.salud = self.brainrot.salud - self.personaje.fuerza
            print(self.brainrot.nombreEnemigo,"quedo con",self.brainrot.salud,"de vida")