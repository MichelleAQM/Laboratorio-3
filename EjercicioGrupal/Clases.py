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
            return False
    #def atacar:

class equipo():
    def __init__(self,nombre,bonificacion):
        self.nombre = nombre
        self.bonificacion = bonificacion

    def pantalla(self):
        print(self.nombre,"recibio una boniciacion de",self.bonificacion,"fuerza")

class enemigosBrainrots():
    def __init__(self,nombreEnemigos,salud,fuerza):
        self.nombreEnemigos = nombreEnemigos
        self.salud = salud
        self.fuerza = fuerza
        self.habilidades = []
    def vivo_o_muerto(self):
        if self.salud > 0:
            return True
        else:
            print("¡Felicidades derrotaste a",self.nombreEnemigos,"!")
    
