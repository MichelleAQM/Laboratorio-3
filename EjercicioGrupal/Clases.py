class Personaje():
    def __init__(self, nombreJugador="Jugador", salud=120, fuerza=10):
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
    def setNombre(self, nombreJugador=None):
        self.nombreJugador = nombreJugador
    def setSalud(self, salud=None):
        self.salud = salud
    def setFuerza(self, fuerza=None):
        self.fuerza = fuerza
    def agregar_habilidades(self, habilidad):
        self.habilidades.append(habilidad)
    def vivo_o_muerto(self):
        if self.salud > 0:
            return True
        else:
            print(self.nombreJugador, "ha sido derrotado.")
            return False
    def asignar_equipo(self, equipo):
        self.equipo = equipo
        self.fuerza += equipo.bonificacion + 10
        print(self.nombreJugador, "obtuvo el equipo", equipo.nombre, 
              "(+", equipo.bonificacion + 10, "fuerza total extra).")
    def usar_habilidad(self, enemigo):
        if not self.habilidades:
            print("No tienes habilidades disponibles.")
            return
        print("\nElige una habilidad:")
        for i, h in enumerate(self.habilidades):
            print(i+1, "-", h.nombre, "(Daño:", h.daño, ")")
        try:
            op = int(input("Opción: "))
            if 1 <= op <= len(self.habilidades):
                habilidad = self.habilidades[op-1]
                print(self.nombreJugador, "usó", habilidad.nombre, "contra", enemigo.nombreEnemigo)
                enemigo.salud -= abs(habilidad.daño)
                print(enemigo.nombreEnemigo, "quedó con", enemigo.salud, "de vida")
            else:
                print("Opción inválida, pierdes el turno.")
        except ValueError:
            print("Entrada no válida, pierdes el turno.")
class equipo():
    def __init__(self, nombre="Espada básica", bonificacion=5):
        self.nombre = nombre
        self.bonificacion = bonificacion

    def pantalla(self):
        print(self.nombre, "recibió una bonificación de", self.bonificacion, "fuerza")

class enemigosBrainrots():
    def __init__(self, nombreEnemigo="Supremacini Mauricini", salud=100, fuerza=12):
        self.nombreEnemigo = nombreEnemigo
        self.salud = salud
        self.fuerza = fuerza
        self.habilidades = []
    def vivo_o_muerto(self):
        if self.salud > 0:
            return True
        else:
            print("¡Felicidades derrotaste a", self.nombreEnemigo, "!")
            return False
    def agregar_habilidades(self, habilidad):
        self.habilidades.append(habilidad)
    def atacar(self, personaje):
        if self.habilidades:
            import random
            habilidad = random.choice(self.habilidades)
            print(self.nombreEnemigo, "usó", habilidad.nombre, "contra", personaje.getNombre())
            personaje.salud -= abs(habilidad.daño)
            print(personaje.getNombre(), "quedó con", personaje.salud, "de vida")
        else:
            print(self.nombreEnemigo, "atacó a", personaje.getNombre())
            personaje.salud -= self.fuerza
            print(personaje.getNombre(), "quedó con", personaje.salud, "de vida")

class habilidades():
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

class Batalla():
    def __init__(self, personaje, brainrot):
        self.personaje = personaje
        self.brainrot = brainrot
    def inicia(self):
        print("\n--- Empieza la batalla ---")
        print(self.personaje.getNombre(), "VS", self.brainrot.nombreEnemigo)
        while self.personaje.vivo_o_muerto() and self.brainrot.vivo_o_muerto():
            self.personaje.usar_habilidad(self.brainrot)
            if self.brainrot.salud <= 0:
                break
            self.brainrot.atacar(self.personaje)